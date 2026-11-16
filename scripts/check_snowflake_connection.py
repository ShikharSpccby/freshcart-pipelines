if __name__ == "__main__":
    # Place your connection test and validation check here
    if missing:
        raise ValueError(f"Missing settings: {missing}")
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
import os
import snowflake.connector
from dotenv import load_dotenv

load_dotenv()

if __name__ == "__main__":
    required_settings = ['account', 'user', 'token', 'warehouse', 'database', 'schema']
    
    settings = {
        'account': os.getenv("SNOWFLAKE_ACCOUNT"),
        'user': os.getenv("SNOWFLAKE_USER"),
        'token': os.getenv("SNOWFLAKE_TOKEN") or os.getenv("SNOWFLAKE_PASSWORD"),
        'warehouse': os.getenv("SNOWFLAKE_WAREHOUSE"),
        'database': os.getenv("SNOWFLAKE_DATABASE"),
        'schema': os.getenv("SNOWFLAKE_SCHEMA"),
    }
    
    missing = [k for k, v in settings.items() if not v]
    
    if missing:
        raise ValueError(f"Missing settings: {missing}")
        
    print("Connecting to Snowflake...")
    conn = snowflake.connector.connect(
        account=settings['account'],
        user=settings['user'],
        password=settings['token'],
        warehouse=settings['warehouse'],
        database=settings['database'],
        schema=settings['schema']
    )
    try:
        cur = conn.cursor()
        cur.execute("SELECT CURRENT_VERSION()")
        version = cur.fetchone()[0]
        print(f"Successfully connected to Snowflake! Version: {version}")
    finally:
        cur.close()
        conn.close()
