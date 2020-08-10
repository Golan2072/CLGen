# clgen.py
# Cepheus Light character generator by Omer Golan-Joel
# v0.5 - August 10th, 2020
# This is open source code, feel free to use it for any purpose
# contact me at golan2072@gmail.com

# Import statements
import flask
import clgen_lib

character = clgen_lib.Character()


app = flask.Flask(__name__)


@app.route('/')
def hello():
    return '''
<html>
    <head>
        <title>Cepheus Light Character Generator</title>
    </head>
    <body>
    <h2>Cepheus Light Character Generator</h2>
    <hr>
    '''+ character.title + " " + character.name + " " + character.surname + "&nbsp;&nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp;&nbsp" + character.upp_string + "&nbsp;&nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp;&nbspAge: " + str(character.age) + " " + character.status + '''<br>
    '''+ str(character.terms) + " terms " + character.career + " " + clgen_lib.careers[character.career]['ranks'][character.rank] + "&nbsp;&nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp;&nbsp" + "Cash:" + str(character.cash) + '''
    <br><br>
    '''+ "Skills: " +  character.skill_string + '''<br><br>
    '''+ "Possessions: " +  character.possessions_string + '''<br>
    
 </body>
</html>'''

if __name__ == '__main__':
    app.run()