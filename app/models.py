from pydantic import BaseModel

class WordStats(BaseModel):
    word: str
    tf: int
    idf: float
