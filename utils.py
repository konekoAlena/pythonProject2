import json
from pprint import pprint

def load_candidate():

    with open("candidates.json", "r", encoding="utf-8") as file:
        data = json.load(file)
        candidates = {}
        for i in data:
            candidates[i['id']] = i

        return candidates


load_candidate()