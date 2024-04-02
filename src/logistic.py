from fastapi import APIRouter
from pydantic import BaseModel
import pandas as pd
import joblib

#load the model&encoder
logistic_model = joblib.load('models\logistic_pipeline.joblib')
encoder = joblib.load('models\LabelEncoder.joblib')

class sepssis(BaseModel):
      PRG:int
      PL:int
      PR:int
      SK:int
      TS:int
      M11:float
      BD2:float
      Age:int

# a router for the logistic endpoint
router = APIRouter(
    prefix="/logistic",
    tags=["Logistic Regression Model"]
)
@router.post("/prediction")
async def logistic_predict(col:sepssis):
          
          cols = ["PRG","PL","PR","SK","TS","M11","BD2","Age"]
          
          df = pd.DataFrame([list(col.dict().values())], columns=cols)

          # make prediction
          pred_proba = logistic_model.predict_proba(df)

          pred = logistic_model.predict(df)
          
          pred = encoder.inverse_transform(pred)

          prob = pred_proba.max()*100

          prob = "{:.1f}%".format(prob) 

          return {"prediction":pred[0],"probability":prob}
