import os
import sys
import yaml
import oracledb

def main():
    config_path = os.getenv("CONFIG_PATH", "/app/config.yaml")
    if not os.path.exists(config_path):
        print(f"Config file not found at: {config_path}")
        sys.exit(1)
        
    with open(config_path, "r") as f:
        try:
            config = yaml.safe_load(f)
        except Exception as e:
            print(f"Error parsing YAML: {e}")
            sys.exit(1)

    db_config = config.get("oracle_db", {})
    ip = db_config.get("ip")
    port = db_config.get("port", 1521)
    dbname = db_config.get("dbname")
    username = db_config.get("username")
    password = db_config.get("password")

    if not all([ip, dbname, username, password]):
        print("Missing required config fields (ip, dbname, username, password)")
        sys.exit(1)

    print(f"Attempting connection to {username}@{ip}:{port}/{dbname}...")
    try:
        connection = oracledb.connect(
            user=username,
            password=password,
            dsn=f"{ip}:{port}/{dbname}"
        )
        with connection.cursor() as cursor:
            cursor.execute("SELECT 'Connection Successful!' FROM dual")
            for row in cursor:
                print(row[0])
    except Exception as e:
        print(f"Database connection failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
