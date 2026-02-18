from fastapi import FastAPI
from app.database import engine, Base

app = FastAPI()

# Create tables automatically
Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
    return {"message": "Real Estate Platform Connected to MySQL"}
