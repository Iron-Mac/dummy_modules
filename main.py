from typing import Union
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel


from model_evaluation import print_word_tag
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

app = FastAPI()

class Input1(BaseModel):
    input_data: str


class Input2(BaseModel):
    phrase1: str
    phrase2: str

@app.post("/postager/")
async def postagger(user_input: Input1):
    res = print_word_tag(user_input.input_data)
    return {"output_list": res}