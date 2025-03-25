# (c) 2025, Gabriel Dzodom
# All rights reserved.

from contextlib import asynccontextmanager
from fastapi import FastAPI

from src.services.podcasts import routers
from src.services.podcasts.storage import Storage

app = FastAPI()

app.include_router(router=routers.router)

@app.on_event("startup")
async def startup():
    Storage().initialize()