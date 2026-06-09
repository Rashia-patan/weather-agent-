from fastapi import FastAPI
from pydantic import BaseModel
from agent import create_asor

app = FastAPI()

@app.get("/")
def home():
    return {"message": "API is working"} 


class ASORRequest(BaseModel):
    employee_id: str
    request_type: str
    reason: str


@app.post("/asor")
def submit_asor(request: ASORRequest):

    payload = {
        "employeeId": request.employee_id,
        "requestType": request.request_type,
        "reason": request.reason
    }

    result = create_asor(payload)

    return {
        "message": "ASOR submitted",
        "workday_response": result
    }
