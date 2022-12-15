import json

def load_candidates_from_json(path):
    with open(path, 'r', encoding="UTF-8") as file:
        return json.load(file)

candidates = load_candidates_from_json("candidates.json")

def get_candidate(candidate_id):
    candidate_id = int(candidate_id) - 1
    return candidates[candidate_id]

def get_candidates_by_name(candidate_name):
    for candidate in candidates:
        if candidate_name == candidate["name"]:
            return candidate

def get_candidates_by_skill(skill):
    dict_candidates = []
    for candidate in candidates:
        if skill.lower() in candidate["skills"].lower():
            dict_candidates.append(candidate)
    return dict_candidates
