from fastapi import APIRouter

from app.models.user_profile import UserProfile

from app.services.eligibility_service import EligibilityService
from app.services.recommendation_service import RecommendationService


router = APIRouter()

eligibility_service = EligibilityService()

recommendation_service = RecommendationService()


@router.post("/")
def get_recommendations(user: UserProfile):

    # First find schemes for which
    # the user is actually eligible.
    eligible_schemes = eligibility_service.check_eligibility(user)

    # Then rank those schemes
    # according to relevance.
    recommendations = recommendation_service.recommend(
        eligible_schemes,
        user
    )

    return {

        "success": True,

        "eligible_scheme_count": len(eligible_schemes),

        "recommendation_count": len(recommendations),

        "recommendations": recommendations

    }