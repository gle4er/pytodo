from fastapi import FastAPI
from starlette.requests import Request

from core.db.session import SessionLocal
from views.v1.tasks import task_router
from views.v1.users import user_router


app = FastAPI(
    docs_url="/api/docs",
    openapi_url="/api",
)


@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    request.state.db = SessionLocal()
    response = await call_next(request)
    request.state.db.close()
    return response


@app.get("/api/v1")
async def root():
    return {"message": "ping"}


app.include_router(
    user_router,
    prefix="/api/v1",
    tags=["users"],
)
app.include_router(
    task_router,
    prefix="/api/v1",
    tags=["tasks"],
)
