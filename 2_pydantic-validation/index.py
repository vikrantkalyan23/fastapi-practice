from fastapi import FastAPI

app = FastAPI()


@app.post("/createUser")
def createUser(user: dict):
    return {"User Info": user}


@app.post("/createUser1")
def createUser1(name: str, address: str):
    return {"Name": name, "Address": address}


