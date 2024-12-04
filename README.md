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

## Output

![multithreading-python-output](https://github.com/user-attachments/assets/002391fa-1350-4640-af9f-7ad7417c73b5)

