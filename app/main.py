from fastapi import FastAPI
from .routes import home_router


def create_app_entry_point() -> FastAPI:
    """ Creates FastAPI app entry point """

    entry_point = FastAPI(
        title="Instagram Backend",
        description="Instagram Backend Clone",
        version="1.0.0",
    )

    # initialize routers
    home_routes = home_router()

    # include routers in the entry point
    entry_point.include_router(home_routes)

    return entry_point


app = create_app_entry_point()
