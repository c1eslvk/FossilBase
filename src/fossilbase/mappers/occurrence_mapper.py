from fossilbase.models.occurrence import Occurrence


def map_to_occurrence(record: dict) -> Occurrence:
    return Occurrence(
        taxon_name=record.get("tna"),
        taxon_environment=record.get("jev"),
        early_interval=record.get("oei"),
        diet=record.get("jdt"),
        latitude=record.get("lat"),
        longitude=record.get("lng"),
        country=record.get("cc2"),
        age_min=record.get("lag"),
        age_max=record.get("eag")
    )