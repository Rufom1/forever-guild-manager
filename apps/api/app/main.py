from fastapi import FastAPI

app = FastAPI(title="Guild Platform API", version="0.1.0")


@app.get("/health")
def health():
    return {"status": "ok", "service": "guild-api"}

@app.get("/ready")
def ready():
    # Perform readiness checks here, e.g., database connection, external services, etc.
    # Setup for PostgreSQL connection check
    try:
        # Replace with actual database connection check
        # e.g., db.execute("SELECT 1")
        pass
    except Exception as e:
        return {"status": "not ready", "reason": str(e)}
