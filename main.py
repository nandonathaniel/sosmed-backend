from fastapi import FastAPI
import model
from routes import router
from config import engine
from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://localhost",
    "http://localhost:3000",
]



model.Base.metadata.create_all(bind=engine)

app = FastAPI(title = "My First REST API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router, prefix="/tweet", tags=["tweet"])