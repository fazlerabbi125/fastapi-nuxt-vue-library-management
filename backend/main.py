from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from settings import config
from utils.custom_openapi import custom_openapi

app = FastAPI() # Create the FastAPI application instance

app.add_middleware(
    CORSMiddleware,
    allow_origins=config.cors_allow_origins,
    allow_methods=["*"],
    allow_headers=["*"],
) # Configure CORS

app.openapi = custom_openapi(
    app,
    title="Library Management API",
    version="1.0.0",
    summary="Documentation for a library management system"
)

@app.get("/")
async def root():
    return {"message": "Hello World"}
