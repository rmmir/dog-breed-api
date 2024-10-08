from fastapi import FastAPI
from database import get_dog_breeds, insert_dog_breed, update_dog_breed
from models import DogBreeds, DogBreed, DogBreedUpdate
from sqlite3 import Connection, Row


app = FastAPI()
connection = Connection('dog_breeds.db')
connection.row_factory = Row


@app.get('/dog-breeds')
async def dog_breeds() -> DogBreeds:
    return get_dog_breeds(connection)


@app.post('/dog-breeds')
async def add_dog_breed(dog_breed: DogBreed) -> DogBreed:
    insert_dog_breed(connection, dog_breed)
    return dog_breed


@app.patch('/dog-breeds/{dog_breed_id}')
async def edit_dog_breed(dog_breed_id: str, dog_breed: DogBreedUpdate) -> DogBreedUpdate:
    update_dog_breed(connection, dog_breed_id, dog_breed)
    return dog_breed