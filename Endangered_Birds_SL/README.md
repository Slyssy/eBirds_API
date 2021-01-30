# Project 1 Plan
========================
## Cornell Bird Lab
### [eBird API 2.0 documentation](https://documenter.getpostman.com/view/664302/S1ENwy59)
* Uses Cornell bird lab data of bird observations from around the world
* Recommend scoping down to Texas and only observations within a specific time period (ie last week) b/c database is HUGE
* Could merge with weather data from open weather map
* Would make for fun visualizations fo number of bird sightings and different bird species


----------------------
### Issues:
**1. DAVID** - Notable birds in region - try Texas or Austin (Houston!!) -- pick a few wildlife refuges / on the coast / national seashore / etc

**2. BRAD** - State by state total number of observations during two or more different time periods -- maybe bar chart by season? or plotly map of states in US with total # observations?

**3. JUGAL** - Historical weather -- free from NOAA API (requires GIT header) or OpenWeatherMap 

**4. STEPHEN** - Endangered species historical search -- "data deficiency as a proxy for endangered bird species"

**5. RACHEL** - Just for fun: bird sightings on historic days

**6. STEPHEN** - Find a list of endagered / threatened / least concern birds & try to merge with a group of sightings

**7. MARIA** - Migratory patterns -- pick one species, find sightings throughout the year -- plot counts in different regions (seasonally?) -- maybe pick a specific region and determine the earliest/latest date that a particular migratory species arrives/departs the area?

*-------Ed's Crazy Ideas-------*

8. RACHEL(?) - monk parakeet now vs then

9. Migration vs light pollution dataset? (darksky/darkskies)


----------------------
### Timeline:
* Tue 22nd
    * Plan & assign "issues" (topics/questions)
* Thurs 24th 
    * Check in on initial issue attempts 
    * problem solving 
    * **first attempt at merging!** 
    * *we should record this for reference*
* Sat 26th 
    * Cross-talk any issues that overlap
    * putting individual pieces into defined functions (keeps them separate in the master code?)
* Tue 29th 
    * Come with a draft of plots 
    * Double check all project requirements met -- readdress/fix as needed
* Thur 1st 
    * Making into a story / polishing / ready for presentation / practice
* Sat 3rd - **PROJECT DUE! PRESENTATION**


----------------------
### Notes:
#### Data Cleaning
* Location names not necessarily informative (e.g. "My House") -- instead rely on location id, region code, lat/lon, etc
* Bird species -- terms like "sp." "spp." and "species" indicate the observation is generic (particular species unknown / not identified) -- should probably pull out any instances of the above when counting "unique species"


----------------------
### Ed Recommendations:
* Problems merging Jupyter Notebook: when ready to commit, **convert notebook to python script and push** 

from terminal: jupyter nbconvert --to python notebook.ipynb

* can set on github only one person push to master (make master a protected branch)
* plotly recommended