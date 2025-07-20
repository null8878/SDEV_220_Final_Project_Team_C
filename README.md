# SplitSmart

This project is a simple Flask application designed to track shared household expenses. It was developed as the final project for SDEV-220 (Team C).

## Requirements

- Python 3
- Flask (see `requirements.txt`)

## Setup

1. Create and activate a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Initialize the SQLite database:
   ```bash
   flask --app app.py init-db
   ```
4. Run the development server:
   ```bash
   flask --app app.py run -p 3000
   ```

Navigate to `http://localhost:3000` in your browser to use the app.

## Project Structure

- `app.py` – main Flask application.
- `data/` – database helpers and schema.
- `templates/` – HTML templates.
- `static/` – CSS styles.
- `classes/` – placeholder Python modules for future expansion.

## Usage

Use the web form on the homepage to add rent and grocery expenses for up to four roommates. The "View Debts" button retrieves stored expenses from the database.

