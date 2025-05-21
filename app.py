from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from core.predictor import Predictor
from core.models import PredictionRequest
from core.config import settings

app = FastAPI(title=settings.APP_NAME, version=settings.VERSION)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Cargar predictor
predictor = Predictor()

@app.post("/predict")
async def predict(request: PredictionRequest):
    return predictor.predict(request.home_team, request.away_team)

@app.get("/health")
async def health_check():
    return {"status": "healthy"}
