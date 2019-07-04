from collections import defaultdict
from string import Template

TABLE_ROW = Template("$team|  $pld |  $w |  $d |  $l |  $pts")
TABLE_HEADER = "Team                           | MP |  W |  D |  L |  P"


def make_row(team, score):
    s = score
    return TABLE_ROW.substitute(
        team=team.ljust(31), pld=s["pld"], w=s["w"], d=s["d"], l=s["l"], pts=s["pts"]
    )


def extract_scores(rows):
    scores = defaultdict(lambda: dict(pld=0, w=0, l=0, d=0, pts=0))
    for row in rows:
        home, away, result = row.split(";")

        scores[home]["pld"] += 1
        scores[away]["pld"] += 1

        if result == "win":
            scores[home]["w"] += 1
            scores[away]["l"] += 1
            scores[home]["pts"] += 3
        elif result == "draw":
            scores[home]["d"] += 1
            scores[away]["d"] += 1
            scores[home]["pts"] += 1
            scores[away]["pts"] += 1
        else:
            scores[away]["w"] += 1
            scores[home]["l"] += 1
            scores[away]["pts"] += 3
    return scores


def tally(rows):
    scores = extract_scores(rows)

    table = [TABLE_HEADER]
    by_points = lambda k: k[1]["pts"]
    for team, score in sorted(scores.items(), key=by_points, reverse=True):
        table.append(make_row(team, score))

    return table
