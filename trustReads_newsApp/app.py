import flask
from find_related_urls import find_related_urls
app = flask.Flask(__name__, template_folder='templates')
@app.route('/', methods=['GET', 'POST'])
def main():
    if flask.request.method == 'GET':
        return(flask.render_template('main.html'))
    if flask.request.method == 'POST':
        query = flask.request.form['query']
        links = find_related_urls(query)
        return flask.render_template('main.html',
                                     original_input={'query':query},
                                     len = len(links),result= links, 
                                     )