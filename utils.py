import json

def load_candidates(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.loads(f.read())

def get_all():
    candidates = load_candidates('candidates.json')
    return candidates

def get_by_id(id):
    candidates = load_candidates('candidates.json')
    for candidate in candidates:
        if id == candidate['id']:
            return candidate

def get_by_name(name):
    candidates = load_candidates('candidates.json')
    names = []
    for candidate in candidates:
        if name.lower() in candidate['name'].lower():
            names.append({'name': candidate['name'], 'id': candidate['id']})
    return names

def get_by_skill(skill_name):
    candidates_with_skill = []
    candidates = load_candidates('candidates.json')
    for candidate in candidates:
        if skill_name.lower() in candidate['skills'].lower():
            candidates_with_skill.append({'name': candidate['name'], 'id': candidate['id']})
    return candidates_with_skill
