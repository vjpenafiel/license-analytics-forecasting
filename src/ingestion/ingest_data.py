import os
import time
from pathlib import Path
from tqdm import tqdm
import psycopg2

# 1. Database Connection Configuration
DB_CONFIG = {
    "dbname": "license_analytics",
    "user": "postgres",
    "password": "admin123",  
    "host": "localhost",
    "port": "5432"
}

# 2. File Path Resolution
BASE_DIR = Path(__file__).resolve().parent.parent.parent    # reach root folder of the project
RAW_DATA_DIR = BASE_DIR / "data" / "raw"                    # directory of raw csv files

# Ordered mapping of target PostgreSQL raw tables to source CSV files
TABLE_FILES = [
    ("raw.users", RAW_DATA_DIR / "users.csv"),
    ("raw.software_products", RAW_DATA_DIR / "software_products.csv"),
    ("raw.software_features", RAW_DATA_DIR / "software_features.csv"),
    ("raw.license_pools", RAW_DATA_DIR / "license_pools.csv"),
    ("raw.license_events", RAW_DATA_DIR / "license_events.csv"),
]

def ingest_raw_data():
    # Streams CSV data directly into raw PostgreSQL tables using the COPY protocol.
    start_time = time.time()    # start time tracking
    print("Starting raw data ingestion into PostgreSQL...\n")

    # Establish connection
    try:
        conn = psycopg2.connect(**DB_CONFIG)    # initialize connection
        cursor = conn.cursor()                  # initialize cursor for executing queries
    except Exception as e:
        print(f"Failed to connect to PostgreSQL: {e}")
        return

    # Perform ingestion
    try:
        for table_name, file_path in tqdm(TABLE_FILES, desc="Ingesting raw data"):
            if not file_path.exists():
                print(f"Skipping {table_name}: File not found at {file_path}")
                continue

            print(f"Loading {file_path.name} -> {table_name}...")

            # Clear raw table to ensure clean script execution
            cursor.execute(f"TRUNCATE TABLE {table_name} CASCADE;")

            # Copy stream using PostgreSQL COPY command
            with open(file_path, "r", encoding="utf-8") as f:
                copy_sql = f"""
                    COPY {table_name}
                    FROM STDIN
                    WITH (FORMAT csv, HEADER true, DELIMITER ',');
                """
                cursor.copy_expert(sql=copy_sql, file=f)

            # Validate ingested row count
            cursor.execute(f"SELECT COUNT(*) FROM {table_name};")
            row_count = cursor.fetchone()[0]    # fetch 1st row containing count
            print(f"  └─ Success: Loaded {row_count:,} rows.\n")

        # Commit all table insertions in a single transaction
        conn.commit()
        total_time = time.time() - start_time   # compute duration of ingestion
        print(f"Ingestion complete in {total_time:.2f} seconds!")

    # Rollback if error during ingestion
    except Exception as e:
        conn.rollback()
        print(f"\nError during ingestion! Rolled back transaction. Details: {e}")

    # Close connection
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    ingest_raw_data()