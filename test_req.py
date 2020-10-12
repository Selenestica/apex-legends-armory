import requests
import json

url = "https://therundown-therundown-v1.p.rapidapi.com/sports/2/dates"

headers = {
    'x-rapidapi-host': "therundown-therundown-v1.p.rapidapi.com",
    'x-rapidapi-key': ""
}

response = requests.request("GET", url, headers=headers)

dates = response.text
dates = json.loads(dates)
dates_list = dates["dates"]
short_dates = []
for long_date in dates_list:
    short_date = long_date.split("T")[0]
    short_dates.append(short_date)

print(short_dates)

# event_data = {}
# events_list = []
# for date in short_dates:
#     event_url = "https://therundown-therundown-v1.p.rapidapi.com/sports/2/events/" + \
#         date + "?includes=scores&includes=teams"
#     event_res = requests.request("GET", event_url, headers=headers)
#     event_str = event_res.text
#     event = json.loads(event_str)
#     events_list.append(event)

# # print("###")
# # print(events_list[7]["events"][0]["event_date"])
# # print("###")

# for event in events_list:
#     if event["events"]:
#         print(event["events"][0]["event_date"])
#     else:
#         print('no events')
