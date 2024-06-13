#!/usr/bin/python3
""" script that starts a Flask web application """
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City


app = Flask(__name__)


@app.route("/states", strict_slashes=False)
@app.route("/states/<id>", strict_slashes=False)
def list_states(id=None):
    """ Displays a HTML page with a list of states or cities of a state """
    states = storage.all(State).values()
    if id:
        state = None
        for st in states:
            if st.id == id:
                state = st
                break
        if state:
            return render_template('9-states.html', state=state)
        else:
            return render_template('9-states.html', not_found=True)
    else:
        states = sorted(states, key=lambda state: state.name)
        return render_template('9-states.html', states=states)


@app.teardown_appcontext
def teardown(exception):
    """ closes the current session """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

