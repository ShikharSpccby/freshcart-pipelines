
import os
import snowflake.connector
from dotenv import load_dotenv

load_dotenv(override=True)

config = {
    "account": os.getenv("SNOWFLAKE_ACCOUNT"),
    "user": os.getenv("SNOWFLAKE_USER"),
    "authenticator": "PROGRAMMATIC_ACCESS_TOKEN",
    "token": os.getenv("SNOWFLAKE_PASSWORD"),
    "warehouse": os.getenv("SNOWFLAKE_WAREHOUSE"),
    "database": os.getenv("SNOWFLAKE_DATABASE"),
    "schema": os.getenv("SNOWFLAKE_SCHEMA"),
}

role = os.getenv("SNOWFLAKE_ROLE")

missing = [key for key, value in config.items() if not value]

if missing:
    raise ValueError(f"Missing settings: {missing}")

if role:
    config["role"] = role

print("Connecting to Snowflake using PAT...")

conn = None

try:
    conn = snowflake.connector.connect(**config)

    cursor = conn.cursor()
    cursor.execute("""
        SELECT CURRENT_USER(), CURRENT_DATABASE(),
               CURRENT_SCHEMA(), CURRENT_WAREHOUSE(),
               CURRENT_ROLE()
    """)

    result = cursor.fetchone()

    print("\nConnection successful!")
    print("User:", result[0])
    print("Database:", result[1])
    print("Schema:", result[2])
    print("Warehouse:", result[3])
    print("Role:", result[4])

    cursor.close()

except Exception as e:
    print("\nConnection failed.")
    print("Error:", str(e))

finally:
    if conn is not None:
        conn.close()
