from fastapi import FastAPI, Header
from typing import Union, Optional, Any
import time

from pydantic import BaseModel

app = FastAPI()

@app.get("/")
async def read_root() -> dict[str, str]:
    return {"message": "Hello, World!"}

@app.get("/greet/{name}")
async def greet(name: str) -> dict[str, str]:
    return {"message": f"Hello, {name}!"}

@app.get("/greet_params")
async def greet(name: str)-> dict[str, str]:
    return {"message": f"Hello, {name}!"}

@app.get("/Projects/{project_id}")
async def get_project(
        project_id: Union[str, int],
        name: str, 
        is_active: Optional[bool] = True, 
        age: int = 18) -> dict[str,Union[str, int, bool, None]]:

    name_length = len(name)
    return {
        "project_id": project_id,
        "name": name,
        "name_length": name_length,
        "is_active": is_active,
        "age": age
    }

class BookCreateModel(BaseModel):
    title: str
    author: str
    description: Optional[str] = None
    price: float

@app.post("/create_book")
async def create_book(book_data: BookCreateModel) -> dict[str, Any]:
    return {"message": f"Book created successfully!", 
    "book_data": {"title": book_data.title, 
                "author": book_data.author, 
                "description": book_data.description, 
                "price": book_data.price,
                "length": len(book_data.description) if book_data.description else 0
                }
    }

@app.get("/greet_user")
async def greet_user(name: Optional[str] = "User") -> dict[str, str]:
    return {"message": f"Hello, {name}!"}

@app.get("/get_headers", status_code=201)
async def get_headers(
    accept: Optional[str] = Header(default=None),
    content_type: Optional[str] = Header(default=None),
    user_agent: Optional[str] = Header(default=None),
    host: Optional[str] = Header(default=None),
    authorization: Optional[str] = Header(default=None),
    x_api_key: Optional[str] = Header(default=None),
    x_request_id: Optional[str] = Header(default=None),
    x_trace_id: Optional[str] = Header(default=None),
    x_span_id: Optional[str] = Header(default=None),
    x_parent_span_id: Optional[str] = Header(default=None),
) -> dict[str, Any]:
    response_headers = {
        "Accept": accept,
        "Content-Type": content_type,
        "User-Agent": user_agent,
        "Authorization": authorization,
        "X-API-Key": x_api_key,
        "X-Request-ID": x_request_id,
        "X-Trace-ID": x_trace_id,
        "X-Span-ID": x_span_id,
        "X-Parent-Span-ID": x_parent_span_id,
        "Host": host
    }
    return response_headers