from fastapi import APIRouter
from pydantic import BaseModel
from word_vectors import read
import numpy as np
import os
from dotenv import load_dotenv

load_dotenv()
VEC_PATH = os.getenv("VEC_PATH")

v, wv = read(VEC_PATH)

def cosine_sim(v1, v2):
    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))

class Query(BaseModel):
    query_word: str
    k: int

class SimilarWords(BaseModel):
    similar_words: dict[str, float]
    k: int

router = APIRouter()

@router.post('/similar_words')
async def get_k_similar_words(word_request: Query):
    similarity_dict = {}
    for word, idx in list(v.items()):
        similarity_dict[word] = cosine_sim(wv[idx], wv[v[word_request.query_word]])
    similarity_dict = {key: val for key, val in sorted(similarity_dict.items(), key=lambda item: item[1], reverse=True)[:word_request.k]}
    return SimilarWords(similar_words=similarity_dict, k=word_request.k)
