from flask import Flask, jsonify, request

app = Flask(__name__)
app.config["DEBUG"] = True

# Create some test data for our catalog in the form of a list of dictionaries
books = [
    {'id': 0, 'title': 'A Fire Upon the Deep', 'author': 'Vernor Vinge', 'first_sentence': 'The coldsleep itself was dreamless.', 'year_published': '1992'},
    {'id': 1, 'title': 'The Ones Who Walk Away From Omelas', 'author': 'Ursula K. Le Guin', 'first_sentence': 'With a clamor of bells that set the swallows soaring.', 'year_published': '1973'},
    {'id': 2, 'title': 'Dhalgren', 'author': 'Samuel R. Delany', 'first_sentence': 'To wound the autumnal city.', 'year_published': '1975'}
]

@app.route('/', methods=['GET'])
def home():
    return '''<h1>Distant Reading Archive</h1>
    <p>A prototype API for distant reading of science fiction novels.</p>'''

# Route to return all books
@app.route('/api/v1/resources/books/all', methods=['GET'])
def api_all():
    return jsonify(books)

# Route to filter books by id
@app.route('/api/v1/resources/books', methods=['GET'])
def api_book():
    book_id = request.args.get('id', type=int)
    if book_id is not None:
        filtered_books = [book for book in books if book['id'] == book_id]
        return jsonify(filtered_books)
    return jsonify(books)

if __name__ == '__main__':
    app.run(debug=True)
