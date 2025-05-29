from pymongo import MongoClient
import os

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
client = MongoClient(MONGO_URI)
db = client["social_support"]

def fetch_unstructured_features(applicant_id):
    doc = db["credit_reports"].find_one({"applicant_id": applicant_id})
    if doc:
        return {
            "credit_score": doc.get("credit_score"),
            "liabilities": doc.get("liabilities", []),
            "remarks": doc.get("remarks", "")
        }
    return {}
