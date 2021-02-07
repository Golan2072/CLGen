from flask import Flask, request, render_template
from app import app
import clgen_lib

@app.route("/")
def index():
        character = clgen_lib.Character()
        return render_template("index.html", title = character.title, name = character.name, surname = character.surname, upp_string = character.upp_string, age = character.age, status = character.status, career = character.career, rank_name = character.rank_name, terms = character.terms, credits = character.cash, possessions = character.possessions_string, skills = character.skill_string)
