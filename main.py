from fastapi import FastAPI
from models import DogBreeds, DogBreed, DogBreedUpdate
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


@app.get('/dog-breeds')
async def get_all() -> DogBreeds:
    return get_dog_breeds(connection)


@app.get('/dog-breeds/{dog_breed_id}')
async def get_by_id(dog_breed_id: str) -> DogBreed:
    return get_dog_breed_by_id(connection, dog_breed_id)


@app.post('/dog-breeds')
async def add(dog_breed: DogBreed) -> None:
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
