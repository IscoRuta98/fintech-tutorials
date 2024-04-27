from fastapi import APIRouter
from models.todos import Todo
from config.database import collection_name
from schema.schemas import list_serial
from bson import ObjectId

router = APIRouter()

# GET all TODOs
@router.get("/")
async def get_todos():
    todos = list_serial(collection_name.find())
    return todos

# POST Create a TODO
@router.post("/",status_code=201)
async def post_todo(todo: Todo):
    collection_name.insert_one(dict(todo))

# PUT Update a TODO
@router.put("/{id}",status_code=204)
async def put_todo(id: str, todo: Todo):
    collection_name.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(todo)})

# DELETE TODO
@router.delete("/{id}",status_code=204)
async def delete_todo(id: str):
    collection_name.find_one_and_delete({"_id": ObjectId(id)})