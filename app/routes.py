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
    career_option = request.args.get("Career", None)
    career = []
    careerDefault = "Any"
    if career_option is not None:
        if career_option != "any":
            career = career_option
            careerDefault = career_option
    character = clgen_lib.Character(death, career)
    return render_template("index.html", title=character.title, name=character.name, surname=character.surname,
                           upp_string=character.upp_string, age=character.age, status=character.status,
                           career=character.career, rank_name=character.rank_name, terms=character.terms,
                           credits=character.cash, possessions=character.possessions_string,
                           skills=character.skill_string, homeworld=character.homeworld,
                           deathDefault=death, careerDefault=careerDefault)
    if request.args.get('generate') == 'Generate':
        return redirect(url_for('chargen', Death=death))
    else:
        pass


@app.route("/api")
def apiRoot():
    with open('./api.swagger', 'r') as f:
        data = f.read()
    return Response(data, mimetype='application/x-yml')

@app.route("/api/chargen")
def apiChargen():
    death = True
    darg = request.args.get("death", None)
    if darg is not None:
        if darg.lower() == "false":
            death = False
    print("death="+str(death))
    character = clgen_lib.Character(death)
    return Response(json.dumps(character.__dict__), mimetype='application/json')