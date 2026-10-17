from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Employee(BaseModel):
    id: int
    name: str
    designation: str


employees = []


@app.get("/employees")
def getEmployees():
    return {"employees": employees}


@app.post("/employees")
def createEmployee(employee: Employee):
    employees.append(employee)
    return {"message": "Employee added successfully"}


@app.put("/employees/{id}")
def updateEmployee(id: int, data: Employee, filter: bool = False):
    for index, emp in enumerate(employees):
        if emp.id == id:
            employees[index] = data
            return {
                "message": "Employee updated successfully",
                "employee": data,
                "filter": filter,
            }
    return {"message": "Employee not found"}
