from app import app
from app.api import router as api_router

app.include_router(api_router)
