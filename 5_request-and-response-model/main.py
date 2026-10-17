from fastapi import FastAPI
from pydantic import BaseModel

vik =FastAPI()

class Employee(BaseModel):
    id: int
    name:str
    address:str
    
class EmployeeResponse(BaseModel):
    id:int
    name:str
    
employees=[]

# Response Model   
@vik.get("/employees",response_model=EmployeeResponse)
def getEmployees():
    return {
        "id":1,
        "name":"Vikrant",
        "address":"Chandigarh"
    }

# Request Model
@vik.post("/employees")
def createEmployee(data:Employee):
    employees.append(data)
    return {
        "status":"Success",
        "message":"Employee added successfully",
        "data":data
    }