from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#set up DB
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///books-collection.db"
db = SQLAlchemy(app)



#setting up DB table with columns for ID, Title, author and rating
class Book(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    author = db.Column(db.String(80), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Book {self.title}>'



@app.route('/')
def home():
    with app.app_context():
        all_books = db.session.query(Book).all()
    return render_template('index.html', all_books= all_books)

#render add page if GET req, if POST from form then add new book to DB
@app.route("/add", methods=['GET', 'POST'] )
def add():

    if request.method == 'POST':
        with app.app_context():
            db.create_all()
            book = Book(title= request.form['name'],
                        author= request.form['author'],
                        rating= request.form['rating']
                        )
            db.session.add(book)
            db.session.commit()
            all_books = db.session.query(Book).all()
        return redirect(url_for('home'))

    else:
        return render_template('add.html')

# if GET req, will present edit page with form, if POST req form then update rating by id
@app.route('/edit', methods=['GET', 'POST'])
def edit():

    if request.method == 'POST':
        book_id = request.form["id"]
        with app.app_context():
            book = Book.query.get(book_id)
            book.rating = request.form["rating"]
            db.session.commit()

        return redirect(url_for('home'))

    else:
        book_id = request.args.get('id')
        with app.app_context():
            book = Book.query.get(book_id)

        return render_template('edit.html', book=book)


#Delete a record by id
@app.route('/delete')
def delete():

    book_id = request.args.get('id')
    with app.app_context():
        book = Book.query.get(book_id)
        db.session.delete(book)
        db.session.commit()

    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)

