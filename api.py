from fastapi import FastAPI, HTTPException
from typing import Optional

app = FastAPI()


@app.get("/")
async def root():
    """Root endpoint that returns available endpoints."""
    return {
        "endpoints": {
            "/": "This help message",
            "/add": "Add two numbers (params: a, b)",
            "/subtract": "Subtract two numbers (params: a, b)"
        }
    }


@app.get("/add")
async def add(a: Optional[int] = None, b: Optional[int] = None):
    """Add two numbers.
    
    Query Parameters:
    - a (int): The first number.
    - b (int): The second number.
    
    Returns:
    - JSON: The sum of the two numbers.
    """
    if a is None or b is None:
        raise HTTPException(
            status_code=400,
            detail="Please provide both 'a' and 'b' as integers.")
    return {"result": a + b}


@app.get("/subtract")
async def subtract(a: Optional[int] = None, b: Optional[int] = None):
    """Subtract two numbers.
    
    Query Parameters:
    - a (int): The first number.
    - b (int): The second number.
    
    Returns:
    - JSON: The result of subtracting b from a.
    """
    if a is None or b is None:
        raise HTTPException(
            status_code=400,
            detail="Please provide both 'a' and 'b' as intgers.")
    return {"result": a - b}
