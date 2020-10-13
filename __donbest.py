import requests
import json
from datetime import datetime
from tabulate import tabulate


def cmd_odds(sport, metadata, session):
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
    # Get Rundown Odds Data
    if sport_id == 0:
        print(0)
        # msg_subject, msg_body = SVC_Rundown.get_notice(16, metadata)
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
        for date in data:
            events = date["events"]
            game_data = {}
            for row in events:
                event_data = dict(row)
                game_data["event_id"] = event_data["event_id"]
                game_data["sport_id"] = event_data["sport_id"]
                game_data["event_date"] = event_data["event_date"]
                game_date = game_data["event_date"].split('T')[0]
                game_time = game_data["event_date"].split(
                    'T')[1].replace(':00Z', '')
                game_time = datetime.strptime(game_time, "%H:%M")
                game_time = game_time.strftime("%I:%M %p")
                score_data = event_data["score"]
                team_data = event_data["teams"]
                team_data0 = team_data[0]
                team_data1 = team_data[1]
                score_data["event_status"] = score_data["event_status"].split("_")[
                    1].lower().title()
                if team_data0["is_home"] is True:
                    game_data["home_name"] = team_data0["name"]
                    game_data["away_name"] = team_data1["name"]
                else:
                    game_data["home_name"] = team_data1["name"]
                    game_data["away_name"] = team_data0["name"]
                line_data = event_data["lines"]
                aff_cnt = 1
                body_text += "\n"
                body_text += (
                    "Home: "
                    + game_data["home_name"]
                    + " | "
                    + "Away: "
                    + game_data["away_name"]
                    + "\n"
                )
                body_text += (
                    "Status: "
                    + score_data["event_status"]
                    + " | "
                    + "Details: "
                    + score_data["event_status_detail"]
                    + "\n"
                )
                body_text += (
                    "Location: "
                    + score_data["venue_name"]
                    + ", "
                    + score_data["venue_location"]
                    + "\n"
                )
                affiliate_names = []
                home_spreads = []
                away_spreads = []
                total = []
                for k, v in line_data.items():
                    if aff_cnt <= 3:
                        line_text = ""
                        affiliates_data = dict(v)
                        spread_data = affiliates_data["spread"]
                        moneyline_data = affiliates_data["moneyline"]
                        total_data = affiliates_data["total"]
                        total_over = total_data["total_over"]
                        total.append(str(total_over))
                        if total_over == 0.0001:
                            total_over = "removed"
                        if moneyline_data["moneyline_home"] == 0.0001:
                            moneyline_data["moneyline_home"] = "removed"
                        if moneyline_data["moneyline_away"] == 0.0001:
                            moneyline_data["moneyline_away"] = "removed"
                        if spread_data["point_spread_home"] == 0.0001:
                            spread_data["point_spread_home"] = "removed"
                        if spread_data["point_spread_away"] == 0.0001:
                            spread_data["point_spread_away"] = "removed"
                        game_data["point_spread_home"] = spread_data[
                            "point_spread_home"
                        ]
                        game_data["point_spread_away"] = spread_data[
                            "point_spread_away"
                        ]
                        aff_data = affiliates_data["affiliate"]
                        aff_name = aff_data["affiliate_name"]

                        # if '-' in str(game_data["point_spread_home"]) and len(str(game_data["point_spread_home"])) > 2:
                        #     point_spread_home = str(
                        #         game_data["point_spread_home"]) + "     |"
                        # elif '-' in str(game_data["point_spread_home"]) and len(str(game_data["point_spread_home"])) <= 2:
                        #     point_spread_home = str(
                        #         game_data["point_spread_home"]) + "       |"
                        # elif '-' not in str(game_data["point_spread_home"]) and len(str(game_data["point_spread_home"])) <= 2:
                        #     point_spread_home = str(
                        #         game_data["point_spread_home"]) + "        |"
                        # elif '-' not in str(game_data["point_spread_home"]) and len(str(game_data["point_spread_home"])) > 2:
                        #     point_spread_home = str(
                        #         game_data["point_spread_home"]) + "      |"
                        # else:
                        #     point_spread_home = str(
                        #         game_data["point_spread_home"]) + "      |"

                        # if '-' in str(game_data["point_spread_away"]) and len(str(game_data["point_spread_away"])) > 2:
                        #     point_spread_away = str(
                        #         game_data["point_spread_away"]) + "     |"
                        # elif '-' in str(game_data["point_spread_away"]) and len(str(game_data["point_spread_away"])) <= 2:
                        #     point_spread_away = str(
                        #         game_data["point_spread_away"]) + "       |"
                        # elif '-' not in str(game_data["point_spread_away"]) and len(str(game_data["point_spread_away"])) <= 2:
                        #     point_spread_away = str(
                        #         game_data["point_spread_away"]) + "        |"
                        # elif '-' not in str(game_data["point_spread_away"]) and len(str(game_data["point_spread_away"])) > 2:
                        #     point_spread_away = str(
                        #         game_data["point_spread_away"]) + "      |"
                        # else:
                        #     point_spread_away = str(
                        #         game_data["point_spread_away"]) + "       |"

                        affiliate_names.append(aff_name)
                        home_spreads.append(
                            str(game_data["point_spread_home"]))
                        away_spreads.append(
                            str(game_data["point_spread_away"]))

                        # line_text += (str(aff_cnt) +
                        # ". Affiliate (" + aff_name + "): "
                        # aff_cnt += 1
                        # line_text += (
                        #     "Spread: [Home] "
                        #     + str(spread_data["point_spread_home"])
                        #     + " | "
                        #     + "[Away] "
                        #     + str(spread_data["point_spread_away"])
                        # )
                        line_text += (
                            " , MoneyLine: [Home] "
                            + str(moneyline_data["moneyline_home"])
                            + " | "
                            + "[Away] "
                            + str(moneyline_data["moneyline_away"])
                        )
                        line_text += " | Over/Under: " + str(total_over)
                        line_text += "\n"
                        body_text += line_text
            msg_body = body_text
            print('')
            if "event_date" in game_data:
                print(tabulate([[str(game_date) + " at", "[Home] " + game_data["home_name"], home_spreads[0], ''], [str(game_time), "[Away] " + game_data["away_name"], away_spreads[0], total[0]]],
                               headers=['Time', 'Team', "Spread", "Over/Under"], tablefmt='orgtbl'))
            # print(msg_body)
    if len(msg_body) < 16:
        msg_subject = "Sports: Error"
        msg_body = "There is no event data for " + sport_name + " at this time."
    return msg_subject, msg_body


cmd_odds("nfl", 2, 2)
