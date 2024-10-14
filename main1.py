import os
import json
from fastapi import FastAPI, status
from pydantic import BaseModel
from typing import List

app = FastAPI()

"""Book data models """
#Get book response model
class Book(BaseModel):
    id : int
    title : str
    author : str
    publisher : str
    published_date : str
    page_count : int
    language : str
    
#Update book model
class UpdateBook(BaseModel):
    title : str
    author : str
    publisher : str
    page_count : str
    language : str
    


def load_books():
    if os.path.exists("books.json"):
        with open("books.json","r") as f:
           books = json.loads(f.read())
    return books
books = load_books()

@app.get("/books", response_model=List[Book] ,status_code=status.HTTP_200_OK)
async def get_books():
    return load_books()

@app.get("/book/{book_id}",response_model=Book,status_code=status.HTTP_200_OK)
async def get_book(book_id:int):
    books = load_books()
    for book in books:
        if book["id"] == book_id:
            my_book = book
    return my_book

@app.post("/book",response_model=Book,status_code=status.HTTP_201_CREATED)
async def add_book(book:Book):
    new_book = book.model_dump()
    return new_book

@app.patch("/book/{book_id}")
async def update_book(book:UpdateBook,book_id:int):
    book_update = book.model_dump()
    books = load_books()
    for book in books:
        if book["id"] == book_id:
            book["title"] = book_update["title"]            
            book["author"] = book_update["author"]
            book["publisher"] = book_update["publisher"]
            book["page_count"] = book_update["page_count"]
            book["language"] = book_update["language"]
            updated_book = book
    return book

@app.delete("/book/{book_id}")
async def delete_book():
    pass