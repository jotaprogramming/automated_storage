from fastapi import FastAPI

app = FastAPI(
    title = "Automated Storage",
    description = "Automatic automation for CoexBuster warehousing",
    version = "0.0.1",
    openapi_tags = [{
        "name": "Actors",
        "description": "Actors Routes"
    }]
)

