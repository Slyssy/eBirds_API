# import dependencies
import os
import requests
import json
import pandas as pd
import plotly.express as px
from config import api_key
from config import mapbox_token
from config import g_key
from calendar import monthrange

%reload_ext lab_black

px.set_mapbox_access_token(mapbox_token)

# create function to hold columns for df
def bird_data(data):
    return {
        "Common Name": data["comName"],
        "Scientific Name": data["sciName"],
        "Location Name": data["locName"],
        "Latitude": data["lat"],
        "Longitude": data["lng"],
        "Date": data["obsDt"],
        "Observation Validity": data["obsValid"],
    }

df.to_csv("Birds in Texas 2019.csv")

# pulling the hummingbird from df
humming_bird = df.loc[df["Scientific Name"] == "Archilochus colubris"]

#reset the index
humming_bird_df = pd.DataFrame(humming_bird).reset_index(drop=True)
humming_bird_df

# Spring (March through May) 3-5
# Summer (June through August) 6-8
# Fall (September through December) 9-12
# Winter (January through February) 1-2

humming_bird_df["Season"] = pd.cut(
    humming_bird_df["month"],
    bins=[0, 3, 6, 9, 13],
    labels=["Winter", "Spring", "Summer", "Fall"],
    right=False,
)

humming_bird_df["month"] = humming_bird_df["month"].replace({1: "January"})
humming_bird_df["month"] = humming_bird_df["month"].replace({2: "February"})
humming_bird_df["month"] = humming_bird_df["month"].replace({3: "March"})
humming_bird_df["month"] = humming_bird_df["month"].replace({4: "April"})
humming_bird_df["month"] = humming_bird_df["month"].replace({5: "May"})
humming_bird_df["month"] = humming_bird_df["month"].replace({6: "June"})
humming_bird_df["month"] = humming_bird_df["month"].replace({7: "July"})
humming_bird_df["month"] = humming_bird_df["month"].replace({8: "August"})
humming_bird_df["month"] = humming_bird_df["month"].replace({9: "September"})
humming_bird_df["month"] = humming_bird_df["month"].replace({10: "October"})
humming_bird_df["month"] = humming_bird_df["month"].replace({11: "November"})
humming_bird_df["month"] = humming_bird_df["month"].replace({12: "December"})


humming_bird_df

px.set_mapbox_access_token(mapbox_token)

fig = px.scatter_mapbox(
    humming_bird_df,
    lat="Latitude",
    lon="Longitude",
    color="Season",
    size="Latitude",
    animation_frame="month",
    color_continuous_scale=px.colors.cyclical.Edge,
    size_max=10,
    height=750,
    mapbox_style="stamen-terrain",
    zoom=4.5,
    title=f"Ruby-throated Hummingbirds Observed in Texas in 2019 by Month",
)

fig.show()