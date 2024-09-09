from fastapi import FastAPI
from database.database import engine
from database import models
from router.router import router

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(router=router)

