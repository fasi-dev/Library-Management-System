# Library Management System

A simple web-based Library Management System built with **Python Flask and MySQL**. The application provides basic book management functionality through a clean browser-based interface.

## Features

* Add new books
* View all books
* Search and manage book records
* Edit existing books
* Delete books
* Store book information in MySQL
* Basic form validation
* Clean and responsive web interface
* Persistent database storage

## Technologies Used

* **Python 3**
* **Flask**
* **MySQL**
* **HTML5**
* **CSS3**
* **mysql-connector-python**

## Project Structure

```text
Library-Management-System/
│
├── app.py
├── requirements.txt
│
├── static/
│   └── style.css
│
└── templates/
    ├── index.html
    ├── add_book.html
    └── edit_book.html
```

## Database

The application uses a MySQL database named:

```text
library_db
```

The main table used by the current application is:

```text
books
```

The book records contain information such as:

* Book ID
* Title
* Author
* Genre

## Requirements

Make sure the following are installed:

* Python 3
* MySQL Server
* pip

Install the Python dependencies:

```bash
pip install -r requirements.txt
```

## Database Setup

1. Start your MySQL server.
2. Create the database:

```sql
CREATE DATABASE library_db;
```

3. Make sure the MySQL username and password configured for the application are correct.
4. Ensure the `books` table exists with the columns expected by `app.py`.

## Running the Application

Open a terminal in the project directory:

```bash
python app.py
```

The Flask development server will start at:

```text
http://127.0.0.1:5000
```

Open that address in your browser.

## Basic Usage

### Add a Book

Open the **Add Book** page and enter the book title, author, and genre.

### View Books

The home page displays the books stored in the database.

### Edit a Book

Select a book and use the **Edit** option to update its information.

### Delete a Book

Use the **Delete** option to remove a book from the database.


Example:

```text
![Home Page](screenshots/home.png)
```

## Future Improvements

Possible future improvements include:

* Member management
* Book issue and return tracking
* Improved search and filtering
* User authentication
* Better database configuration through environment variables
* Deployment to a cloud platform

## Deployment

The application can be deployed using a Flask-compatible hosting platform together with a hosted MySQL database.

For local development, the application is intended to run using Flask's development server.

## Author

**Mohammed Fasiuddin**

GitHub: [fasi-dev](https://github.com/fasi-dev)
