from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from app.services.ai_service import ask_gemini

router = APIRouter()


class ChatRequest(BaseModel):
    message: str = Field(..., min_length=1, max_length=1500)


@router.post("/")
def chat(request: ChatRequest):
    message = request.message.strip()

    if not message:
        raise HTTPException(
            status_code=400,
            detail="Message cannot be empty."
        )

    try:
        answer = ask_gemini(message)

        return {
            "success": True,
            "question": message,
            "answer": answer
        }

    except Exception as error:
        print("Gemini Error:", error)

        raise HTTPException(
            status_code=503,
            detail=str(error)
        )
