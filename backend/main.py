from fastapi import FastAPI
from pydantic import BaseModel
from backend.database import init_db
from backend.experiment_logic import assign_driver_to_group
from backend.analysis import get_experiment_metrics

app = FastAPI()

class DriverAssignment(BaseModel):
    driver_id: int
    experiment_id: int

@app.on_event("startup")
def startup():
    init_db()

@app.post("/assign")
def assign_driver(data: DriverAssignment):
    group = assign_driver_to_group(data.driver_id, data.experiment_id)
    return {"driver_id": data.driver_id, "group": group}

@app.get("/metrics/{experiment_id}")
def metrics(experiment_id: int):from fastapi import FastAPI
from pydantic import BaseModel
from backend.database import init_db
from backend.experiment_logic import assign_driver_to_group
from backend.analysis import get_experiment_metrics

app = FastAPI()

class DriverAssignment(BaseModel):
    driver_id: int
    experiment_id: int

@app.on_event("startup")
def startup():
    init_db()

@app.get("/")
def root():
    return {"message": "Driver Payout Optimization Framework API is running."}

@app.post("/assign")
def assign_driver(data: DriverAssignment):
    group = assign_driver_to_group(data.driver_id, data.experiment_id)
    return {"driver_id": data.driver_id, "group": group}

@app.get("/metrics/{experiment_id}")
def metrics(experiment_id: int):
    return get_experiment_metrics(experiment_id)

    
