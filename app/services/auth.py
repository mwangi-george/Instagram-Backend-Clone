
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from sqlalchemy import or_
from sqlalchemy.orm import Session
from fastapi import HTTPException, status, BackgroundTasks
from jose import jwt, JWTError

from ..models import User
from ..schemas.auth import UserCreate, ChangePasswordSchema
from ..security import Security

security = Security()


class AuthServices:
    """ Class to manage users """
    def __init__(self):
        pass

    @staticmethod
    def create_user(user_data: UserCreate, db: Session):
        """ Create a new user """
        db_existing_user = db\
            .query(User)\
            .filter(or_(User.email == user_data.email, User.username == user_data.username))\
            .first()

        # If a user exists, check their email and username - these fields should be unique
        if db_existing_user:
            if db_existing_user.email == user_data.email:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail=f'email: {user_data.email} is already registered'
                )
            elif db_existing_user.username == user_data.username:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail=f'username: {user_data.username} is not available'
                )
        # create a new user if none is found in the database
        else:
            db_user = User(
                email=user_data.email,
                username=user_data.username,
                password=security.get_password_hash(user_data.password)
            )
            # add the new user to database
            try:
                db.add(db_user)
                db.commit()
                db.refresh(db_user)
                return f'{user_data.username} registered successfully'
            except Exception:
                db.rollback()
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail='Could not register user. Something went wrong!'
                )

    @staticmethod
    def login_user(username: str, password: str, db: Session):
        """ Login user with given credentials """
        user = security.authenticate_user(username, password, db)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail='Incorrect username or password'
            )
        access_token = security.create_access_token(data={'sub': user.username})
        return {'access_token': access_token, 'token_type': 'Bearer'}

    @staticmethod
    def send_email(recipient: str, token: str):
        """ Helper function for sending email to given recipient """
        sender = security.ADMIN_EMAIL
        pwd = security.ADMIN_EMAIL_PASSWORD
        reset_link = f"http://127.0.0.1:8000/auth/validate-reset-token?token={token}"  # Confirmation Url

        email_body = f"""
                <html>
                <body>
                 <p>Hi there! 
                 <br>Click the link to reset your password: {reset_link}</p>
                </body>
                </html>
                """
        message = MIMEMultipart("alternative", None, [MIMEText(email_body, 'html')])
        message["Subject"] = "Password Reset: Instagram"
        message["From"] = sender
        message["To"] = recipient

        try:
            server = smtplib.SMTP('smtp.gmail.com:587')
            server.ehlo()
            server.starttls()
            server.login(sender, pwd)
            server.sendmail(sender, recipient, message.as_string())
            server.quit()
            print("Password reset email sent")
        except Exception as e:
            print(f"Error in sending email: {e}")

    async def send_password_reset_email(self, recipient: str, background_tasks: BackgroundTasks, db: Session) -> str:
        """ Function for sending email to a verified user """
        # check whether user exists by email
        user = db.query(User).filter_by(email=recipient).first()
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found')

        # create reset token
        reset_token = security.create_access_token(data={'sub': user.email}, for_password_reset=True)

        # send the email in the background
        background_tasks.add_task(self.send_email, user.email, reset_token)
        return "Password Reset Request sent"

    @staticmethod
    def validate_reset_token(token: str) -> str:
        """ Function to validate a token """
        try:
            payload = jwt.decode(token, security.JWT_SECRET_KEY, algorithms=[security.ALGORITHM])
            email: str = payload.get('sub')
            if email is None:
                raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid token')
            return email
        except JWTError:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid or expired token!')

    def reset_password(self, token: str, new_password, db: Session):
        """ Function to reset password """
        user_email = self.validate_reset_token(token)
        user = db.query(User).filter_by(email=user_email).first()
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found')
        try:
            user.password = security.get_password_hash(new_password)
            db.add(user)
            db.commit()
            db.refresh(user)
            return 'Password has been Changed successfully'
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))



