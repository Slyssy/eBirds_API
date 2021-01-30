# eBirds_API

### For this exercise, we made serveral api requests from Cornell University's Ebird API. In order to run these request you will need to obtain an eBird API Key.

### Technology Employed: 
* Jupyter Notebook imports: CSV, OS, Requests, JSON, Datetime
* Python: Pandas, Numpy
* Visualizations: Plot.ly, mapbox

### Contributors
Rachel Reynolds: Parakeet Story<br>
David Vance: Notable Observations<br>
Stephen Lyssy: Endangered Birds<br>
Brad Lampton: State by State Observations<br>
Maria Sierra-Cardoza: Migratory Pattern (Ruby-Throated Hummingbird)<br>

### Below is a list of API Request in order to get the data we needed for the visualizations shown below.
* Migratory Pattern (Ruby-throated Hummingbird): https://api.ebird.org/v2/data/obs/US-TX/historic/2019/{month}/{day}
* Notable Observations: https://api.ebird.org/v2/data/obs/
* Endangered Birds: https://api.ebird.org/v2/data/obs/{{regionCode}}/recent, https://api.ebird.org/v2/product/stats/{{regionCode}}/{{y}}/{{m}}/{{d}}
* ParaKeet Story: https://api.ebird.org/v2/data/obs/{{regionCode}}/historic/{{y}}/{{m}}/{{d}}

## Migratory Pattern (Ruby-Throated Hummingbird)
![ruby_throated_hummingbird](images/ruby_throated_hummingbird.png)
<br>
<br>
![ruby_throated_hummingbird_map](images/ruby_throated_hummingbird_map.png)
<br>
<br>
## State Bird Sightings
![state_bird_sightings](images/state_bird_sightings.png)
## Notable Observations
![notable_calliope_hummingbird](images/notable_calliope_hummingbird.png)
![notable_observations_all_species_map](images/notable_observations_all_species_map.png)
## Endangered Birds
![usfw_region_map](images/usfw_region_map.png)
<br>
<br>
![endangered_bird_sitings_7days](images/endangered_bird_sitings_7days.png)
<br>
![engangered_autumn](images/engangered_autumn.png)
<br>
![engangered_autumn_map](images/engangered_autumn_map.png)
<br>
<br>
## Parakeet Story
![then_and_now](images/then_and_now.png)
![historic_contributors](images/historic_contributors.png)
![final_sightings](images/final_sightings.png)
![monk_parakeet](images/monk_parakeet.png)
![monk_parakeet_map](images/monk_parakeet_map.png)
![monk_parakeet_austin](images/monk_parakeet_austin.png)
![monk_parakeet_austin_map](images/monk_parakeet_austin_map.png)
![monk_parakeet_austin_thermal](images/monk_parakeet_austin_thermal.png)


