# ==========================================
# SAHAYAKAI - USER ROUTES
# ==========================================

from fastapi import APIRouter, HTTPException

from app.models.user_profile import UserProfile
from app.services.user_service import create_user


router = APIRouter()


# ==========================================
# CREATE USER PROFILE
# ==========================================

@router.post("/")
def create_user_profile(user: UserProfile):

    try:

        user_data = user.model_dump()

        user_id = create_user(user_data)

        return {
            "success": True,
            "message": "User profile saved successfully.",
            "user_id": user_id
        }

    except Exception as error:

        print("User creation error:", error)

        raise HTTPException(
            status_code=500,
            detail="Unable to save user profile."
        )