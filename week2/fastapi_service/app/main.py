from fastapi import FastAPI
from . import similar_words

app = FastAPI()
app.include_router(similar_words.router)
