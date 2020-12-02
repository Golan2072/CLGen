# clgen.py
# Cepheus Light character generator by Omer Golan-Joel
# v0.5 - August 10th, 2020
# This is open source code, feel free to use it for any purpose
# contact me at golan2072@gmail.com

# Import statements
import flask
from flask import request
import clgen_lib



app = flask.Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hello():
    # character death checkbox
    char_death = True
    char_death_check = ' checked="checked"'
    if 'allow_character_death' not in request.form:
        char_death = False
        char_death_check = ''

    # career choice
    random_choice_value = '__random__'

    career_choice = None
    if 'career_choice' in request.form:
        career_choice = request.form['career_choice']
        if career_choice == random_choice_value:
            career_choice = None

    options = '<option value="' + random_choice_value + '">Random</option>'
    for choice in clgen_lib.careers.keys():
        options += '<option value="' + choice + '"'
        if choice == career_choice:
            options += ' selected="selected"'
        options += '>' + choice + '</option>'

    character = clgen_lib.Character(death=char_death, career=career_choice)

    return '''
<html>
    <head>
        <title>Cepheus Light Character Generator</title>
    </head>
    <body>
    <h2>Cepheus Light Character Generator</h2>
    <hr>
    '''+ character.title + " " + character.name + " " + character.surname + "&nbsp;&nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp;&nbsp" + character.upp_string + "&nbsp;&nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp;&nbspAge: " + str(character.age) + " " + character.status + '''<br>
    '''+ str(character.terms) + " terms " + character.career + "; rank: " + clgen_lib.careers[character.career]['ranks'][character.rank] + "&nbsp;&nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp;&nbsp" + "Cash: " + str(character.cash) + '''
    <br><br>
    '''+ "Skills: " +  character.skill_string + '''<br><br>
    '''+ "Possessions: " +  character.possessions_string + '''<br>
    History: ''' + '; '.join(character.history) + '''

    <hr>
    <p>
      <form method="POST" action="/">
      Choose a career: <select name="career_choice">''' + options + '''</select><br>
      Allow character death?
      <input type="checkbox" name="allow_character_death"''' + char_death_check + '''><br>
      <input type="submit" value="Generate another">
      </form>
    </p>

 </body>
</html>'''

if __name__ == '__main__':
    app.run()
