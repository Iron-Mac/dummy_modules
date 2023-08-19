from typing import Union
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel


from model_evaluation import print_word_tag
from TextRankMedium import textrank
from Roge import roge
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
    return {"res": res}

@app.post("/textrank/")
async def textrank(user_input: Input1):
    res = textrank(user_input.input_data)
    return {"res": res}

@app.post("/roge/")
async def rouge(user_input: Input2):
    res = roge(user_input.phrase1, user_input.phrase2)
    return {"res": res}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)