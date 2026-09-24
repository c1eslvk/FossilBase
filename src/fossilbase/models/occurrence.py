from pydantic import BaseModel


class Occurrence(BaseModel):
    taxon_name:str | None
    taxon_environment:str | None
    early_interval:str | None
    diet:str | None
    latitude:float | None
    longitude:float | None
    country:str | None
    age_min:float | None
    age_max:float | None
    