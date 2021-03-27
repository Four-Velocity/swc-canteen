from fastapi import FastAPI
from apps.common.routers import router as common_router


app = FastAPI()

app.include_router(common_router)
