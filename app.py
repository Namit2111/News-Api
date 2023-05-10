# pylint: disable=C0103, C0111, R0914

'''
Main server file returning the news dictionary from inshorts file as JSON Object
'''

from flask import Flask, request, jsonify
from scraper import getNews
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return ('''
    <h3>usage : www.host.com/news?category={category name}</h3>  <br><br>
    <h4>Categories available</h4> 
    <b>       
    1. '' //leave blank for top news<br>
    2. national <br>
    3. business<br>
    4. sports<br>
    5. world<br>
    6. politics<br>
    7. technology<br>
    8. startup<br>
    9. entertainment<br>
    10. miscellaneous<br>
    11. hatke <br>
    12. science<br>
    13. automobile</b><br>
''')




@app.route('/news', methods=['GET', 'POST'])

def news():
    if request.method == 'POST':
        return jsonify(getNews(request.form['category']))
    elif request.method == 'GET':
        return jsonify(getNews(request.args.get('category')))


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0',port=5000,use_reloader=True)