from pydantic import BaseModel

class PredictionRequest(BaseModel):
    home_team: str
    away_team: str

class PredictionResponse(BaseModel):
    prediction: str  # "home", "draw", "away"
    probabilities: dict
    success: bool
