import fastapi

router = fastapi.APIRouter(prefix="/healthcheck", tags=["healthcheck"])


@router.get("/")
async def healthcheck(): 
    return {"message": "alive"}