from unittest.mock import MagicMock, patch

import httpx

from fossilbase.services.pbdb import find_occurrences


def test_find_occurences_name_only():
    fake_json = {
        "records": [
            {"tna": "Ankylosaurus magniventris",
             "jev": "terrestrial",
             "oei": "Late Maastrichtian",
             "jdt": "herbivore",
             "lat": 47,
             "lng": -106,
             "cc2": "US",
             "lag": 66,
             "eag": 72.2
             },
        ]
    }

    fake_response = MagicMock(spec=httpx.Response)
    fake_response.json.return_value = fake_json

    with patch("fossilbase.services.pbdb.httpx.get", return_value=fake_response) as mock_get:
        result = find_occurrences("Ankylosaurus")

    called_params = mock_get.call_args.kwargs["params"]
    assert called_params["base_name"] == "Ankylosaurus"
    assert "interval" not in called_params
    assert "latmin" not in called_params
    assert "latmax" not in called_params
    assert "lngmin" not in called_params
    assert "lngmax" not in called_params

    assert len(result) == 1
    assert result[0].taxon_name == "Ankylosaurus magniventris"