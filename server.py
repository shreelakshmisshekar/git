from flask import Flask, render_template, request, redirect, url_for
from library_system import LibrarySystem

app = Flask(__name__)
library = LibrarySystem()

@app.route('/')
def home():
    return render_template('index.html', books=library.books)

@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        library.add_book(title, author)
        return redirect(url_for('home'))
    return render_template('add_book.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        title = request.form['title']
        books = library.search_book(title)
        return render_template('search_results.html', books=books)
    return render_template('search.html')

@app.route('/borrow/<int:book_id>')
def borrow_book(book_id):
    library.borrow_book(book_id)
    return redirect(url_for('home'))

@app.route('/return/<int:book_id>')
def return_book(book_id):
    library.return_book(book_id)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True) 