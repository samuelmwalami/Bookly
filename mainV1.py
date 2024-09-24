from fastapi import FastAPI,Header
from pydantic import BaseModel
app = FastAPI()

class BookCreateModel(BaseModel):
    title : str
    author : str


@app.get("/")
async def hello():
    return {"Message" : "Hello"}

@app.post("/create_book", status_code=201)
async def create_book(book : BookCreateModel):
    return{
        "Title" : book.title,
        "Author" : book.author
    }
    
@app.get("/get_headers", status_code=200)
async def get_headers(
    accept:str = Header(None),
    content_type:str = Header(None),
    date:str = Header(None),
    user_agent:str = Header(None),
    host:str = Header(None)
):
    request_headers = {}
    request_headers["ACCEPT"] = accept
    request_headers["CONTENT-TYPE"] = content_type
    request_headers["DATE"] = date
    request_headers["USER-AGENT"] = user_agent
    request_headers["HOST"] = host
    
    return request_headers