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
    # sth = await db.execute(select(User))
    # print(28, sth.scalars().all()) # Use scalars() to get list of objects when all columns are selected to avoid getting list of tuples inside which is the object
    # sth = await db.execute(select(User).where(User.id == 2))
    # print(30, sth.scalars().one()) # or sth.scalars().one_or_none() or sth.scalar()
    # sth = await db.execute(select(User.id, User.email))
    # print(32, sth.all()) # When specific columns are selected, the result is list of tuples. Using scalars() only returns the first column
    # sth = await db.execute(select(User.id, User.email).where(User.id == 2))
    # print(34, sth.first())
    return {"message": "Hello World"}