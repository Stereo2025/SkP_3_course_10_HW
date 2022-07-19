from flask import Flask
from utils import get_all_candidates, get_candidates_by_pk, get_candidate_by_skill


app = Flask(__name__)


@app.route("/")
def show_all_candidates():
    """Показывает всех кандидатов на главной страничке"""
    return get_all_candidates()


@app.route("/candidates/<int:pk>")
def show_candidate_by_key(pk) -> str:
    """Показывает кандидата на страничке /candidates/ по номеру кандидата"""
    return get_candidates_by_pk(pk)


@app.route('/skill/<uid>')
def show_candidate_by_skill(uid) -> str:
    """Показывает кандидата на страничке /skill/ по введённому навыку"""
    return get_candidate_by_skill(uid)


if __name__ == '__main__':
    app.run(debug=True)
###########################################################################
