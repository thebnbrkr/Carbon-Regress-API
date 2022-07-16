from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello":"World"}

@app.get("/ALNTS")
def get_user():
    return {
        "eng_name":"Ailanthus",
        "sci_name":"Ailanthus altissima ",
        "oth_name":"Tree of heaven",
        "type"    :"Deciduous",
        "zero_a"  :"N",
        "zero_b"  :"N",
        "one_a"   :"N",
        "one_b"   :"N",
        "two_a"   :"N",
        "two_b"   :"N",
        "three_a" :"N",
        "three_b" :"N",
        "four_a"  :"N",
        "four_b"  :"N",
        "five_a"  :"Y",
        "five_b"  :"Y",
        "six_a"   :"Y",
        "six_b"   :"Y",
        "seven_a" :"Y",
        "seven_b" :"Y",
        "eight_a" :"Y",
        "eight_b" :"Y",
        "nine_a"  :"N",
        "native"  :"Naturalized",
        "kingdom" :"Plantae",
        "family"  :"Simaroubaceae",
        "genus"   :"Ailanthus",
        "order"   :"Sapindales",
        "clade"   :"Angiosperms",
        "edible"  :"No",
        "iucn"    :"-",
    }
