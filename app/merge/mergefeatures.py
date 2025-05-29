from app.db.postgressql import fetch_structured_features
from app.db.mongodb import fetch_unstructured_features

def get_applicant_features(applicant_id):
    structured = fetch_structured_features(applicant_id)
    unstructured = fetch_unstructured_features(applicant_id)
    return {**structured, **unstructured}
