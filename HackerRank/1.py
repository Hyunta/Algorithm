import requests
import json


def get_total_goals(team, year):
    # Write your code here
    total = 0
    for i in range(1, 3):
        url = f"https://jsonmock.hackerrank.com/api/football_matches?year={year}&team{i}={team}"
        response = requests.get(url)
        result = json.loads(response.content)
        cur = 1
        total_pages_url = result['total_pages']
        while cur <= total_pages_url:
            url = f"https://jsonmock.hackerrank.com/api/football_matches?year={year}&team{i}={team}&page={cur}"
            response = requests.get(url)
            result = json.loads(response.content)
            for data in result['data']:
                if data[f'team{i}'].upper() == team.upper():
                    total += int(data[f'team{i}goals'])
            cur += 1
    return total
