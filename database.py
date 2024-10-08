import sqlite3
import stat

from sqlite3 import Connection
from fastapi import HTTPException
from models import DogBreedUpdate, DogBreeds, DogBreed


def get_dog_breeds(connection: Connection) -> DogBreeds:
    with connection:
        cursor = connection.cursor().execute(
            '''
            SELECT *
            FROM dog_breeds;
            '''
        )
        return DogBreeds( dogBreeds = [DogBreed.model_validate(dict(dog_breed)) for dog_breed in cursor])


def get_dog_breed_by_id(connection: Connection, dog_breed_id: str) -> DogBreed:
    with connection:
        cursor = connection.cursor().execute(
            '''
            SELECT *
            FROM dog_breeds
            WHERE id=:dog_breed_id;
            ''',
             {"dog_breed_id": dog_breed_id}
        )
        row = cursor.fetchone()
        if row:
            return DogBreed.model_validate(dict(row))
        return None
    

def insert_dog_breed(connection: Connection, dog_breed: DogBreed) -> None:
    fields = {key: value for key, value in dog_breed.__dict__.items() if value is not None}

    if not fields:
            raise HTTPException(
                status_code=stat.HTTP_400_BAD_REQUEST,
                detail="No fields provided for update."
            )
    
    columns = ", ".join(fields.keys())
    placeholders = ", ".join([f":{key}" for key in fields.keys()])
    query = f'''
        INSERT INTO dog_breeds ({columns})
        VALUES ({placeholders});
    '''
    with connection:
        cursor = connection.cursor()
        cursor.execute(query, fields)


def update_dog_breed(connection: Connection, dog_breed_id: str, dog_breed: DogBreedUpdate) -> None:
    fields = {key: value for key, value in dog_breed.__dict__.items() if value is not None}

    if not fields:
        raise HTTPException(
            status_code=stat.HTTP_400_BAD_REQUEST,
            detail="No fields provided for update."
        )

    set_clause = ", ".join([f"{key} = :{key}" for key in fields.keys()])
    query = f'''
        UPDATE dog_breeds
        SET {set_clause}
        WHERE id = :id;
    '''
    
    fields["id"] = dog_breed_id

    with connection:
        cursor = connection.cursor()
        cursor.execute(query, fields)

        if cursor.rowcount == 0:
            raise HTTPException(
                status_code=stat.HTTP_404_NOT_FOUND,
                detail="Dog breed not found."
            )


def delete_dog_breed(connection: Connection, dog_breed_id: str) -> None:
     with connection:
        cursor = connection.cursor()
        cursor.execute(
            '''
            DELETE FROM dog_breeds
            WHERE id = :dog_breed_id;
            ''',
            {"dog_breed_id": dog_breed_id}
        )

        if cursor.rowcount == 0:
            raise HTTPException(
                status_code=stat.HTTP_404_NOT_FOUND,
                detail="Dog breed not found."
            )


if __name__ == "__main__":
    connection = sqlite3.connect('dog_breeds.db')
    connection.row_factory = sqlite3.Row

    print(get_dog_breeds(connection))