from fastapi import APIRouter

from app.models.user_profile import UserProfile
from app.services.eligibility_service import EligibilityService


router = APIRouter()

eligibility_service = EligibilityService()


@router.post("/check")
def eligibility(user: UserProfile):

    schemes = eligibility_service.check_eligibility(user)

    return {
        "success": True,
        "eligible_scheme_count": len(schemes),
        "schemes": schemes
    }