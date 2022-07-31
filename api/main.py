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
        "Species" :"A. altissima"
    }

@app.get("/APBRC")
def get_user():
    return {
        "eng_name":"Alaska paper birch",
        "sci_name":"Betula neoalaskana Betula",
        "oth_name":"Alaska white birch",
        "type"    :"Deciduous",
        "zero_a"  :"Y",
        "zero_b"  :"Y",
        "one_a"   :"Y",
        "one_b"   :"Y",
        "two_a"   :"Y",
        "two_b"   :"Y",
        "three_a" :"N",
        "three_b" :"N",
        "four_a"  :"N",
        "four_b"  :"N",
        "five_a"  :"N",
        "five_b"  :"N",
        "six_a"   :"N",
        "six_b"   :"N",
        "seven_a" :"N",
        "seven_b" :"N",
        "eight_a" :"N",
        "eight_b" :"N",
        "nine_a"  :"N",
        "native"  :"Native",
        "kingdom" :"Plantae",
        "family"  :"Betulaceae",
        "genus"   :"Betula",
        "order"   :"Sapindales",
        "clade"   :"Angiosperms",
        "edible"  :"No",
        "iucn"    :"-",
        "Species" :"B. neoalaskana"
    }

@app.get("/ALLDW")
def get_user():
    return {
        "eng_name":"Alternate-leaf dogwood",
        "sci_name":"Cornus alternifolia",
        "oth_name":"Pagoda dogwood",
        "type"    :"Deciduous",
        "zero_a"  :"N",
        "zero_b"  :"N",
        "one_a"   :"N",
        "one_b"   :"N",
        "two_a"   :"N",
        "two_b"   :"N",
        "three_a" :"N",
        "three_b" :"N",
        "four_a"  :"Y",
        "four_b"  :"Y",
        "five_a"  :"Y",
        "five_b"  :"Y",
        "six_a"   :"Y",
        "six_b"   :"Y",
        "seven_a" :"Y",
        "seven_b" :"Y",
        "eight_a" :"Y",
        "eight_b" :"Y",
        "nine_a"  :"N",
        "native"  :"Native",
        "kingdom" :"Plantae",
        "family"  :"Cornaceae",
        "genus"   :"Cornus",
        "order"   :"Cornales",
        "clade"   :"Asterids",
        "edible"  :"No",
        "iucn"    :"LC",
        "Species" :"C. alternifolia"
    }

@app.get("/AMBCH")
def get_user():
    return {
        "eng_name":"American beech",
        "sci_name":"Fagus grandifolia",
        "oth_name":"-",
        "type"    :"Deciduous",
        "zero_a"  :"N",
        "zero_b"  :"N",
        "one_a"   :"N",
        "one_b"   :"N",
        "two_a"   :"N",
        "two_b"   :"N",
        "three_a" :"Y",
        "three_b" :"Y",
        "four_a"  :"Y",
        "four_b"  :"Y",
        "five_a"  :"Y",
        "five_b"  :"Y",
        "six_a"   :"Y",
        "six_b"   :"Y",
        "seven_a" :"Y",
        "seven_b" :"Y",
        "eight_a" :"Y",
        "eight_b" :"Y",
        "nine_a"  :"Y",
        "native"  :"Native",
        "kingdom" :"Plantae",
        "family"  :"Fagaceae",
        "genus"   :"Fagus",
        "order"   :"Fagales",
        "clade"   :"Rosids",
        "edible"  :"No",
        "iucn"    :"LC",
        "Species" :"F. grandifolia"
    }

@app.get("/AMCNT")
def get_user():
    return {
        "eng_name":"American chestnut",
        "sci_name":"Castanea dentata",
        "oth_name":"-",
        "type"    :"Deciduous",
        "zero_a"  :"N",
        "zero_b"  :"N",
        "one_a"   :"N",
        "one_b"   :"N",
        "two_a"   :"N",
        "two_b"   :"N",
        "three_a" :"N",
        "three_b" :"N",
        "four_a"  :"Y",
        "four_b"  :"Y",
        "five_a"  :"Y",
        "five_b"  :"Y",
        "six_a"   :"Y",
        "six_b"   :"Y",
        "seven_a" :"Y",
        "seven_b" :"Y",
        "eight_a" :"Y",
        "eight_b" :"Y",
        "nine_a"  :"N",
        "native"  :"Native",
        "kingdom" :"Plantae",
        "family"  :"Fagaceae",
        "genus"   :"Fagus",
        "order"   :"Fagales",
        "clade"   :"Rosids",
        "edible"  :"Yes",
        "iucn"    :"CR",
        "Species" :"C. dentata"
    }

@app.get("/AMELD")
def get_user():
    return {
        "eng_name":"American elder",
        "sci_name":"Sambucus canadensis",
        "oth_name":"-",
        "type"    :"Deciduous",
        "zero_a"  :"N",
        "zero_b"  :"N",
        "one_a"   :"N",
        "one_b"   :"N",
        "two_a"   :"N",
        "two_b"   :"N",
        "three_a" :"Y",
        "three_b" :"Y",
        "four_a"  :"Y",
        "four_b"  :"Y",
        "five_a"  :"Y",
        "five_b"  :"Y",
        "six_a"   :"Y",
        "six_b"   :"Y",
        "seven_a" :"Y",
        "seven_b" :"Y",
        "eight_a" :"N",
        "eight_b" :"N",
        "nine_a"  :"N",
        "native"  :"Native",
        "kingdom" :"Plantae",
        "family"  :"Adoxaceae",
        "genus"   :"Sambucus",
        "order"   :"Dipsacales",
        "clade"   :"Asterids",
        "edible"  :"Yes",
        "NatureServe":"T5",
        "Species" :"S. canadensis"
    }

@app.get("/AMHZL")
def get_user():
    return {
        "eng_name":"American hazel",
        "sci_name":"Corylus americana",
        "oth_name":"-",
        "type"    :"Deciduous",
        "zero_a"  :"N",
        "zero_b"  :"N",
        "one_a"   :"N",
        "one_b"   :"N",
        "two_a"   :"N",
        "two_b"   :"N",
        "three_a" :"N",
        "three_b" :"N",
        "four_a"  :"Y",
        "four_b"  :"Y",
        "five_a"  :"Y",
        "five_b"  :"Y",
        "six_a"   :"Y",
        "six_b"   :"Y",
        "seven_a" :"Y",
        "seven_b" :"Y",
        "eight_a" :"Y",
        "eight_b" :"Y",
        "nine_a"  :"Y",
        "native"  :"Native",
        "kingdom" :"Plantae",
        "family"  :"Betulaceae",
        "genus"   :"Corylus",
        "order"   :"Fagales",
        "clade"   :"Rosids",
        "edible"  :"Yes",
        "iucn":"LC",
        "Species" :"C. americana"
    }

@app.get("/AMHLY")
def get_user():
    return {
        "eng_name":"American holly",
        "sci_name":"Ilex opaca",
        "oth_name":"-",
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
        "nine_a"  :"Y",
        "native"  :"Introduced",
        "kingdom" :"Plantae",
        "family"  :"Aquifoliaceae",
        "genus"   :"Ilex",
        "order"   :"Aquifoliales",
        "clade"   :"Asterids",
        "edible"  :"No",
        "iucn":"LC",
        "Species" :"I. opaca"
    }

@app.get("/AMMNA")
def get_user():
    return {
        "eng_name":"American mountain-ash",
        "sci_name":"Sorbus americana",
        "oth_name":"-",
        "type"    :"Deciduous",
        "zero_a"  :"N",
        "zero_b"  :"N",
        "one_a"   :"N",
        "one_b"   :"N",
        "two_a"   :"Y",
        "two_b"   :"Y",
        "three_a" :"Y",
        "three_b" :"Y",
        "four_a"  :"Y",
        "four_b"  :"Y",
        "five_a"  :"Y",
        "five_b"  :"Y",
        "six_a"   :"Y",
        "six_b"   :"Y",
        "seven_a" :"N",
        "seven_b" :"N",
        "eight_a" :"N",
        "eight_b" :"N",
        "nine_a"  :"N",
        "native"  :"Native",
        "kingdom" :"Plantae",
        "family"  :"Rosaceae",
        "genus"   :"Sorbus",
        "order"   :"Rosales",
        "clade"   :"Rosids",
        "edible"  :"No",
        "iucn":"LC",
        "Species" :"S. americana"
    }

@app.get("/AMPLM")
def get_user():
    return {
        "eng_name":"American plum",
        "sci_name":"Prunus americana",
        "oth_name":"Wild plum",
        "type"    :"Deciduous",
        "zero_a"  :"N",
        "zero_b"  :"N",
        "one_a"   :"N",
        "one_b"   :"N",
        "two_a"   :"N",
        "two_b"   :"N",
        "three_a" :"Y",
        "three_b" :"Y",
        "four_a"  :"Y",
        "four_b"  :"Y",
        "five_a"  :"Y",
        "five_b"  :"Y",
        "six_a"   :"Y",
        "six_b"   :"Y",
        "seven_a" :"Y",
        "seven_b" :"Y",
        "eight_a" :"Y",
        "eight_b" :"Y",
        "nine_a"  :"N",
        "native"  :"Native",
        "kingdom" :"Plantae",
        "family"  :"Rosaceae",
        "genus"   :"Prunus",
        "order"   :"Rosales",
        "clade"   :"Rosids",
        "edible"  :"Yes",
        "iucn":"LC",
        "Species" :"P. americana"
    }

@app.get("/AMCRY")
def get_user():
    return {
        "eng_name":"Amur choke cherry",
        "sci_name":"Prunus maackii",
        "oth_name":"-",
        "type"    :"Deciduous",
        "zero_a"  :"N",
        "zero_b"  :"N",
        "one_a"   :"N",
        "one_b"   :"N",
        "two_a"   :"N",
        "two_b"   :"N",
        "three_a" :"Y",
        "three_b" :"Y",
        "four_a"  :"Y",
        "four_b"  :"Y",
        "five_a"  :"Y",
        "five_b"  :"Y",
        "six_a"   :"Y",
        "six_b"   :"Y",
        "seven_a" :"N",
        "seven_b" :"N",
        "eight_a" :"N",
        "eight_b" :"N",
        "nine_a"  :"N",
        "native"  :"Introduced",
        "kingdom" :"Plantae",
        "family"  :"Rosaceae",
        "genus"   :"Prunus",
        "order"   :"Rosales",
        "clade"   :"Rosids",
        "edible"  :"Yes",
        "iucn":"-",
        "Species" :"P. maackii"
    }

@app.get("/AMCTR")
def get_user():
    return {
        "eng_name":"Amur corktree",
        "sci_name":"Phellodendron amurense",
        "oth_name":"-",
        "type"    :"Deciduous",
        "zero_a"  :"N",
        "zero_b"  :"N",
        "one_a"   :"N",
        "one_b"   :"N",
        "two_a"   :"N",
        "two_b"   :"N",
        "three_a" :"Y",
        "three_b" :"Y",
        "four_a"  :"Y",
        "four_b"  :"Y",
        "five_a"  :"Y",
        "five_b"  :"Y",
        "six_a"   :"Y",
        "six_b"   :"Y",
        "seven_a" :"Y",
        "seven_b" :"Y",
        "eight_a" :"Y",
        "eight_b" :"Y",
        "nine_a"  :"N",
        "native"  :"Introduced",
        "kingdom" :"Plantae",
        "family"  :"Rutaceae",
        "genus"   :"Phellodendron",
        "order"   :"Sapindales",
        "clade"   :"Rosids",
        "edible"  :"No",
        "iucn":"-",
        "Species" :"P. amurense"
    }

@app.get("/AMRML")
def get_user():
    return {
        "eng_name":"Amur maple",
        "sci_name":"Acer ginnala",
        "oth_name":"-",
        "type"    :"Deciduous",
        "zero_a"  :"N",
        "zero_b"  :"N",
        "one_a"   :"N",
        "one_b"   :"N",
        "two_a"   :"N",
        "two_b"   :"N",
        "three_a" :"Y",
        "three_b" :"Y",
        "four_a"  :"Y",
        "four_b"  :"Y",
        "five_a"  :"Y",
        "five_b"  :"Y",
        "six_a"   :"Y",
        "six_b"   :"Y",
        "seven_a" :"Y",
        "seven_b" :"Y",
        "eight_a" :"Y",
        "eight_b" :"Y",
        "nine_a"  :"N",
        "native"  :"Introduced",
        "kingdom" :"Plantae",
        "family"  :"Sapindaceae",
        "genus"   :"Acer",
        "order"   :"Sapindales",
        "clade"   :"Rosids",
        "edible"  :"No",
        "iucn":"-",
        "Species" :"A. ginnala"
    }

@app.get("/ARBTS")
def get_user():
    return {
        "eng_name":"Arbutus",
        "sci_name":"Arbutus menziesii",
        "oth_name":"-",
        "type"    :"Conifer",
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
        "five_a"  :"N",
        "five_b"  :"N",
        "six_a"   :"Y",
        "six_b"   :"Y",
        "seven_a" :"Y",
        "seven_b" :"Y",
        "eight_a" :"Y",
        "eight_b" :"Y",
        "nine_a"  :"N",
        "native"  :"Native",
        "kingdom" :"Plantae",
        "family"  :"Ericaceae",
        "genus"   :"Arbutus",
        "order"   :"Ericales",
        "clade"   :"Asterids",
        "edible"  :"Yes",
        "iucn":"LC",
        "Species" :"A. menziesii"
    }

@app.get("/ATCDR")
def get_user():
    return {
        "eng_name":"Atlas cedar",
        "sci_name":"Cedrus atlantica",
        "oth_name":"-",
        "type"    :"Conifer",
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
        "five_a"  :"N",
        "five_b"  :"N",
        "six_a"   :"Y",
        "six_b"   :"Y",
        "seven_a" :"Y",
        "seven_b" :"Y",
        "eight_a" :"Y",
        "eight_b" :"Y",
        "nine_a"  :"Y",
        "native"  :"Introduced",
        "kingdom" :"Plantae",
        "family"  :"Pinaceae",
        "genus"   :"Cedrus",
        "order"   :"Pinales",
        "clade"   :"Tracheophytes",
        "edible"  :"No",
        "iucn":"EN",
        "Species" :"C. atlantica"
    }

@app.get("/BDCPS")
def get_user():
    return {
        "eng_name":"Bald-cypress",
        "sci_name":"Taxodium distichum",
        "oth_name":"-",
        "type"    :"Conifer",
        "zero_a"  :"N",
        "zero_b"  :"N",
        "one_a"   :"N",
        "one_b"   :"N",
        "two_a"   :"N",
        "two_b"   :"N",
        "three_a" :"N",
        "three_b" :"N",
        "four_a"  :"Y",
        "four_b"  :"Y",
        "five_a"  :"Y",
        "five_b"  :"Y",
        "six_a"   :"N",
        "six_b"   :"N",
        "seven_a" :"N",
        "seven_b" :"N",
        "eight_a" :"N",
        "eight_b" :"N",
        "nine_a"  :"N",
        "native"  :"Introduced",
        "kingdom" :"Plantae",
        "family"  :"Cupressaceae",
        "genus"   :"Taxodium",
        "order"   :"Pinales",
        "clade"   :"Tracheophytes",
        "edible"  :"No",
        "iucn":"LC",
        "Species" :"T. distichum"
    }

@app.get("/AUTPN")
def get_user():
    return {
        "eng_name":"Austrian pine",
        "sci_name":"Pinus nigra",
        "oth_name":"-",
        "type"    :"Conifer",
        "zero_a"  :"N",
        "zero_b"  :"N",
        "one_a"   :"N",
        "one_b"   :"N",
        "two_a"   :"N",
        "two_b"   :"N",
        "three_a" :"N",
        "three_b" :"N",
        "four_a"  :"Y",
        "four_b"  :"Y",
        "five_a"  :"Y",
        "five_b"  :"Y",
        "six_a"   :"Y",
        "six_b"   :"Y",
        "seven_a" :"Y",
        "seven_b" :"Y",
        "eight_a" :"N",
        "eight_b" :"N",
        "nine_a"  :"N",
        "native"  :"Introduced",
        "kingdom" :"Plantae",
        "family"  :"Pinaceae",
        "genus"   :"Cedrus",
        "order"   :"Pinus",
        "clade"   :"Tracheophytes",
        "edible"  :"No",
        "iucn":"LC",
        "Species" :"P. nigra"
    }

@app.get("/BSMFR")
def get_user():
    return {
        "eng_name":"Balsam fir",
        "sci_name":"Abies balsamea",
        "oth_name":"-",
        "type"    :"Conifer",
        "zero_a"  :"N",
        "zero_b"  :"N",
        "one_a"   :"Y",
        "one_b"   :"Y",
        "two_a"   :"Y",
        "two_b"   :"Y",
        "three_a" :"Y",
        "three_b" :"Y",
        "four_a"  :"Y",
        "four_b"  :"Y",
        "five_a"  :"Y",
        "five_b"  :"Y",
        "six_a"   :"Y",
        "six_b"   :"Y",
        "seven_a" :"N",
        "seven_b" :"N",
        "eight_a" :"N",
        "eight_b" :"N",
        "nine_a"  :"N",
        "native"  :"Introduced",
        "kingdom" :"Plantae",
        "family"  :"Pinaceae",
        "genus"   :"Abies",
        "order"   :"Pinales",
        "clade"   :"Tracheophytes",
        "edible"  :"No",
        "iucn":"LC",
        "Species" :"A. balsamea"
    }

@app.get("/BSMPR")
def get_user():
    return {
        "eng_name":"Balsam Poplar",
        "sci_name":"Populus balsamifera",
        "oth_name":"Eastern balsam poplar",
        "type"    :"Deciduous",
        "zero_a"  :"Y",
        "zero_b"  :"Y",
        "one_a"   :"Y",
        "one_b"   :"Y",
        "two_a"   :"Y",
        "two_b"   :"Y",
        "three_a" :"Y",
        "three_b" :"Y",
        "four_a"  :"Y",
        "four_b"  :"Y",
        "five_a"  :"Y",
        "five_b"  :"Y",
        "six_a"   :"Y",
        "six_b"   :"Y",
        "seven_a" :"Y",
        "seven_b" :"Y",
        "eight_a" :"Y",
        "eight_b" :"Y",
        "nine_a"  :"N",
        "native"  :"Native",
        "kingdom" :"Plantae",
        "family"  :"Salicaceae",
        "genus"   :"Populus",
        "order"   :"Malpighiales",
        "clade"   :"Tracheophytes",
        "edible"  :"No",
        "iucn":"-",
        "Species" :"P. balsamifera"
    }

@app.get("/BSTWW")
def get_user():
    return {
        "eng_name":"Basket willow",
        "sci_name":"Salix viminalis",
        "oth_name":"-",
        "type"    :"Deciduous",
        "zero_a"  :"N",
        "zero_b"  :"N",
        "one_a"   :"N",
        "one_b"   :"N",
        "two_a"   :"N",
        "two_b"   :"N",
        "three_a" :"Y",
        "three_b" :"Y",
        "four_a"  :"N",
        "four_b"  :"N",
        "five_a"  :"N",
        "five_b"  :"N",
        "six_a"   :"N",
        "six_b"   :"N",
        "seven_a" :"N",
        "seven_b" :"N",
        "eight_a" :"N",
        "eight_b" :"N",
        "nine_a"  :"N",
        "native"  :"Naturalized",
        "kingdom" :"Plantae",
        "family"  :"Salicaceae",
        "genus"   :"Salix",
        "order"   :"Malpighiales",
        "clade"   :"Tracheophytes",
        "edible"  :"No",
        "iucn":"LC",
        "Species" :"S. viminalis"
    }

@app.get("/BASWD")
def get_user():
    return {
        "eng_name":"Basswood",
        "sci_name":"Tilia americana",
        "oth_name":"American linden",
        "type"    :"Deciduous",
        "zero_a"  :"Y",
        "zero_b"  :"Y",
        "one_a"   :"Y",
        "one_b"   :"Y",
        "two_a"   :"Y",
        "two_b"   :"Y",
        "three_a" :"Y",
        "three_b" :"Y",
        "four_a"  :"Y",
        "four_b"  :"Y",
        "five_a"  :"Y",
        "five_b"  :"Y",
        "six_a"   :"Y",
        "six_b"   :"Y",
        "seven_a" :"Y",
        "seven_b" :"Y",
        "eight_a" :"N",
        "eight_b" :"N",
        "nine_a"  :"N",
        "native"  :"Naturalized",
        "kingdom" :"Plantae",
        "family"  :"Malvaceae",
        "genus"   :"Tilia",
        "order"   :"Malvales",
        "clade"   :"Tracheophytes",
        "edible"  :"No",
        "iucn":"LC",
        "Species" :"T. americana"
    }

@app.get("/BASWD")
def get_user():
    return {
        "eng_name":"Beaked hazel",
        "sci_name":"Corylus cornuta",
        "oth_name":"-",
        "type"    :"Deciduous",
        "zero_a"  :"N",
        "zero_b"  :"N",
        "one_a"   :"N",
        "one_b"   :"N",
        "two_a"   :"Y",
        "two_b"   :"Y",
        "three_a" :"N",
        "three_b" :"N",
        "four_a"  :"N",
        "four_b"  :"N",
        "five_a"  :"N",
        "five_b"  :"N",
        "six_a"   :"N",
        "six_b"   :"N",
        "seven_a" :"N",
        "seven_b" :"N",
        "eight_a" :"N",
        "eight_b" :"N",
        "nine_a"  :"N",
        "native"  :"Naturalized",
        "kingdom" :"Plantae",
        "family"  :"Betulaceae",
        "genus"   :"Corylus",
        "order"   :"Fagales",
        "clade"   :"Tracheophytes",
        "edible"  :"Yes",
        "iucn":"LC",
        "Species" :"C. cornuta"
    }

@app.get("/BBWLW")
def get_user():
    return {
        "eng_name":"Bebb willow",
        "sci_name":"Salix bebbiana",
        "oth_name":"Diamond willow",
        "type"    :"Deciduous",
        "zero_a"  :"Y",
        "zero_b"  :"Y",
        "one_a"   :"Y",
        "one_b"   :"Y",
        "two_a"   :"Y",
        "two_b"   :"Y",
        "three_a" :"Y",
        "three_b" :"Y",
        "four_a"  :"Y",
        "four_b"  :"Y",
        "five_a"  :"Y",
        "five_b"  :"Y",
        "six_a"   :"Y",
        "six_b"   :"Y",
        "seven_a" :"Y",
        "seven_b" :"Y",
        "eight_a" :"Y",
        "eight_b" :"Y",
        "nine_a"  :"Y",
        "native"  :"Native",
        "kingdom" :"Plantae",
        "family"  :"Salicaceae",
        "genus"   :"Salix",
        "order"   :"Malpighiales",
        "clade"   :"Tracheophytes",
        "edible"  :"No",
        "iucn":"-",
        "Species" :"S. bebbiana"
    }

@app.get("/BBOAK")
def get_user():
    return {
        "eng_name":"Bebb's Oak",
        "sci_name":"Quercus bebbiana",
        "oth_name":"-",
        "type"    :"Deciduous",
        "zero_a"  :"N",
        "zero_b"  :"N",
        "one_a"   :"N",
        "one_b"   :"N",
        "two_a"   :"N",
        "two_b"   :"N",
        "three_a" :"Y",
        "three_b" :"Y",
        "four_a"  :"Y",
        "four_b"  :"Y",
        "five_a"  :"Y",
        "five_b"  :"Y",
        "six_a"   :"Y",
        "six_b"   :"Y",
        "seven_a" :"Y",
        "seven_b" :"Y",
        "eight_a" :"Y",
        "eight_b" :"Y",
        "nine_a"  :"N",
        "native"  :"Native",
        "kingdom" :"Plantae",
        "family"  :"Fagaceae",
        "genus"   :"Quercus",
        "order"   :"Fagales",
        "clade"   :"Tracheophytes",
        "edible"  :"Yes",
        "iucn":"-",
        "Species" :"Q. × bebbiana"
    }

@app.get("/BLMPL")
def get_user():
    return {
        "eng_name":"Bigleaf maple",
        "sci_name":"Acer macrophyllum",
        "oth_name":"Broadleaf maple",
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
        "five_a"  :"N",
        "five_b"  :"N",
        "six_a"   :"Y",
        "six_b"   :"Y",
        "seven_a" :"Y",
        "seven_b" :"Y",
        "eight_a" :"Y",
        "eight_b" :"Y",
        "nine_a"  :"N",
        "native"  :"Native",
        "kingdom" :"Plantae",
        "family"  :"Sapindaceae",
        "genus"   :"Acer",
        "order"   :"Sapindales",
        "clade"   :"Tracheophytes",
        "edible"  :"Yes",
        "iucn":"LC",
        "Species" :"A. macrophyllum"
    }

@app.get("/BTHRY")
def get_user():
    return {
        "eng_name":"Bitternut hickory",
        "sci_name":"Carya cordiformis",
        "oth_name":"Swamp Hickory",
        "type"    :"Deciduous",
        "zero_a"  :"N",
        "zero_b"  :"N",
        "one_a"   :"N",
        "one_b"   :"N",
        "two_a"   :"N",
        "two_b"   :"N",
        "three_a" :"N",
        "three_b" :"N",
        "four_a"  :"Y",
        "four_b"  :"Y",
        "five_a"  :"Y",
        "five_b"  :"Y",
        "six_a"   :"Y",
        "six_b"   :"Y",
        "seven_a" :"Y",
        "seven_b" :"Y",
        "eight_a" :"N",
        "eight_b" :"N",
        "nine_a"  :"N",
        "native"  :"Native",
        "kingdom" :"Plantae",
        "family"  :"Juglandaceae",
        "genus"   :"Carya",
        "order"   :"Fagales",
        "clade"   :"Tracheophytes",
        "edible"  :"Yes",
        "iucn":"LC",
        "Species" :"C. cordiformis"
    }

@app.get("/BTRCY")
def get_user():
    return {
        "eng_name":"Bitter cherry",
        "sci_name":"Prunus emarginata",
        "oth_name":"-",
        "type"    :"Deciduous",
        "zero_a"  :"Y",
        "zero_b"  :"Y",
        "one_a"   :"Y",
        "one_b"   :"Y",
        "two_a"   :"Y",
        "two_b"   :"Y",
        "three_a" :"Y",
        "three_b" :"Y",
        "four_a"  :"Y",
        "four_b"  :"Y",
        "five_a"  :"Y",
        "five_b"  :"Y",
        "six_a"   :"Y",
        "six_b"   :"Y",
        "seven_a" :"Y",
        "seven_b" :"Y",
        "eight_a" :"Y",
        "eight_b" :"Y",
        "nine_a"  :"N",
        "native"  :"Native",
        "kingdom" :"Plantae",
        "family"  :"Rosaceae",
        "genus"   :"Prunus",
        "order"   :"Rosales",
        "clade"   :"Tracheophytes",
        "edible"  :"Yes",
        "iucn":"LC",
        "Species" :"P. emarginata"
    }

@app.get("/ACPLT")
def get_user():
    return {
        "Name"    :"Acer platanoides",
        "Eng_name":"Norway maple leaves",
        "dbh"     : "10-102",
        # Volume eqn
        "eqn"     : "0.001011 × dbhcm^1.533 × htm^0.657" #dbhm - diameeter at breast height in cm. htm- tree height in meters
    }

@app.get("/ACSCM")
def get_user():
    return {
        "Name"    :"Acer saccharinum",
        "Eng_name":"silver maple",
        "dbh"     : "13-125",
        # Volume eqn
        "eqn"     : "0.0002383 × dbhcm^1.998 × htm^0.596" #dbhm - diameeter at breast height in cm. htm- tree height in meters
    }

@app.get("/CL0LS")
def get_user():
    return {
        "Name"    :"Celtis occidentalis",
        "Eng_name":"Common hackberry",
        "dbh"     : "11-119",
        #Volume eqn
        "eqn"     : "0.0022451 × dbhcm^2.118 × htm^ to 0.447" #dbhm - diameeter at breast height in cm. htm- tree height in meters
    }

@app.get("/CRSLQ")
def get_user():
    return {
        "Name"    :"Ceratonia siliqua",
        "Eng_name":"carob",
        "dbh"     : "16-74",
        #Volume eqn
        "eqn"     : "0.0001368 × dbhcm^1.79584 × htm^0.92667" #dbhm - diameeter at breast height in cm. htm- tree height in meters
    }

@app.get("/CICRA")
def get_user():
    return {
        "Name"    :"Cinnamomum camphora",
        "Eng_name":"Camphor tree",
        "dbh"     : "13-69",
        "eqn"     : "0.0000807 × dbhcm^2.1348 × htm^0.63404" #dbhm - diameeter at breast height in cm. htm- tree height in meters
    }

@app.get("/CPMCA")
def get_user():
    return {
        "Name"    :"Cupressus macrocarpa",
        "Eng_name":"Monterey cypress",
        "dbh"     : "16-147",
        "eqn"     : "0.0000419 × dbhcm^2.2604 × htm^0.6301" #dbhm - diameeter at breast height in cm. htm- tree height in meters
    }

@app.get("/EUGLB")
def get_user():
    return {
        "Name"    :"Eucalyptus globulus",
        "Eng_name":"southern blue gum",
        "dbh"     : "116-130",
        "eqn"     : "0.0000318 × dbhcm^2.15182 × htm^0.83573" #dbhm - diameeter at breast height in cm. htm- tree height in meters
    }

@app.get("/get-item/{item_id}")
def get_item(item_id:int):
    return item_id*2

@app.get("/ACPLT_eqn/{dbhcm}/{htm}")
def get_item(dbhcm:int, htm:int):
    return 0.001011*(dbhcm**1.533)*(htm**0.657)

@app.get("/ACSCM_eqn/{dbhcm}/{htm}")
def get_item(dbhcm:int, htm:int):
    return 0.0002383*(dbhcm**1.998)*(htm**0.596)

@app.get("/CLOLS_eqn/{dbhcm}/{htm}")
def get_item(dbhcm:int, htm:int):
    return 0.0022451*(dbhcm**2.118)*(htm**0.447)

@app.get("/CRSLQ_eqn/{dbhcm}/{htm}")
def get_item(dbhcm:int, htm:int):
    return 0.0001368*(dbhcm**1.79584)*(htm**0.92667)

@app.get("/CICRA_eqn/{dbhcm}/{htm}")
def get_item(dbhcm:int, htm:int):
    return 0.0000807*(dbhcm**2.1348)*(htm**0.63404)

@app.get("/CPMCA_eqn/{dbhcm}/{htm}")
def get_item(dbhcm:int, htm:int):
    return 0.0000419*(dbhcm**2.2604)*(htm**0.6301)

@app.get("/EUGLB_eqn/{dbhcm}/{htm}")
def get_item(dbhcm:int, htm:int):
    return 0.0000318*(dbhcm**2.15182)*(htm**0.83573)
