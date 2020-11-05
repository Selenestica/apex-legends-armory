import requests
import json
from datetime import datetime, timedelta
import pytz


def get_sport_id_and_name(body):
    body_list = str(body).lower().split(" ")
    ncaa_foot_list = ["NCAA Football", "ncaa football", "ncaa", "1"]
    nfl_list = ["NFL", "nfl", "2", "nlf"]
    mlb_list = ["MLB", "3", "mlb", "mbl", "baseball"]
    nba_list = ["NBA", "nba", "4", "nab"]
    ncaa_mens_bb_list = ["NCAA Men's Basketball",
                         "ncaa mens basketball", "ncaa men's basketball", "5"]
    nhl_list = ["NHL", "6", "nhl", "nlh"]
    ufc_list = ["UFC/MMA", "7", "mma", "ufc", "ufc/mma", "mam", "ucf"]
    wnba_list = ["WNBA", "wnba", "8", "wbna"]
    cfl_list = ["CFL", "cfl", "clf", "9"]
    mls_ist = ["MLS", "10", "msl", "mls", "soccer"]
    sport_dict = {"1": ncaa_foot_list, "2": nfl_list, "3": mlb_list, "4": nba_list,
                  "5": ncaa_mens_bb_list, "6": nhl_list, "7": ufc_list, "8": wnba_list, "9": cfl_list, "10": mls_ist}
    sport_id = 0
    sport_name = ""
    for word in body_list:
        for k, v in sport_dict.items():
            if word in v:
                sport_id = int(k)
                sport_name = v[0]
    return sport_id, sport_name


def cmd_scores(sport, metadata, session):
    try:
        sport_id, sport_name = get_sport_id_and_name(sport)
        # Get Rundown Sports Data
        if sport_id == 0:
            msg_subject, msg_body = "SVC_Rundown.get_notice(16, metadata)", "sport = 0    slfoslodjcosidcjopajdicospidjcposij"
        else:
            msg_subject = "Sports: " + sport_name
            url = f"https://www.corbot.us/data/scores-{sport_id}-yesterday.json"
            body_text = "Game Data:\r"
            r = requests.get(
                url,
                headers={
                    "User-agent": "Mozilla/5.0 (X11; Linux i686; rv:64.0) Gecko/20100101 Firefox/70.0"
                },
            )

            j_data = json.loads(r.text)
            meta = j_data["meta"]
            events = j_data["events"]
            game_data = {}

            for row in events:
                event_data = dict(row)
                game_data["event_id"] = event_data["event_id"]
                game_data["sport_id"] = event_data["sport_id"]
                game_data["event_date"] = event_data["event_date"]
                score_data = event_data["score"]
                if "teams" in event_data:
                    team_data = event_data["teams"]
                    team_data0 = team_data[0]
                    team_data1 = team_data[1]
                    if team_data0["is_home"] is True:
                        game_data["home_name"] = team_data0["name"]
                        game_data["away_name"] = team_data1["name"]
                    else:
                        game_data["home_name"] = team_data1["name"]
                        game_data["away_name"] = team_data0["name"]
                else:
                    team_data = event_data["teams_normalized"]
                    team_data0 = team_data[0]
                    team_data1 = team_data[1]
                    if team_data0["is_home"] is True:
                        game_data["home_name"] = team_data0["name"] + \
                            ' ' + team_data0["mascot"]
                        game_data["away_name"] = team_data1["name"] + \
                            ' ' + team_data1["mascot"]
                    else:
                        game_data["home_name"] = team_data1["name"] + \
                            ' ' + team_data1["mascot"]
                        game_data["away_name"] = team_data0["name"] + \
                            ' ' + team_data0["mascot"]
                body_text += (
                    "Home: "
                    + game_data["home_name"]
                    + " | "
                    + "Away: "
                    + game_data["away_name"]
                    + "\n"
                )
                body_text += (
                    "Scores:  Home: "
                    + str(score_data["score_home"])
                    + " | "
                    + " Away: "
                    + str(score_data["score_away"])
                    + "\n"
                )
                body_text += (
                    "Venue Name: "
                    + score_data["venue_name"]
                    + " | "
                    + "Location: "
                    + score_data["venue_location"]
                    + "\n"
                )

                body_text += "\n"
            msg_body = body_text
        if len(msg_body) < 16:
            msg_subject = "Scores: Error"
            msg_body = "There is no score data for " + sport_name + " at this time."
        return msg_subject, msg_body
    except Exception as e:
        msg_subject = "Error"
        msg_body = "There was an issue with the server: " + str(e)
        return msg_subject, msg_body


print(cmd_scores("ass 1 titties", 2, 2))
