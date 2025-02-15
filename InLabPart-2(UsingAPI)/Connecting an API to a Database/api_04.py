import flask
from flask import Flask, request, jsonify

app = Flask(__name__)
app.config["DEBUG"] = True

# Create some test data for our catalog in the form of a list of dictionaries
albums = [
    {'id': 0, 'title': 'Jagged Little Pill', 'artist': 'Alanis Morissette'},
    {'id': 1, 'title': 'For Those About To Rock We Salute You', 'artist': 'AC/DC'},
    {'id': 2, 'title': 'Restless and Wild', 'artist': 'Accept'},
    {'id': 3, 'title': 'Let There Be Rock', 'artist': 'AC/DC'}
]

# Route to return albums filtered by title
@app.route('/api/v1/resources/albums', methods=['GET'])
def get_albums():
    title = request.args.get('title')  # Get title from query string
    if title:
        filtered_albums = [album for album in albums if title.lower() in album['title'].lower()]
        return jsonify(filtered_albums)
    return jsonify(albums)

# Route for home
@app.route('/', methods=['GET'])
def home():
    return '''<h1>Accessing Chinook Database</h1>
    <p>A prototype API for accessing the Chinook SQLite database.</p>'''

@app.errorhandler(404)
def page_not_found(e):
    return '''<h1>404</h1><p>The resource could not be found.</p>''', 404

if __name__ == '__main__':
    app.run(debug=True)

