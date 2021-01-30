%load_ext lab_black

import pandas as pd
import plotly.graph_objects as go
import requests
import json
import glob
import datetime
import plotly.express as px
from config import api_key
from config import mapbox_token
from calendar import monthrange


# Data pulled from U.S. Fish & Wildlife Service
# https://ecos.fws.gov/ecp/report/species-listings-by-tax-group?statusCategory=Listed&groupName=Birds
endangered_bird_data_to_load = "Resources/endangered_birds.csv"

endangered_birds_data = pd.read_csv(endangered_bird_data_to_load)

![USFW Regions](Resources/Images/USFW_Regions.png)

# Number of endangered bird that can be found in each US Fish and Wildlife Service Region.
endangered_df = endangered_birds_data
endangered_df["Region  "].value_counts()

### Requesting all bird sightings in the US that have been logged over the last 7 days.
#### This data will be merged with endangered species list to show only the birds that are listed as endangered or threatened.

regionCode = "US"

url = f"https://api.ebird.org/v2/data/obs/{regionCode}/recent"

r = requests.get(url, params={"key": api_key, "back": 7})

r.url

r.status_code

data = r.json()

# This is the recent sightings DataFrame
recent_birds_df = pd.DataFrame(data)
recent_birds_df

endangered_df.head()

# Merging endangered bird DataFrame with recent sightings DataFrame
endangered_recent_df = endangered_df.merge(
    recent_birds_df, left_on="Scientific Name", right_on="sciName"
)
endangered_recent_df

# Setting MapBox token.
px.set_mapbox_access_token(mapbox_token)

# Generating scatter map.
fig = px.scatter_mapbox(
    endangered_recent_df,
    lat="lat",
    lon="lng",
    color="howMany",
    hover_data=["Common Name", "Scientific Name", "Where Listed", "locName"],
    title="Endangered Bird Species Sitings in the United States (Last 7 Days)",
    height=750,
)
fig.show()

### Sightings for the birds in the endangered species list (sited in the last 7 days) in the state they were observed over several years.
#### (Requesting Data to determine the number of sightings for all birds that have been observed in the states indicated above.)

# List of years to plug into API request
year_list = ["2020", "2019", "2018", "2017", "2016", "2015", "2010", "2005", "2000"]

def extract_data(data):

    return {
        "Common Name": data["comName"],
        "Scientific Name": data["sciName"],
        "Date Sighted": data["obsDt"],
        "Location Name": data["locName"],
        "Num Sighted": data["howMany"],
        "Latitude": data["lat"],
        "Longitude": data["lng"],
    }

# Use this code to creat csv files for each state with endagered birds sited on date.
year_results = []
regionCode = "US-IL"
year = []
month = "9"
day = "22"

for year in year_list:
    data = requests.get(
        f"https://api.ebird.org/v2/data/obs/{regionCode}/historic/{year}/{month}/{day}",
        params={"key": api_key},
    ).json()

    for bird in data:
        try:
            results = extract_data(bird)
            results["year"] = year
            year_results.append(results)

        except KeyError:
            pass

# il_df = pd.DataFrame(year_results)
# il_df.to_csv("illinois_sightings.csv")

# Combining all CSVs that include the all of the bird sitings in the states that reported endangered bird sitings in the past 7 days. I picked the first day of Autumnfor each year indicated in year_list.
path = "Resources/Endangered_State_Files"
all_files = glob.glob(path + "/*.csv")

li = []

for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=0)
    li.append(df)

birds_states_df = pd.concat(li, axis=0, ignore_index=True)
birds_states_df

# List of birds (scientific name) that have been seen in the US over the last 7 days.
endangered_list = endangered_recent_df["Scientific Name"].to_list()
endangered_list_unique = list(set(endangered_list))
endangered_list_unique

## Endangered bird sitings for the states that reported endagered bird sightings in the past seven days

![Endangered Header](Resources/Images/Endangered_Bird_Header.png)

endangered_bird_states_df = birds_states_df[
    birds_states_df["Scientific Name"].isin(endangered_list_unique)
]
endangered_bird_states_df

barchart = px.bar(
    endangered_bird_states_df,
    x="Num Sighted",
    y="year",
    color="Common Name",
    opacity=0.9,
    orientation="h",
    barmode="relative",
    hover_data=["Scientific Name", "Date Sighted", "Location Name"],
    title="'Recent' Endangered Bird Sightings Per State Sited Over Multiple Years",
)
barchart

![Autumn Bird](Resources/Images/Autumn_Bird.png)

### Pulling Bird Sightings across the entire US on the first day of Autumn and Filtering DataFrame to show only Endangered Bird Sitings

year_results = []
regionCode = "US"
year = []
month = "9"
day = "22"

for year in year_list:
    data = requests.get(
        f"https://api.ebird.org/v2/data/obs/{regionCode}/historic/{year}/{month}/{day}",
        params={"key": api_key},
    ).json()

    for bird in data:
        try:
            results = extract_data(bird)
            results["year"] = year
            year_results.append(results)

        except KeyError:
            pass

birds_usa_df = pd.DataFrame(year_results)
birds_usa_df

# Creating a list of all of the birds that are classified as endangered by the US Dept. of Fish and Wildlife Services.
endangered_usa_list = endangered_df["Scientific Name"].to_list()

# Filtering DataFrame to show only birds that are on the endangered list.
endangered_usa_fall_df = birds_usa_df[
    birds_usa_df["Scientific Name"].isin(endangered_usa_list)
]
endangered_usa_fall_df

barchart = px.bar(
    endangered_usa_fall_df,
    x="Num Sighted",
    y="year",
    color="Common Name",
    opacity=0.9,
    orientation="h",
    barmode="relative",
    hover_data=["Scientific Name", "Date Sighted", "Location Name"],
    title="Endangered Bird Sightings in the USA for the First Day of Autumn",
)
barchart

### Creating a chart to visualize the change in sightings of endagered birds in the state of Texas over a number of years.

# Bird Sightings in Texas over a number of years.
year_results = []
regionCode = "US-TX"
year = []
month = "9"
day = "22"

for year in year_list:
    data = requests.get(
        f"https://api.ebird.org/v2/data/obs/{regionCode}/historic/{year}/{month}/{day}",
        params={"key": api_key},
    ).json()

    for bird in data:
        try:
            results = extract_data(bird)
            results["year"] = year
            year_results.append(results)

        except KeyError:
            pass

tx_df = pd.DataFrame(year_results)
tx_df

endangered_tx_fall_df = tx_df[tx_df["Scientific Name"].isin(endangered_usa_list)]
endangered_tx_fall_df

barchart = px.bar(
    endangered_tx_fall_df,
    x="year",
    y="Num Sighted",
    color="Common Name",
    opacity=0.9,
    orientation="v",
    barmode="relative",
    hover_data=["Scientific Name", "Date Sighted", "Location Name"],
    title="Endangered Bird Sightings in Texas",
)
barchart

fig = px.scatter_mapbox(
    endangered_tx_fall_df,
    lat="Latitude",
    lon="Longitude",
    color="Common Name",
    hover_data=["Common Name", "Scientific Name", "Location Name", "year"],
    title="Endangered Bird Sightings in Texas (2000, 2005, 2010, 2015, 2016, 2017, 2018, 2019, 2020)",
    height=750,
)
fig.show()

![Endangered Texas Birds](Resources/Images/Endangered_Texas.png)



Scrap Code

