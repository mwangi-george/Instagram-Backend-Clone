from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from dotenv import load_dotenv
import os

# load environment variables
load_dotenv()


def create_homepage_router() -> APIRouter:
    """ Creates homepage API Router """
    router = APIRouter(
        tags=["Homepage"],
        include_in_schema=False,
    )

    # create a template object
    template = Jinja2Templates(directory="templates")

    # Swagger documentation
    swagger_url = os.getenv("API_SWAGGER_URL")

    @router.get("/", response_class=HTMLResponse)
    async def homepage(request: Request):
        return template.TemplateResponse(
            request=request,
            name="index.html",
            context={"swagger_url": swagger_url}
        )

    return router
