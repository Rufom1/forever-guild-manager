import logging
from typing import Annotated, Literal

from fastapi import Depends, FastAPI, Response, status
from pydantic import BaseModel
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from app.db.session import get_db

logger = logging.getLogger(__name__)

app = FastAPI(title="Guild Platform API", version="0.1.0")


class ServiceStatus(BaseModel):
    status: Literal["ok", "not_ready"]
    service: str


@app.get("/health", response_model=ServiceStatus)
def health() -> ServiceStatus:
    return ServiceStatus(status="ok", service="guild-api")


@app.get(
    "/ready",
    response_model=ServiceStatus,
    responses={503: {"model": ServiceStatus}},
)
def ready(
    response: Response,
    db: Annotated[Session, Depends(get_db)],
) -> ServiceStatus:
    try:
        db.execute(text("SELECT 1"))
    except SQLAlchemyError:
        logger.exception("Database readiness check failed")
        response.status_code = status.HTTP_503_SERVICE_UNAVAILABLE
        return ServiceStatus(status="not_ready", service="guild-api")

    return ServiceStatus(status="ok", service="guild-api")