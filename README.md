# 🦴 FossilBase

**Explore the fossil record by time and place.**

FossilBase is a Python web app that queries fossil occurrences from the
[Paleobiology Database (PBDB)](https://paleobiodb.org/) and plots them on an
interactive map. Pick a geologic era and a region of the world, and see where
those creatures actually lived — millions of years ago.

## What it does

- 🔎 **Query by era & region** — search fossil occurrences for a given geologic
  time interval (e.g. *Cretaceous*) and geographic area.
- 🗺️ **Map them** — every occurrence is plotted on an interactive map you can
  pan, zoom, and click for details.
- 🧭 **Explore by time** — browse the deep past one era at a time.

## How it works

FossilBase pulls live data from the public **PBDB data API** and turns it into
an explorable map:

```
You  ──▶  FastAPI web app  ──▶  Query core  ──▶  PBDB API
                                     │
                                     ▼
                          Interactive folium map
```

> 📊 *Pipeline and data-flow diagrams will be added here as the app takes shape.*

## Tech stack

| Concern        | Tool                          |
| -------------- | ----------------------------- |
| Language       | Python                        |
| Tooling        | [uv](https://docs.astral.sh/uv/) |
| Data source    | [PBDB API](https://paleobiodb.org/data1.2/) |
| Web framework  | FastAPI + Jinja templates     |
| Maps           | [folium](https://python-visualization.github.io/folium/) (Leaflet) |
| Testing        | pytest                        |

## Status

🚧 **Early development.**

## Data & attribution

Fossil occurrence data is provided by the
[Paleobiology Database](https://paleobiodb.org/). FossilBase is an independent
project and is not affiliated with the PBDB.
