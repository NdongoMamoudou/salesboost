from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routers.recommender import router as recommender_router

app = FastAPI(
    title="SalesBoost API - Recommendation Engine",
    version="1.0"
)

# ✅ Autoriser le frontend (React) à faire des appels API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # En DEV : on autorise tout ✅
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routes
app.include_router(recommender_router)

@app.get("/")
def root():
    return {"status": "API running ✅"}
