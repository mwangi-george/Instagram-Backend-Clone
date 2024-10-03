from fastapi import FastAPI


def create_app_entry_point() -> FastAPI:
    """ Creates FastAPI app entry point """

    entry_point = FastAPI(
        title="Instagram Backend",
        description="Instagram Backend Clone",
        version="1.0.0",

    )
    return entry_point


app = create_app_entry_point()
