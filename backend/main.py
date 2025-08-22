from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from settings import config

api = FastAPI(root_path="/api") # Create the FastAPI application instance

api.add_middleware(
    CORSMiddleware,
    allow_origins=config.cors_allow_origins,
    allow_methods=["*"],
    allow_headers=["*"],
) # Configure CORS
