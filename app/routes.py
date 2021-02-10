from flask import render_template, request, url_for, Response
from werkzeug.utils import redirect
import json

from app import app
import clgen_lib

@app.route("/")
def chargen():

    death_toggle = request.args.get("Death", 'None Selected')
    death = False
    if death_toggle == "Death":
        death = True
    elif death_toggle == "Life":
        death = False
    character = clgen_lib.Character(death)
    return render_template("index.html", title=character.title, name=character.name, surname=character.surname,
                           upp_string=character.upp_string, age=character.age, status=character.status,
                           career=character.career, rank_name=character.rank_name, terms=character.terms,
                           credits=character.cash, possessions=character.possessions_string,
                           skills=character.skill_string,
                           deathDefault=death)
    if request.args.get('generate') == 'Generate':
        return redirect(url_for('chargen', Death=death))
    else:
        pass
