from fastapi import APIRouter, Depends, status
from typing import List, Optional

from schemas.AuthorSchema import AuthorPostRequestSchema, AuthorPostResponseSchema, AuthorSchema
from services.AuthorService import AuthorService

AuthorRouter = APIRouter(prefix="/authors", tags=["author"])

@AuthorRouter.get("/", response_model=List[AuthorSchema])
def index(pageSize: Optional[int] = 100, startIndex: Optional[int] = 0, authorService: AuthorService = Depends()):
  return authorService.index(pageSize, startIndex)

@AuthorRouter.get("/{id}", response_model=AuthorSchema)
def get(id: int, authorService: AuthorService = Depends()):
  return authorService.get(id)

@AuthorRouter.post("/", response_model=AuthorPostResponseSchema, status_code=status.HTTP_201_CREATED)
def create(author: AuthorPostRequestSchema, authorService: AuthorService = Depends()):
  return authorService.create(author)

@AuthorRouter.put("/{id}", response_model=AuthorSchema)
def update(id: int, author: AuthorPostRequestSchema, authorService: AuthorService = Depends()):
  return authorService.update(id, author)

@AuthorRouter.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(id: int, authorService: AuthorService = Depends()):
  return authorService.delete(id)
