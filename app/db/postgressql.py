import os
from dotenv import load_dotenv
import psycopg2
from psycopg2.extras import RealDictCursor

load_dotenv()

# Get DB config from .env
PG_USER = os.getenv("PG_USER", "postgres")
PG_PASSWORD = os.getenv("PG_PASSWORD", "postgres")
PG_HOST = os.getenv("PG_HOST", "localhost")
PG_PORT = os.getenv("PG_PORT", "5432")
PG_DATABASE = os.getenv("PG_DATABASE", "postgres")

def fetch_structured_features(applicant_id):
    try:
        with psycopg2.connect(
            user=PG_USER,
            password=PG_PASSWORD,
            host=PG_HOST,
            port=PG_PORT,
            database=PG_DATABASE
        ) as conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute("""
                    SELECT income, family_size, asset_score, employment_status, region
                    FROM applicant_features
                    WHERE applicant_id = %s
                """, (applicant_id,))
                row = cur.fetchone()
                if row:
                    return dict(row)  # RealDictCursor already returns dict-like row
                return {}
    except Exception as e:
        print("Error fetching structured features:", e)
        return {}
