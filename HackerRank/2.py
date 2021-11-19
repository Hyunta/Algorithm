import requests
import json


def get_num_draw(year):
    total = 0
    for i in range(0, 12):
        url = f"https://jsonmock.hackerrank.com/api/football_matches?year={year}&team1goals={i}&team2goals={i}"
        response = requests.get(url)
        result = json.loads(response.content)
        total += result['total']
    return total
