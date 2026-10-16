from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Todos(BaseModel):
    id:int
    title: str
    status:bool
    
todos =[]
# Create Todo
@app.post("/todos")
def createTodos(todo:Todos):
    todos.append(todo)
    return {"message":"Todo created","Data":todo}

# Get Todos    
@app.get("/todos")
def getTodos():
    return {"Todos":todos}    

# Get Todo
@app.get("/todos/{id}")
def getTodo(id : int):
    for index,todo in enumerate(todos):
        if todo.id==id:
            return {"Todo":todo}
    return {"message":"Todo not found"}

# Update Todo
@app.put("/todos/{id}")
def updateTodo(id:int, data:Todos):
    for index,todo in enumerate(todos):
        if todo.id ==id:
            todos[index] =data
            return {"message": "Todo Updated"}
    return {"message":"Todo update failed"}


# Delete Todo
@app.delete("/todos/{id}")
def deleteTodo(id : int):
    for index, todo in enumerate(todos):
        if todo.id ==id:
            todos.pop(index)
            return {"message":"Record Deleted"}
    return {"message": "Error to delete Todo"}