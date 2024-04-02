from fastapi import APIRouter, Response
from typing import List
from pydantic import BaseModel

router = APIRouter()


@router.get("/", summary="Welcome", tags=["Documentation"])
async def root():
    """
    Hello! Try it out!
    """
    return Response(
        content="Welcome to Medical Sepsis API! Visit /docs to see the documentation on how to use this API.",
        media_type="text/plain"
    )


@router.get("/docs", summary=" API Documentation", tags=["Documentation"])
async def get_docs():
    """
    Documentation for the Medical Sepsis API.

    This API is designed to predict the risk of sepsis in medical patients based on various input features.
    
    The API expects the following columns as input: 

    - PRG (Plasma_glucose)
    - PL (Blood Work Result-1 (mu U/ml))
    - PR (Blood Pressure (mm Hg))
    - SK (Blood Work Result-2 (mm))
    - TS (Blood Work Result-3 (mu U/ml))
    - M11 (Body mass index (weight in kg/(height in m)^2)
    - BD2 (Blood Work Result-4 (mu U/ml))
    - Age (patients age (years))

    To use the API, send a POST request to the '/predict' endpoint with the required input data in the request body.
    The API will process the input and return a prediction indicating the risk of sepsis for the given patient.
    
    """
    return 

