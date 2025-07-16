DROP TABLE IF EXISTS expense;
DROP TABLE IF EXISTS roommate;
DROP TABLE IF EXISTS household;
DROP TABLE IF EXISTS tracker;

CREATE TABLE tracker (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL
);

CREATE TABLE household (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL,
    tracker_id INTEGER NOT NULL,
    FOREIGN KEY (tracker_id) REFERENCES tracker (id)
);

CREATE TABLE roommate (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL,
    tracker_id INTEGER NOT NULL,
    FOREIGN KEY (tracker_id) REFERENCES tracker (id)
);

CREATE TABLE expense (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    amount REAL NOT NULL,
    description TEXT NOT NULL,
    tracker_id INTEGER NOT NULL,
    roommate_id INTEGER NOT NULL,
    FOREIGN KEY (tracker_id) REFERENCES tracker (id),
    FOREIGN KEY (roommate_id) REFERENCES roommate (id)
);