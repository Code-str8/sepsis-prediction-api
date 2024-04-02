from fastapi import FastAPI
from src.logistic import router as logistic_router
from src.svm import router as svm_router
from src.doc import router as doc_router

app = FastAPI()

# Include the routers 
app.include_router(doc_router)
app.include_router(logistic_router)
app.include_router(svm_router)
