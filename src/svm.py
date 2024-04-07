from fastapi import APIRouter
from pydantic import BaseModel
import pandas as pd
import joblib

#load the model&encoder
svm_model = joblib.load('models/svm_pipeline.joblib')
encoder = joblib.load('models/LabelEncoder.joblib')

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
    prefix="/svm",
    tags=["Sector Vector Machine Model"]
)
@router.post("/prediction")
async def svm_predict(col:sepssis):
          
          cols = ["PRG","PL","PR","SK","TS","M11","BD2","Age"]
          
          df = pd.DataFrame([list(col.dict().values())], columns=cols)

          # make prediction
          pred_proba = svm_model.predict_proba(df)

          pred = svm_model.predict(df)
          
          pred = encoder.inverse_transform(pred)

          prob = pred_proba.max()*100

          prob = "{:.1f}%".format(prob) 

          return {"prediction":pred[0],"probability":prob}
