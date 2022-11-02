from flask import Flask, render_template
from utils import get_all, get_by_id, get_by_name, get_by_skill

app = Flask(__name__)

@app.route('/')
def index():
    candidates = get_all()
    return render_template('list.html', candidates=candidates)

@app.route('/candidates/<int:id>')
def get_candidate(id):
    candidate = get_by_id(id)
    return render_template('candidate.html', candidate=candidate)

@app.route('/search/<candidate_name>')
def search_by_name(candidate_name):
    candidates = get_by_name(candidate_name)
    return render_template('search.html', candidates=candidates)

@app.route('/skill/<skill_name>')
def search_by_skill(skill_name):
    candidates = get_by_skill(skill_name)
    count = len(candidates)
    return render_template('skill.html', candidates=candidates, skill=skill_name, count=count)

app.run(host='127.0.0.1', port='5000')
