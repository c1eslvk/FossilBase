import httpx

from fossilbase.mappers import occurrence_mapper
from fossilbase.models.occurrence import Occurrence

PBDB_OCCS_URL = "https://paleobiodb.org/data1.2/occs/list.json"

def find_occurrences(
        name: str,
        interval: str | None = None,
        location: tuple[float, float, float, float] | None = None
        ) -> list[Occurrence]:
    params = {
        'base_name': name,
        'show': 'coords,loc,env,ecospace,ident'
    }
    if interval is not None:
        params["interval"] = interval
    if location is not None:
        params["latmin"] = location[0]
        params["latmax"] = location[1]
        params["lngmin"] = location[2]
        params["lngmax"] = location[3]

    r = httpx.get(PBDB_OCCS_URL, params=params)
    records = r.json()["records"]
    mapped_records = []
    for record in records:
        mapped_records.append(occurrence_mapper.map_to_occurrence(record))
    return mapped_records


