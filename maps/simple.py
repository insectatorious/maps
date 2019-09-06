import folium

base_map = folium.Map(control_scale=True,
                      max_zoom=32,
                      zoom_start=6)

folium.TileLayer('cartodbdark_matter', name="CartoDB Dark Matter").add_to(base_map)
folium.TileLayer("stamentoner", name='Stamen Toner').add_to(base_map)
folium.TileLayer('stamenwatercolor', name="Stamen Watercolor").add_to(base_map)
NASAGIBS_NightEarthURL: str = ("https://map1.vis.earthdata.nasa.gov/wmts-webmerc/VIIRS_CityLights_2012/default/{time}"
                               "/{tilematrixset}{maxZoom}/{z}/{y}/{x}.{format}")
NASAGIBS_NightEarthAttr: str = ("<a href='https://leaflet-extras.github.io/leaflet-providers/preview/#filter="
                                "NASAGIBS.ViirsEarthAtNight2012'>NASAGIBS.ViirsEarthAtNight2012</a>")
folium.TileLayer(tiles=NASAGIBS_NightEarthURL,
                 attr=NASAGIBS_NightEarthAttr,
                 name="NASA Earth at Night 2012",
                 minZoon=1,
                 maxZoom=8,
                 format="jpg",
                 time="",
                 tilematrixset="GoogleMapsCompatible_Level").add_to(base_map)

NASAMODISUrl: str = ("https://map1.vis.earthdata.nasa.gov/wmts-webmerc/"
                     "VIIRS_Black_Marble/default//"
                     "GoogleMapsCompatible_Level8/{z}/{y}/{x}.png")

folium.TileLayer(tiles=NASAMODISUrl,
                 attr="GIBS",
                 overlay=True,
                 show=False,
                 name="VIIRS_Black_Marble").add_to(base_map)

NASAMODISUrl: str = ("https://gibs.earthdata.nasa.gov/wmts/epsg3857/best/"
                     "GPW_Population_Density_2020/default//"
                     "GoogleMapsCompatible_Level7/{z}/{y}/{x}.png")

folium.TileLayer(tiles=NASAMODISUrl,
                 attr="GIBS",
                 overlay=True,
                 show=False,
                 opacity=0.9,
                 name="GPW_Population_Density_2020").add_to(base_map)

folium.LayerControl().add_to(base_map)

base_map.save("../out/simple.html")
