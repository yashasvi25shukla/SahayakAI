from app.repository.scheme_repository import SchemeRepository


class EligibilityService:

    def __init__(self):
        self.repository = SchemeRepository()

    def check_eligibility(self, user):

        schemes = self.repository.get_all()

        print("NUMBER OF SCHEMES LOADED:", len(schemes))
        print("USER DATA:", user)

        eligible_schemes = []

        for scheme in schemes:

            rule = scheme.get("eligibility", {})

            # ---------------- AGE ----------------

            if user.age < rule.get("minimum_age", 0):
                continue

            if user.age > rule.get("maximum_age", 200):
                continue

            # ---------------- GENDER ----------------

            if rule.get("gender", "Any") != "Any":

                if user.gender.lower() != rule.get("gender", "Any").lower():
                    continue

            # ---------------- CITIZENSHIP ----------------

            if user.citizenship.lower() != rule.get("citizenship", "Indian").lower():
                continue

            # ---------------- OCCUPATION ----------------

            if "Any" not in rule.get("occupation", ["Any"]):

                occupation_list = [
                    occupation.lower()
                    for occupation in rule.get("occupation", ["Any"])
                ]

                if user.occupation.lower() not in occupation_list:
                    continue

            # ---------------- ANNUAL INCOME ----------------

            if rule.get("annual_income_limit") is not None:

                if user.annual_income > rule.get("annual_income_limit"):
                    continue

            # ---------------- BPL ----------------

            if rule.get("bpl_required", False):

                if not user.bpl:
                    continue

            # ---------------- STUDENT ----------------

            if rule.get("student", False):

                if not user.student:
                    continue

            # ---------------- FARMER ----------------

            if rule.get("farmer", False):

                if not user.farmer:
                    continue

            # ---------------- DISABLED ----------------

            if rule.get("disabled", False):

                if not user.disabled:
                    continue

            # ---------------- WIDOW ----------------

            if rule.get("widow", False):

                if not user.widow:
                    continue

            # ---------------- SENIOR CITIZEN ----------------

            if rule.get("senior_citizen", False):

                if not user.senior_citizen:
                    continue

            # ---------------- STATE ----------------

            if "All" not in rule.get("state", ["All"]):

                state_list = [
                    state.lower()
                    for state in rule.get("state", ["All"])
                ]

                if user.state.lower() not in state_list:
                    continue

            # ---------------- CASTE ----------------

            if "All" not in rule.get("caste", ["All"]):

                caste_list = [
                    caste.lower()
                    for caste in rule.get("caste", ["All"])
                ]

                if user.caste.lower() not in caste_list:
                    continue

            # ---------------- RELIGION ----------------

            if "All" not in rule.get("religion", ["All"]):

                religion_list = [
                    religion.lower()
                    for religion in rule.get("religion", ["All"])
                ]

                if user.religion.lower() not in religion_list:
                    continue

            eligible_schemes.append(scheme)

        return eligible_schemes