import requests
import json
from datetime import datetime, timedelta
import pytz


def cmd_odds(sport, metadata, session):
    # Figure Out the Sport Code
    todays_date = datetime.now()
    week_out = todays_date + timedelta(days=7)
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
    # Get Rundown Odds Data
    if sport_id == 0:
        msg_subject, odds_info = "dd", "847hfxwm84x7hfwd98473yhdw9843ysjdw8974yfsj8374ydsj28374ydj"
    else:
        msg_subject = "Sports: " + sport_name
        url = f"https://www.corbot.us/data/odds-{sport_id}.json"
        body_text = ""
        r = requests.get(
            url,
            headers={
                "User-agent": "Mozilla/5.0 (X11; Linux i686; rv:64.0) Gecko/20100101 Firefox/70.0"
            },
        )

        j_data = json.loads(r.text)
        data = j_data["data"]
        odds_info = '\n'
        for date in data:
            events = date["events"]
            if len(events) > 0:
                game_data = {}
                for event_data in events:
                    game_data["event_id"] = event_data["event_id"]
                    game_data["sport_id"] = event_data["sport_id"]

                    # get date and time
                    game_data["event_date"] = event_data["event_date"]
                    game_date = game_data["event_date"].split('T')[0]
                    game_date_date = datetime.strptime(game_date, "%Y-%m-%d")
                    game_time = game_data["event_date"].split(
                        'T')[1].replace(':00Z', '')
                    game_time = datetime.strptime(game_time, "%H:%M")
                    # function to see if its DST in CST

                    def is_dst(time_arg, tz_arg):
                        tz_arg = pytz.timezone(tz_arg)
                        tz_arg_aware_date = tz_arg.localize(
                            time_arg, is_dst=None)
                        return tz_arg_aware_date.tzinfo._dst.seconds != 0
                    if is_dst(game_date_date, "US/Central") == True:
                        game_time = game_time - timedelta(hours=5)
                    else:
                        game_time = game_time - timedelta(hours=6)
                    game_time = game_time.strftime("%I:%M %p")

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

                    score_data["event_status"] = score_data["event_status"].split("_")[
                        1].lower().title()

                    aff_cnt = 1
                    if "lines" in event_data:
                        affiliate_names = []
                        home_spreads = []
                        away_spreads = []
                        total = []
                    else:
                        affiliate_names = ["No data"]
                        home_spreads = ["No data"]
                        away_spreads = ["No data"]
                        total = ["No data"]
                    if "lines" in event_data:
                        line_data = event_data["lines"]
                        for k, v in line_data.items():
                            if aff_cnt <= 5:
                                affiliates_data = dict(v)
                                spread_data = affiliates_data["spread"]
                                total_data = affiliates_data["total"]
                                total_over = total_data["total_over"]

                                # if spread or total is a pulled line
                                if total_over == 0.0001:
                                    total_over = "No data"
                                if spread_data["point_spread_home"] == 0.0001:
                                    spread_data["point_spread_home"] = "No data"
                                if spread_data["point_spread_away"] == 0.0001:
                                    spread_data["point_spread_away"] = "No data"

                                game_data["point_spread_home"] = spread_data[
                                    "point_spread_home"
                                ]
                                game_data["point_spread_away"] = spread_data[
                                    "point_spread_away"
                                ]
                                aff_data = affiliates_data["affiliate"]
                                aff_name = aff_data["affiliate_name"]

                                affiliate_names.append(aff_name)
                                aff_cnt += 1
                                if spread_data["point_spread_home"] != "No data" and aff_cnt < 5:
                                    home_spreads.append(
                                        str(game_data["point_spread_home"]))
                                else:
                                    home_spreads.append(
                                        str(game_data["point_spread_home"]))
                                if spread_data["point_spread_away"] != "No data" and aff_cnt < 5:
                                    away_spreads.append(
                                        str(game_data["point_spread_away"]))
                                else:
                                    away_spreads.append(
                                        str(game_data["point_spread_away"]))
                                if total_over != "No data" and aff_cnt < 5:
                                    total.append(str(total_over))
                                else:
                                    total.append(str(total_over))

                    if game_date_date <= week_out:
                        odds_info += ("Time: " + str(game_date) + " at " + str(game_time) + "\n" + "Home: " + game_data["home_name"] + " | Spread: " + home_spreads[0] + "\n"
                                      "Away: " + game_data["away_name"] + " | Spread: " + away_spreads[0] + "\n" + "Over/Under: " + total[0] + '\n\n')

    print(odds_info)
    if len(odds_info) < 16:
        msg_subject = "Sports: Error"
        odds_info = "There is no event data for " + sport_name + " at this time."
    return msg_subject, odds_info


cmd_odds("nfl", 2, 2)
