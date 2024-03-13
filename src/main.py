import fastapi
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

from src.api.endpoints import router as api_endpoint_router
from src.config.config_parser import Config

def initialize_backend_application() -> fastapi.FastAPI:
    app = fastapi.FastAPI()

    app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

    app.include_router(router=api_endpoint_router, prefix='/api')

    return app

cfg = Config()
backend_app: fastapi.FastAPI = initialize_backend_application()

if __name__ == "__main__":
    uvicorn.run(
        app="main:backend_app",
        host=cfg.config[cfg.env]["SERVER_HOST"],
        port=int(cfg.config[cfg.env]["SERVER_PORT"]),
        reload=cfg.config[cfg.env]["DEBUG"],
        workers=int(cfg.config[cfg.env]["SERVER_WORKERS"]),
        log_level=cfg.logging_level,
    )
