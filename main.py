from flask import Flask, render_template
from utils import load_candidates_from_json, get_candidate, get_candidates_by_name, get_candidates_by_skill

app = Flask(__name__)

@app.route("/")
def index():
    candidates = load_candidates_from_json("candidates.json")
    return render_template('list.html', candidates=candidates)

@app.route("/candidate/<candidate_id>")
def get_candidate_(candidate_id):
    candidates = get_candidate(candidate_id)
    return render_template('card.html', candidates=candidates)

@app.route("/search/<candidate_name>")
def get_candidates_by_name_(candidate_name):
    candidates = get_candidates_by_name(candidate_name)
    number = len(get_candidates_by_name(candidate_name))
    return render_template('search.html', candidates=candidates, number=number)

@app.route("/skill/<skill_name>")
def get_candidates_by_skill_(skill_name):
    candidates = get_candidates_by_skill(skill_name)
    number = len(get_candidates_by_skill(skill_name))
    return render_template('skill.html', candidates=candidates, number=number, skill=skill_name)

if __name__ == '__main__':
    app.run(debug=True)
