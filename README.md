# SplitSmart

SplitSmart is a small Flask-based web application used to track shared expenses between roommates. It was created as the final project for SDEV‑220 (Team C).

## Features

- Web form built with HTML and vanilla JavaScript
- Input validation on the client side
- `/add_expense` API route stores rent and grocery costs in an SQLite database
- `/get_expenses` API route returns a JSON list of saved expenses

## Directory overview

- `app.py` – Flask routes and server configuration
- `data/` – SQLite schema and helper functions (`db.py`)
- `templates/` – HTML interface (`index.html`)
- `static/` – basic stylesheet
- `classes/` – placeholder modules for future object‑oriented design

## Installation

1. (Optional) Create a virtual environment
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```
2. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```
3. Initialize the database
   ```bash
   flask --app app.py init-db
   ```
4. Run the development server
   ```bash
   flask --app app.py run -p 3000
   ```

Open <http://localhost:3000> in your browser to access the app.

## Usage example

Enter the names of up to four roommates and specify the rent and grocery totals. Click **Add Bill** to save the expenses or **View Debts** to retrieve everything stored in the database.

The repository includes a sample `data/database` file for convenience. You can delete it and run the `init-db` command to start fresh.


## Team Contributions

- **Edward Clark (Project Manager & Backend Developer)**  
  Led development and planning. Built and tested all backend Flask routes including `/add_expense`, `/get_expenses`, and `/get_balances`. Integrated form inputs with SQLite, connected frontend to backend, managed GitHub repository, and ensured project completion.

- **Emma (Frontend Developer)**  
  Built the HTML form layout and JavaScript functions for validating user input and submitting expenses. Implemented the initial structure of the Add Bill and View Debts functionality and styled the user interface.

- **Matt (Backend Developer)**  
  Assisted with backend database logic and route handling.

- **Zane (Data Handler)**  
  Managed JSON data or database layer.

## Sample output

The `/get_expenses` endpoint returns JSON similar to the following:

```json
[
    {"id": 1, "description": "Rent", "amount": 999.0},
    {"id": 2, "description": "Groceries", "amount": 999.0},
    {"id": 3, "description": "Rent", "amount": 843.0},
    {"id": 4, "description": "Groceries", "amount": 838.0}
]
```
