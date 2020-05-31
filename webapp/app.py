import flask
def find_related_urls(title):
    """
    args: title of article
    returns: links of  most related articles from trusted sources
    """
    try: 
        from googlesearch import search 
    except ImportError:  
        print("No module named 'google' found")  
    print(title)
    st = " "
    related_urls = []
    # to search 
    query1 = "ndtv: "+ title
    query2 = "timesofindia: "+title
    query3 = "hindustantimes: " + title
    for q in search(query1, tld="com", num=10, stop=1, pause=2): 
        st += q
        st += "\n"
        
    for r in search(query2, tld="co.in", num=10, stop=1, pause=2): 
        st += r
        st += "\n"
    for s in search(query3, tld="com", num=10, stop=1, pause=2): 
        st += s
        st += "\n"
    return st
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
                                     result= links,
                                     )