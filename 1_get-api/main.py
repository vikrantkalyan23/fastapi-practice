from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def home():
    return "Welcome to fastapi"


@app.get("/about")
def about():
    return {"message": "Welcome to About Page"}


@app.get("/product")
def product(name: str = "Laptop"):
    return {"Product Name": name}


@app.get("/detail/{id}")
def detail(id):
    return {"Product Id": id}


@app.get("/info/{name}/{price}")
def info(name: str, price: int):
    return {"Name": name, "Price": price}
