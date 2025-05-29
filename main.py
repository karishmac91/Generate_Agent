from fastapi import FastAPI, HTTPException,  UploadFile, File
from pathlib import Path
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from fastapi.responses import JSONResponse

from app.agents.pipeline import run_recommendation_pipeline



app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/recommend/{applicant_id}")
async def recommend_support(applicant_id: str):
    result = run_recommendation_pipeline(applicant_id)
    return {"status": "ok", "recommendation": result}



if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
