# import dependencies
import requests
import pandas as pd
from config import api_key
from calendar import monthrange


# create an empty dictionary
dates_with_data = {}

# iterates over years in range (remember the iteration goes up to but doesn't include the second item in the range -- in this example, 1800-1999)
for year in range(1800, 2000):
    # iterates over months in range (up to but not including 13)
    for month in range(1, 13):
        # iterates over days in month -- calls the function monthrange() from the calendar library (have to import above)
        # monthrange() takes two arguments -- the year and the month and will return the number of days in that month.  For example, February 1980 was a leap year, so monthrange(1980, 2) will return 29.
        # remember that the iteration will go up to but not including the second number in the range, so add 1 to it to work 
        for day in range(1, monthrange(year, month)[1] + 1):
            
            # set the url with the year month and day variables in the for loop
            url = f"https://api.ebird.org/v2/product/stats/US/{year}/{month}/{day}"
            r = requests.get(url, params={"key": api_key})
            
            # this particular url returns a single dictionary, not a list of dictionaries -- other end points (such as notable birds, recent observations, etc) will return a list of dictionaries
            # make sure to do a test run to figure out how to extract the info you want from however the api returns your request
            json_dict = r.json()

            # I only append the empty dictionary with the info I want, and only if the dictionary I received from the API was not empty -- this might be different for different requests
            if sum(json_dict.values()) > 0:
                dates_with_data.setdefault("year", []).append(year)
                dates_with_data.setdefault("month", []).append(month)
                dates_with_data.setdefault("day", []).append(day)

                num_checklists = json_dict["numChecklists"]
                num_contributors = json_dict["numContributors"]
                num_species = json_dict["numSpecies"]

                dates_with_data.setdefault("checklists", []).append(num_checklists)
                dates_with_data.setdefault("contributors", []).append(num_contributors)
                dates_with_data.setdefault("species", []).append(num_species)

                print(
                    f"Date {month}/{day}/{year} has {num_contributors} contributors!!!!!!!!!!!!!!!!!"
                )

            else:
                print(f"No data for {month}/{day}/{year}")
    # at the end of the year in range(x, y) for loop, I saved whatever data has been extracted so far into a csv file -- just in case the connection was lost or something weird happened, I would at least have all of the data up to the point where the problem happened
    # this way, I could even open the csv file as the program was running and making API requests just to check and see if I was getting data every time the loop got finished with a year -- you could put this part of the code at the end of the month loop and save a copy of the data every time the iterator gets through all the days of a given month
    pd.DataFrame(dates_with_data).to_csv("bird_dates.csv", index=False)

# finally I saved the whole thing to a separate csv at the end -- since my API calls went well (took about 8.5 hours), this csv and the one above turned out to be identical.  Yay!
df = pd.DataFrame(dates_with_data)
df.to_csv("bird_dates_all.csv", index=False)