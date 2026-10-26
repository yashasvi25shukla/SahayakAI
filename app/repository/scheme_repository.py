# ==========================================
# SAHAYAKAI - MONGODB SCHEME REPOSITORY
# ==========================================

from app.database.db import schemes_collection


class SchemeRepository:

    # ==========================================
    # GET ALL SCHEMES
    # ==========================================

    def get_all(self):
        return list(
            schemes_collection.find(
                {},
                {"_id": 0}
            )
        )

    # ==========================================
    # SAME METHOD FOR COMPATIBILITY
    # ==========================================

    def get_all_schemes(self):
        return self.get_all()

    # ==========================================
    # GET SCHEME BY ID
    # ==========================================

    def get_scheme_by_id(self, scheme_id):

        return schemes_collection.find_one(
            {"id": scheme_id},
            {"_id": 0}
        )

    # ==========================================
    # SEARCH SCHEMES
    # ==========================================

    def search(self, keyword):

        keyword = keyword.lower()

        schemes = self.get_all()

        result = []

        for scheme in schemes:

            text = (
                str(scheme.get("scheme_name", "")) + " " +
                str(scheme.get("description", "")) + " " +
                str(scheme.get("ministry", "")) + " " +
                str(scheme.get("category", ""))
            ).lower()

            if keyword in text:
                result.append(scheme)

        return result

    # ==========================================
    # FILTER BY CATEGORY
    # ==========================================

    def filter_category(self, category):

        schemes = self.get_all()

        return [
            scheme
            for scheme in schemes
            if str(scheme.get("category", "")).lower()
            == category.lower()
        ]

    # ==========================================
    # FILTER BY MINISTRY
    # ==========================================

    def filter_ministry(self, ministry):

        schemes = self.get_all()

        return [
            scheme
            for scheme in schemes
            if str(scheme.get("ministry", "")).lower()
            == ministry.lower()
        ]