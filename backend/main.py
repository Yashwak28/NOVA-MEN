from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="NOVA MEN API", description="Backend for AI Marketing Automation")

class Campaign(BaseModel):
    name: str
    budget: float
    target_audience: str

@app.get("/")
def read_root():
    return {"message": "Welcome to NOVA MEN API"}

@app.post("/api/campaigns/")
def create_campaign(campaign: Campaign):
    return {"status": "success", "data": campaign}
