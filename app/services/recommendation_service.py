class RecommendationService:

    def calculate_score(self, scheme, user):

        rule = scheme.get("eligibility", {})

        score = 0
        reasons = []

        # ------------------------------------------------
        # BASE SCORE
        # ------------------------------------------------

        # The scheme has already passed the eligibility
        # engine, so it starts with a basic match score.
        score += 50

        reasons.append("You satisfy the basic eligibility requirements.")

        # ------------------------------------------------
        # OCCUPATION MATCH
        # ------------------------------------------------

        occupations = rule.get("occupation", ["Any"])

        if "Any" not in occupations:

            occupations_lower = [
                occupation.lower()
                for occupation in occupations
            ]

            if user.occupation.lower() in occupations_lower:

                score += 15

                reasons.append(
                    f"Your occupation ({user.occupation}) matches the scheme."
                )

        else:

            score += 5

        # ------------------------------------------------
        # GENDER MATCH
        # ------------------------------------------------

        gender = rule.get("gender", "Any")

        if gender != "Any":

            if user.gender.lower() == gender.lower():

                score += 10

                reasons.append(
                    f"The scheme specifically supports {gender} beneficiaries."
                )

        else:

            score += 5

        # ------------------------------------------------
        # STATE MATCH
        # ------------------------------------------------

        states = rule.get("state", ["All"])

        if "All" not in states:

            states_lower = [
                state.lower()
                for state in states
            ]

            if user.state.lower() in states_lower:

                score += 10

                reasons.append(
                    f"The scheme is available in {user.state}."
                )

        else:

            score += 5

        # ------------------------------------------------
        # INCOME MATCH
        # ------------------------------------------------

        income_limit = rule.get("annual_income_limit")

        if income_limit is not None:

            if user.annual_income <= income_limit:

                score += 5

                reasons.append(
                    "Your annual income is within the scheme limit."
                )

        # ------------------------------------------------
        # STUDENT MATCH
        # ------------------------------------------------

        if rule.get("student", False):

            if user.student:

                score += 5

                reasons.append(
                    "You are a student and the scheme targets students."
                )

        # ------------------------------------------------
        # FARMER MATCH
        # ------------------------------------------------

        if rule.get("farmer", False):

            if user.farmer:

                score += 5

                reasons.append(
                    "You are a farmer and the scheme targets farmers."
                )

        # ------------------------------------------------
        # DISABILITY MATCH
        # ------------------------------------------------

        if rule.get("disabled", False):

            if user.disabled:

                score += 5

                reasons.append(
                    "The scheme supports persons with disabilities."
                )

        # ------------------------------------------------
        # WIDOW MATCH
        # ------------------------------------------------

        if rule.get("widow", False):

            if user.widow:

                score += 5

                reasons.append(
                    "The scheme supports eligible widows."
                )

        # ------------------------------------------------
        # SENIOR CITIZEN MATCH
        # ------------------------------------------------

        if rule.get("senior_citizen", False):

            if user.senior_citizen:

                score += 5

                reasons.append(
                    "The scheme supports senior citizens."
                )

        # ------------------------------------------------
        # MAXIMUM SCORE
        # ------------------------------------------------

        score = min(score, 100)

        return {
            "score": score,
            "reasons": reasons
        }


    def recommend(self, schemes, user):

        recommendations = []

        for scheme in schemes:

            result = self.calculate_score(
                scheme,
                user
            )

            recommendations.append({

                "scheme": scheme,

                "match_score": result["score"],

                "reasons": result["reasons"]

            })

        # Highest score first
        recommendations.sort(
            key=lambda item: item["match_score"],
            reverse=True
        )

        return recommendations