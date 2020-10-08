import requests
import json

url = "https://therundown-therundown-v1.p.rapidapi.com/sports/1/dates"

headers = {
    'x-rapidapi-host': "therundown-therundown-v1.p.rapidapi.com",
    'x-rapidapi-key': "{our-api-key}"
}

response = requests.request("GET", url, headers=headers)

dates = response.text
dates = json.loads(dates)
dates_list = dates["dates"]
events_list = []
for date in dates_list:
    event_url = "https://therundown-therundown-v1.p.rapidapi.com/sports/1/events/" + \
        date + "?includes=scores&includes=teams"
    event_res = requests.request("GET", event_url, headers=headers)
    event_str = event_res.text
    event = json.loads(event_str)
    events_list.append(event)

print(type(events_list[0]))
print(len(events_list))
stuff = json.loads(events_list)
print(stuff)
