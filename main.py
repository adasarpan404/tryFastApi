"""
This module provides a FastAPI application with two endpoints.
"""
from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    """
    A simple function to handle requests to the root URL ("/").
    
    Returns:
        dict: A dictionary containing a simple greeting.
    """
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    """
    A function to handle requests to "/items/{item_id}" URL.
    
    Args:
        item_id (int): The ID of the item.
        q (Union[str, None], optional): A query parameter (string or None). Defaults to None.
        
    Returns:
        dict: A dictionary containing the item ID and the query parameter.
    """
    return {"item_id": item_id, "q": q}
