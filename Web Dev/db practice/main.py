from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# db = sqlite3.connect("books-collection.db")
# cursor = db.cursor()
#
# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"
db = SQLAlchemy(app)




class Book(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    author = db.Column(db.String(80), unique=True, nullable=False)
    rating = db.Column(db.Float, unique=True, nullable=False)

    def __repr__(self):
        return f'<Book {self.title}>'

if __name__ == "__main__":
    app.run(debug=True)
    with app.app_context():
        db.create_all()
        hp = Book(id=1, title='Harry Potter', author="J. K. Rowling", rating=9.3)
        db.session.add(hp)
        db.session.commit()


