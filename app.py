from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="~Fasi@#125",
    database="library_db"
)

cursor = db.cursor()

@app.route('/')
def home():
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()
    return render_template("index.html", books=books)

@app.route('/add', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        genre = request.form['genre']

        cursor.execute(
            "INSERT INTO books (title, author, genre) VALUES (%s, %s, %s)",
            (title, author, genre)
        )
        db.commit()

        return redirect('/')

    return render_template("add_book.html")

@app.route('/delete/<int:id>')
def delete_book(id):
    cursor.execute("DELETE FROM books WHERE id = %s", (id,))
    db.commit()
    return redirect('/')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_book(id):
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        genre = request.form['genre']

        cursor.execute(
            "UPDATE books SET title=%s, author=%s, genre=%s WHERE id=%s",
            (title, author, genre, id)
        )
        db.commit()
        return redirect('/')

    cursor.execute("SELECT * FROM books WHERE id = %s", (id,))
    book = cursor.fetchone()
    return render_template("edit_book.html", book=book)

if __name__ == '__main__':
    app.run(debug=True)