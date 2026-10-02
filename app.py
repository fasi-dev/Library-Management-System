import os

from flask import Flask, flash, redirect, render_template, request
import mysql.connector

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "dev-secret-key")

# Database configuration.
# Credentials are read from environment variables so that no secrets
# are stored in the code. The defaults work for a local MySQL setup.
DB_CONFIG = {
    "host": os.environ.get("DB_HOST", "localhost"),
    "user": os.environ.get("DB_USER", "root"),
    "password": os.environ.get("DB_PASSWORD", ""),
    "database": os.environ.get("DB_NAME", "library_db"),
}


def get_connection():
    """Open a new connection to the MySQL database."""
    return mysql.connector.connect(**DB_CONFIG)


def init_db():
    """Create the books table if it does not exist yet."""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS books (
            id INT AUTO_INCREMENT PRIMARY KEY,
            title VARCHAR(255) NOT NULL,
            author VARCHAR(255) NOT NULL,
            genre VARCHAR(100)
        )
        """
    )
    conn.commit()
    cur.close()
    conn.close()


@app.route("/")
def home():
    search = request.args.get("q", "").strip()

    conn = get_connection()
    cur = conn.cursor()
    if search:
        like = f"%{search}%"
        cur.execute(
            "SELECT * FROM books WHERE title LIKE %s OR author LIKE %s OR genre LIKE %s ORDER BY id",
            (like, like, like),
        )
    else:
        cur.execute("SELECT * FROM books ORDER BY id")
    books = cur.fetchall()
    cur.close()
    conn.close()

    return render_template("index.html", books=books, search=search)


@app.route("/add", methods=["GET", "POST"])
def add_book():
    if request.method == "POST":
        title = request.form["title"].strip()
        author = request.form["author"].strip()
        genre = request.form["genre"].strip()

        conn = get_connection()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO books (title, author, genre) VALUES (%s, %s, %s)",
            (title, author, genre),
        )
        conn.commit()
        cur.close()
        conn.close()

        flash(f'"{title}" was added to the library.', "success")
        return redirect("/")

    return render_template("add_book.html")


@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_book(id):
    conn = get_connection()
    cur = conn.cursor()

    if request.method == "POST":
        title = request.form["title"].strip()
        author = request.form["author"].strip()
        genre = request.form["genre"].strip()

        cur.execute(
            "UPDATE books SET title=%s, author=%s, genre=%s WHERE id=%s",
            (title, author, genre, id),
        )
        conn.commit()
        cur.close()
        conn.close()

        flash("Book details updated.", "success")
        return redirect("/")

    cur.execute("SELECT * FROM books WHERE id = %s", (id,))
    book = cur.fetchone()
    cur.close()
    conn.close()

    if book is None:
        flash("Book not found.", "error")
        return redirect("/")

    return render_template("edit_book.html", book=book)


@app.route("/delete/<int:id>")
def delete_book(id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM books WHERE id = %s", (id,))
    conn.commit()
    deleted = cur.rowcount
    cur.close()
    conn.close()

    if deleted:
        flash("Book deleted.", "success")
    else:
        flash("Book not found.", "error")
    return redirect("/")


# Create the table on startup (works for both `python app.py` and gunicorn).
init_db()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=True)
