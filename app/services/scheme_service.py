# ==========================================
# SAHAYAKAI - SCHEME SERVICE
# ==========================================

from app.repository.scheme_repository import SchemeRepository


repository = SchemeRepository()


# ==========================================
# GET ALL SCHEMES
# ==========================================

def get_all_schemes():
    return repository.get_all()


# ==========================================
# GET SCHEME BY ID
# ==========================================

def get_scheme_by_id(scheme_id):

    scheme = repository.get_scheme_by_id(scheme_id)

    if scheme is None:
        return None

    return scheme


# ==========================================
# SEARCH SCHEMES
# ==========================================

def search_schemes(keyword):

    return repository.search(keyword)


# ==========================================
# FILTER BY CATEGORY
# ==========================================

def get_schemes_by_category(category):

    return repository.filter_category(category)


# ==========================================
# FILTER BY MINISTRY
# ==========================================

def get_schemes_by_ministry(ministry):

    return repository.filter_ministry(ministry)