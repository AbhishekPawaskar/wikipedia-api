from fastapi import FastAPI
from starlette.routing import Mount

#only for debugging
import debugpy
debugpy.listen(("0.0.0.0", 5678))

from src.routes.route_controller import wiki_api_routes

app = FastAPI()
app.mount("/wiki-api", wiki_api_routes)