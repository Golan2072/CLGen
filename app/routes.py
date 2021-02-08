from flask import Flask, request, render_template, url_for
from werkzeug.utils import redirect
from app import app
import clgen_lib

@app.route("/")
def chargen():
    death = True
    character = clgen_lib.Character(death)
    return render_template("index.html", title=character.title, name=character.name, surname=character.surname,
                           upp_string=character.upp_string, age=character.age, status=character.status,
                           career=character.career, rank_name=character.rank_name, terms=character.terms,
                           credits=character.cash, possessions=character.possessions_string,
                           skills=character.skill_string)
    if request.form['submit'] == 'Generate':
        death_toggle = request.form.get("Death")
        if death_toggle == "Death":
            death = True
        elif death_toggle == "Life":
            death = False
        return redirect(url_for('/'), death)

