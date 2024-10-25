from fastapi import APIRouter, status, Depends, BackgroundTasks
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from ..models import get_db
from ..services.auth import AuthServices
from ..schemas.auth import (
    ActionConfirm,
    TokenCreate,
    UserCreate,
    PasswordResetRequest,
    ChangePasswordSchema,
)


def create_auth_router() -> APIRouter:
    router = APIRouter(
        prefix="/auth",
        tags=["Authentication"],
    )

    # instantiate UserServices class with implementation logic
    auth_services = AuthServices()

    # ------------------User Sign Up--------------------------
    @router.post(
        path="/signup", response_model=ActionConfirm, status_code=status.HTTP_201_CREATED,
        name="signup", description="Register user"
    )
    async def create_user(user_data: UserCreate, db: Session = Depends(get_db)):
        response = auth_services.create_user(user_data, db)
        formated_response = ActionConfirm(msg=response)
        return formated_response

    # ------------------User Login--------------------------
    @router.post(
        path="/login", response_model=TokenCreate, status_code=status.HTTP_200_OK,
        name="login", description="User Login"
    )
    async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
        token = auth_services.login_user(form_data.username, form_data.password, db)
        return token

    # ------------------Reset Password Request--------------------------
    @router.post(
        path="/request-password-reset", response_model=ActionConfirm, status_code=status.HTTP_200_OK,
        name="password reset request", description="Request to change password"
    )
    async def request_password_reset(recipient: PasswordResetRequest, background_tasks: BackgroundTasks, db: Session = Depends(get_db)):
        confirmation_message = await auth_services.send_password_reset_email(recipient.email, background_tasks, db)
        formated_response = ActionConfirm(msg=confirmation_message)
        return formated_response

    # ------------------Verify token’s existence, validity, and expiration.--------------------------
    @router.get(
        path="/validate-reset-token", response_model=ActionConfirm, status_code=status.HTTP_200_OK,
        name="validate password reset token", description="Validate password reset token"
    )
    async def validate_reset_token(token: str):
        response = auth_services.validate_reset_token(token)
        formated_response = ActionConfirm(msg="Success! Token has been validated")
        return formated_response

    # ------------------Update Password--------------------------
    @router.post(
        path="/reset-password", response_model=ActionConfirm, status_code=status.HTTP_200_OK,
        name="reset password", description="Reset user password"
    )
    async def reset_password(data: ChangePasswordSchema, db: Session = Depends(get_db)):
        confirmation_message = auth_services.reset_password(data.token, data.new_password, db)
        formated_response = ActionConfirm(msg=confirmation_message)
        return formated_response

    return router
