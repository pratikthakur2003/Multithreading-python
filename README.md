# Multi-threaded SQLite Database Operations

A Python program that demonstrates concurrent database operations using multiple SQLite databases and threading.

## Project Structure

- `models.py`: Contains the database models (Users, Products, Orders)
- `main.py`: Main program that runs concurrent insertions
- `requirements.txt`: Project dependencies

## Database Models

### Users (users.db)
- id: Primary Key
- name: Text
- email: Text

### Products (products.db)
- id: Primary Key
- name: Text
- price: Real

### Orders (orders.db)
- id: Primary Key
- user_id: Integer
- product_id: Integer
- quantity: Integer

## Features

- Separate SQLite databases for each model
- Concurrent insertions using Python threading
- Basic data validation
- Thread-safe database operations

## Running the Program

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the program:
```bash
python main.py
```

The program will create the databases, tables, and perform concurrent insertions of sample data.
