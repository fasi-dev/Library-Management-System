# Library Management System

A simple web-based Library Management System built with **Python (Flask)** and **MySQL**. It provides complete book-management (CRUD) functionality through a clean browser interface.

## ✨ Features

- View all books in a clean table
- Search books by title, author, or genre
- Add new books
- Edit existing books
- Delete books (with confirmation)
- Success / error feedback messages after every action
- Responsive layout that works on mobile and desktop
- MySQL persistence — the `books` table is created automatically on first run
- Database credentials via environment variables (no secrets in code)

## 🛠️ Technologies Used

| Layer | Technology |
| ----- | ---------- |
| Backend | Python 3, Flask |
| Database | MySQL (mysql-connector-python) |
| Frontend | HTML5, CSS3, Jinja2 templates |
| Production server | Gunicorn (see Deployment) |

## 📂 Project Structure

```text
Library-Management-System/
├── app.py               # Flask application (routes + DB logic)
├── schema.sql           # Optional SQL script (app auto-creates the table too)
├── requirements.txt     # Python dependencies
├── .env.example         # Example environment configuration
├── Procfile             # Start command for PaaS deployment
├── static/
│   └── style.css        # Stylesheet
└── templates/
    ├── base.html        # Layout: navbar, alerts, footer
    ├── index.html       # Book list + search
    ├── add_book.html    # Add book form
    └── edit_book.html   # Edit book form
```

## ⚙️ Setup & Installation

### 1. Prerequisites

- Python 3.9+
- MySQL Server running locally

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Create the database

```sql
CREATE DATABASE library_db;
```

(The `books` table is created automatically when the app starts. Alternatively you can run the provided `schema.sql`.)

### 4. Configure environment variables

The app reads its database credentials from environment variables:

| Variable | Description | Default |
| -------- | ----------- | ------- |
| `DB_HOST` | MySQL host | `localhost` |
| `DB_USER` | MySQL user | `root` |
| `DB_PASSWORD` | MySQL password | *(empty)* |
| `DB_NAME` | Database name | `library_db` |
| `SECRET_KEY` | Flask session key | dev value |

See `.env.example` for a template. **Never commit real passwords to GitHub.**

### 5. Run the app

```bash
python app.py
```

Then open http://127.0.0.1:5000 in your browser.

## 📖 Usage

- **View books** — the home page lists every book.
- **Search** — use the search bar to filter by title, author, or genre.
- **Add a book** — click **+ Add Book**, fill in the form, and submit.
- **Edit a book** — click **Edit** on a row, change the details, and save.
- **Delete a book** — click **Delete** and confirm.

## 📸 Screenshots

> Add screenshots here after running the app, e.g.:
>
> - `screenshots/home.png` — book list with search
> - `screenshots/add.png` — add book form

## 🚀 Deployment

The app is deployment-ready: it uses environment variables for configuration and ships a `Procfile` for Gunicorn. The simplest hosting route for a **Flask + MySQL** project is a platform that offers both in one place, e.g. **Railway**:

1. Push this repository to GitHub (done).
2. On Railway, create a new project → **Deploy from GitHub repo**.
3. Add a **MySQL** service to the same project.
4. Set the environment variables (`DB_HOST`, `DB_USER`, `DB_PASSWORD`, `DB_NAME`) using the credentials Railway provides for the MySQL service.
5. Deploy — Railway installs `requirements.txt` and starts the app with the `Procfile`.

(Render + a hosted MySQL provider such as Aiven works the same way.)

## 🔮 Future Improvements

- Member management and book issue/return tracking
- Pagination for large libraries
- User authentication

## 👤 Author

**Mohammed Fasiuddin** — [github.com/fasi-dev](https://github.com/fasi-dev)
