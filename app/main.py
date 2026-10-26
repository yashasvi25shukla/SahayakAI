
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import schemes, chat, user
from app.routes import eligibility
from app.routes import recommendation
from app.routes import upload

app = FastAPI(
    title="SahayakAI Backend",
    description="AI Powered Government Scheme Eligibility Assistant",
    version="1.0.0"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Home Route
@app.get("/")
def home():

    return {
        "status": "success",
        "message": "Welcome to SahayakAI Backend 🚀"
    }


# Scheme Routes
app.include_router(
    schemes.router,
    prefix="/schemes",
    tags=["Government Schemes"]
)


# Eligibility Routes
app.include_router(
    eligibility.router,
    prefix="/eligibility",
    tags=["Eligibility Engine"]
)
# Recommendation Routes

app.include_router(
    recommendation.router,
    prefix="/recommendations",
    tags=["Recommendation Engine"]
)
# document upload
app.include_router(
    upload.router,
    prefix="/upload",
    tags=["Document Upload"]
)
# AI Assistant Routes
app.include_router(
    chat.router,
    prefix="/chat",
    tags=["AI Assistant"]
)
app.include_router(
    user.router,
    prefix="/users",
    tags=["Users"]
)