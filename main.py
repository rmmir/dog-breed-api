from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models import DogBreeds, DogBreed, DogBreedUpdate, DogBreedAdd
from sqlite3 import Connection, Row
from database import (
    get_dog_breeds, 
    get_dog_breed_by_id, 
    insert_dog_breed, 
    update_dog_breed, 
    delete_dog_breed
)

app = FastAPI()
connection = Connection('dog_breeds.db')
connection.row_factory = Row
origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/dog-breeds')
async def get_all() -> DogBreeds:
    return get_dog_breeds(connection)


@app.get('/dog-breeds/{dog_breed_id}')
async def get_by_id(dog_breed_id: str) -> DogBreed:
    return get_dog_breed_by_id(connection, dog_breed_id)


@app.post('/dog-breeds')
async def add(dog_breed: DogBreedAdd) -> None:
    insert_dog_breed(connection, dog_breed)
    return None


@app.patch('/dog-breeds/{dog_breed_id}')
async def update(dog_breed_id: str, dog_breed: DogBreedUpdate) -> None:
    update_dog_breed(connection, dog_breed_id, dog_breed)
    return None


@app.delete('/dog-breeds/{dog_breed_id}')
async def delete(dog_breed_id: str) -> None:
    delete_dog_breed(connection, dog_breed_id)
    return None
