import joblib
import pandas as pd
from core.models import PredictionResponse

class Predictor:
    def __init__(self, model_path: str = "data/predictor.pkl"):
        self.model = joblib.load(model_path)
        self.teams = ["Arsenal", "Chelsea", "Liverpool"]  # Reemplaza con tus equipos

    def predict(self, home_team: str, away_team: str) -> PredictionResponse:
        # Validación
        if home_team not in self.teams or away_team not in self.teams:
            return PredictionResponse(
                prediction="invalid",
                probabilities={},
                success=False
            )

        # Preparar features (ejemplo)
        input_data = pd.DataFrame([[
            1.8,  # Home_Avg_Goals 
            1.2,  # Away_Avg_Goals
            15,   # HS
            8     # AS
        ]], columns=['Home_Avg_Goals', 'Away_Avg_Goals', 'HS', 'AS'])
        
        proba = self.model.predict_proba(input_data)[0]
        
        return PredictionResponse(
            prediction=["away", "draw", "home"][proba.argmax()],
            probabilities={
                "away": float(proba[0]),
                "draw": float(proba[1]),
                "home": float(proba[2])
            },
            success=True
        )
