import fastapi

from src.api.routes.summarize import router as summarize_router
from src.api.routes.healthcheck import router as healthcheck_routere
router = fastapi.APIRouter()

router.include_router(router=summarize_router)
router.include_router(router=healthcheck_routere)
