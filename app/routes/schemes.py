from fastapi import APIRouter

from app.services.scheme_service import (
    get_all_schemes,
    get_scheme_by_id,
    search_schemes,
    get_schemes_by_category,
    get_schemes_by_ministry
)

router = APIRouter()


@router.get("/")
def fetch_all_schemes():

    return get_all_schemes()


@router.get("/search")
def search(keyword: str):

    return search_schemes(keyword)


@router.get("/category/{category}")
def category(category: str):

    return get_schemes_by_category(category)


@router.get("/ministry/{ministry}")
def ministry(ministry: str):

    return get_schemes_by_ministry(ministry)


@router.get("/{scheme_id}")
def fetch_scheme(scheme_id: int):

    return get_scheme_by_id(scheme_id)