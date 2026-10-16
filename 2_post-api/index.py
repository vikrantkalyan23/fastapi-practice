from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User2(BaseModel):
    name :str
    address:str
    mobile:int

class Address(BaseModel):
    city:str
    pin:int
    country:str
class User3(BaseModel):
    name:str
    mobile:int
    address:Address

@app.post("/createUser")
def createUser(data: dict):
    return {"User Info": data}


@app.post("/createUser1")
def createUser1(name: str, address: str):
    return {"Name": name, "Address": address}


@app.post("/createUser2")
def createUser2(user:User2):
    return {"User Info ": user}

@app.post("/createUser3")
def createUser3(user:User3):
    return {"User Info": user}