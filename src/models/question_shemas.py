from typing import List
from pydantic import BaseModel,Field,validator


class MCQQuestion(BaseModel):
    question: str = Field(description="the question text")

    options: List[str] = Field(description="list of 4  questions")

    correct_answer: str = Field(description="correct answer from the question") 



    @validator('question', pre=True)
    def clean_question(cls,v):
        if isinstance(v, dict):
            return v.get('description', str(v))
        return str(v)
    

class FillBlankQuestion(BaseModel):
    question: str = Field(description="the question with ____ in it")

    answer: str = Field(description="the correct answer for the blank")

    @validator('question', pre=True)
    def clean_question(cls,v):
        if isinstance(v, dict):
            return v.get('description', str(v))
        return str(v)