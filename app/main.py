from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import items
from app.database import engine, Base
from app.auth import router as auth_router
from app.routers import users

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Set allowed origins, methods, and headers
origins = [
    "http://localhost",
    "http://localhost:3000",  # Add your frontend URL here
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["Authorization", "Content-Type"],
)

app.include_router(auth_router)
app.include_router(users.router)
app.include_router(items.router)
