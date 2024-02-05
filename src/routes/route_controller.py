# Routes APIs and its endpoints

from fastapi import APIRouter
from src.endpoints.content_endpoint import word_frequency_analysis, search_history

wiki_api_routes = APIRouter()
wiki_api_routes.add_api_route("/word-frequency-analysis", word_frequency_analysis, methods=["POST"])
wiki_api_routes.add_api_route("/search-history", search_history, methods=["POST"])

