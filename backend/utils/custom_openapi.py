from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
import inspect

def custom_openapi(app: FastAPI, title: str, version: str, **openapi_args: dict):
    params = inspect.signature(get_openapi).parameters
    for key in openapi_args.keys():
        if key in params:
            continue
        openapi_args.pop(key)

    def inner_func():
        if app.openapi_schema:
            return app.openapi_schema

        openapi_schema = get_openapi(
            title=title,
            version=version,
            **openapi_args,
            routes=app.routes,
        )
        app.openapi_schema = openapi_schema
        return app.openapi_schema

    return inner_func