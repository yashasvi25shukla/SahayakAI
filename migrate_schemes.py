# ==========================================
# SAHAYAKAI - MIGRATE SCHEMES TO MONGODB
# ==========================================

import json
from pathlib import Path

from app.database.db import schemes_collection


# ==========================================
# SCHEMES JSON FILE
# ==========================================

json_path = (
    Path(__file__).resolve().parent
    / "data"
    / "schemes.json"
)


# ==========================================
# LOAD JSON DATA
# ==========================================

print("Reading schemes.json...")

with open(json_path, "r", encoding="utf-8") as file:
    schemes = json.load(file)


print(f"Found {len(schemes)} schemes in JSON.")


# ==========================================
# CLEAR OLD MONGODB DATA
# ==========================================

print("Clearing old schemes collection...")

schemes_collection.delete_many({})


# ==========================================
# INSERT SCHEMES
# ==========================================

if schemes:

    result = schemes_collection.insert_many(schemes)

    print(
        f"Successfully inserted {len(result.inserted_ids)} schemes into MongoDB."
    )

else:

    print("No schemes found in schemes.json.")


# ==========================================
# VERIFY
# ==========================================

count = schemes_collection.count_documents({})

print(f"MongoDB schemes count: {count}")

print("\nMigration completed successfully! ✅")