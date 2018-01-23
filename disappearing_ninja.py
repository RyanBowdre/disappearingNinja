
from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route('/')
def no_ninjas_here():
    return render_template('no_ninjas_here.html')

@app.route('/ninja', methods = ['POST'])
def ninjas():
    return render_template('allFourNinjas.html')

@app.route('/find_ninja', methods = ['POST'])
def ninja_color():
    color = request.form['text']
    if color == "blue" or color == "BLUE":
        return render_template('blue_ninja.html')
    elif color == "red" or color == "RED":
        return render_template('red_ninja.html')
    elif color == "purple" or color == "PURPLE":
        return render_template('purple_ninja.html')
    elif color == "orange" or color == "ORANGE":
        return render_template('orange_ninja.html')
    else:
        return render_template('not_april.html')

app.run(debug=True)


#
# @app.route('/result', methods=['POST'])
# def create_user():
#       print "Got Post Info"
#       first = request.form['first_name']
#       last = request.form['last_name']
#       desc = request.form['description']
#     #   option = request.form['option']
#       print first, last
#       return render_template('results.html', first_name=first, last_name=last, description=desc)
#
# # @app.route('/')
