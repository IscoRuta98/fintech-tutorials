import requests

# Base URL for the JSONPlaceholder API
base_url = "https://jsonplaceholder.typicode.com"

# Function to perform GET request
def perform_get(endpoint):
    url = base_url + endpoint
    response = requests.get(url)
    return response.json()

# Function to perform POST request
def perform_post(endpoint, data):
    url = base_url + endpoint
    response = requests.post(url, json=data)
    return response.json()

# Function to perform PUT request
def perform_put(endpoint, data):
    url = base_url + endpoint
    response = requests.put(url, json=data)
    return response.json()

# Function to perform PATCH request
def perform_patch(endpoint, data):
    url = base_url + endpoint
    response = requests.patch(url, json=data)
    return response.json()

# Function to perform DELETE request
def perform_delete(endpoint):
    url = base_url + endpoint
    response = requests.delete(url)
    return response.status_code

# # GET /todos
todos = perform_get("/todos")
print("GET /todos:", todos)

# Uncomment the code you want to run.

# # GET /todos/1
# todo_1 = perform_get("/todos/1")
# print("GET /todos/1:", todo_1)

# # GET /todos/1/comments
# comments_todo_1 = perform_get("/todos/1/comments")
# print("GET /todos/1/comments:", comments_todo_1)

# # GET /todos?userId=1
# todos_user_1 = perform_get("/todos?userId=1")
# print("GET /todos?userId=1:", todos_user_1)

# POST /todos
# new_todo_data = {
#     "userId": 1,
#     "title": "Buy groceries",
#     "completed": False
# }
# new_todo = perform_post("/todos", new_todo_data)
# print("POST /todos:", new_todo)

# # PUT /todos/1
# updated_todo_data = {
#     "userId": 1,
#     "id": 1,
#     "title": "Buy groceries",
#     "completed": True
# }
# updated_todo = perform_put("/todos/1", updated_todo_data)
# print("PUT /todos/1:", updated_todo)

# # PATCH /todos/1
# patched_todo_data = {
#     "completed": False
# }
# patched_todo = perform_patch("/todos/1", patched_todo_data)
# print("PATCH /todos/1:", patched_todo)

# # DELETE /todos/1
# delete_status = perform_delete("/todos/1")
# print("DELETE /todos/1 Status Code:", delete_status)
