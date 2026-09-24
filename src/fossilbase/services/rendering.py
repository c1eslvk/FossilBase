import folium

from fossilbase.models.occurrence import Occurrence


def render_map(occurrences: list[Occurrence]) -> folium.Map:
    m = folium.Map(location=[0, 0], zoom_start=2, tiles=folium.TileLayer(no_wrap=True))

    for occurrence in occurrences:
        folium.Marker(
            location=[occurrence.latitude, occurrence.longitude],
            tooltip=occurrence.taxon_name,
            popup=folium.Popup(html=create_popup_html(occurrence), max_width=300),
            icon=folium.Icon(color="red")
        ).add_to(m)

    m.fit_bounds([[occ.latitude, occ.longitude] for occ in occurrences])
    m.save("index.html")

def create_popup_html(occurrence: Occurrence) -> str:
    return (
        f"<b>Name:</b> {occurrence.taxon_name}</b><br>"
        f"<b>Time Period:</b> {occurrence.early_interval} "
        f"({occurrence.age_min}–{occurrence.age_max} MA)<br>"
        f"<b>Environment:</b> {occurrence.taxon_environment}<br>"
        f"<b>Diet:</b> {occurrence.diet}<br>"
        f"<b>Fossil Location:</b> {occurrence.country} "
        f"({occurrence.latitude:.2f}, {occurrence.longitude:.2f})"
    )