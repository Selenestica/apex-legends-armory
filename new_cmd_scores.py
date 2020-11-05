import requests
import json
from datetime import datetime, timedelta
import pytz


def cmd_scores(sport, metadata, session):
    # Figure Out the Sport Code
    sport_code = str(sport).lower().strip()
    if (sport_code == "ncaa football") or (sport_code == "1"):
        sport_name = "NCAA Football"
        sport_id = 1
    elif (sport_code == "nfl") or (sport_code == "2"):
        sport_name = "NFL"
        sport_id = 2
    elif (sport_code == "mlb") or (sport_code == "3"):
        sport_name = "MLB"
        sport_id = 3
    elif (sport_code == "nba") or (sport_code == "4"):
        sport_name = "NBA"
        sport_id = 4
    elif (sport_code == "ncaa men's basketball") or (sport_code == "5"):
        sport_name = "NCAA Men's Basketball"
        sport_id = 5
    elif (sport_code == "nhl") or (sport_code == "6"):
        sport_name = "NHL"
        sport_id = 6
    elif (
        (sport_code == "ufc")
        or (sport_code == "mma")
        or (sport_code == "ufc/mma")
        or (sport_code == "7")
    ):
        sport_name = "UFC/MMA"
        sport_id = 7
    elif (sport_code == "wnba") or (sport_code == "8"):
        sport_name = "WNBA"
        sport_id = 8
    elif (sport_code == "cfl") or (sport_code == "9"):
        sport_name = "CFL"
        sport_id = 9
    else:
        sport_id = 0
    # Get Rundown Sports Data
    if sport_id == 0:
        msg_subject, msg_body = SVC_Rundown.get_notice(16, metadata)
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
    print(msg_subject, msg_body)


cmd_scores("1", 2, 2)

# def get_notice(notice_id, metadata):
#     notices = Table("notices", metadata, autoload=True)
#     qry = notices.select().where(notices.c.notice_id == notice_id).limit(1)
#     results = qry.execute()
#     notice_data = {}
#     for row in results:
#         notice_data = dict(row)
#     return notice_data["notice_subject"], notice_data["notice_text"]
