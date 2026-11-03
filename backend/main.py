from fastapi import FastAPI
from loguru import logger
from pydantic import BaseModel

app=FastAPI()

class Message(BaseModel):
    text: str

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/health")
def health():
    return {"message": "L'API est opérationnelle"}

@app.post("/chat")
def chat(message: Message):
    logger.info(f"Message reçu : {message.text}")
    return {"message": "Le message a été reçu."}
