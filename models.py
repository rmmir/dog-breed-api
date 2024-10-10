from pydantic import BaseModel
from typing import List, Optional

class DogBreed(BaseModel):
    id: str
    metric_weight: str
    imperial_weight: str
    name: str
    temperament: str
    origin: str
    life_span: str
    reference_image_id: str

class DogBreeds(BaseModel):
    dogBreeds: List[DogBreed]

class DogBreedAdd(BaseModel):
    metric_weight: str
    imperial_weight: str
    name: str
    temperament: str
    origin: str
    life_span: str
    reference_image_id: str

class DogBreedUpdate(BaseModel):
    metric_weight: Optional[str] = None
    imperial_weight: Optional[str] = None
    name: Optional[str] = None
    temperament: Optional[str] = None
    origin: Optional[str] = None
    life_span: Optional[str] = None
    reference_image_id: Optional[str] = None