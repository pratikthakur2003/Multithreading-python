import sqlite3
import threading
from typing import Dict, Any

class BaseModel:
    def __init__(self, db_name: str):
        self.db_name = db_name
        self.lock = threading.Lock()
        self._create_table()

    def _create_table(self):
        raise NotImplementedError

    def _get_connection(self):
        return sqlite3.connect(self.db_name)

    def validate(self, data: Dict[str, Any]) -> bool:
        raise NotImplementedError

class User(BaseModel):
    def __init__(self):
        super().__init__('users.db')

    def _create_table(self):
        with self._get_connection() as conn:
            conn.execute('DROP TABLE IF EXISTS users')
            conn.execute('''
                CREATE TABLE users (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    email TEXT
                )
            ''')
            print("Users table created successfully")

    def validate(self, data: Dict[str, Any]) -> bool:
        if not data.get('name'):
            print(f"Invalid name for user ID {data.get('id')}  (Name cannot be null)")
            return False
        
        if not data.get('email'):
            print(f"Invalid email for user ID {data.get('id')}")
            return False

        return True

    def insert(self, data: Dict[str, Any]):
        if not self.validate(data):
            return False

        with self.lock:
            try:
                with self._get_connection() as conn:
                    conn.execute(
                        'INSERT INTO users (id, name, email) VALUES (?, ?, ?)',
                        (data['id'], data['name'], data['email'])
                    )
                print(f"Inserted user: ID={data['id']}, Name={data['name']}, Email={data['email']}")
                return True
            except sqlite3.Error as e:
                print(f"Error inserting user {data['id']}: {e}")
                return False

class Product(BaseModel):
    def __init__(self):
        super().__init__('products.db')

    def _create_table(self):
        with self._get_connection() as conn:
            conn.execute('DROP TABLE IF EXISTS products')
            conn.execute('''
                CREATE TABLE products (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    price REAL
                )
            ''')
            print("Products table created successfully")

    def validate(self, data: Dict[str, Any]) -> bool:
        if not data.get('name'):
            print(f"Invalid name for product ID {data.get('id')}")
            return False

        if not isinstance(data.get('price'), (int, float)):
            print(f"Invalid price type for product ID {data.get('id')}")
            return False

        return True

    def insert(self, data: Dict[str, Any]):
        if not self.validate(data):
            return False

        with self.lock:
            try:
                with self._get_connection() as conn:
                    conn.execute(
                        'INSERT INTO products (id, name, price) VALUES (?, ?, ?)',
                        (data['id'], data['name'], data['price'])
                    )
                print(f"Inserted product: ID={data['id']}, Name={data['name']}, Price={data['price']}")
                return True
            except sqlite3.Error as e:
                print(f"Error inserting product {data['id']}: {e}")
                return False

class Order(BaseModel):
    def __init__(self):
        super().__init__('orders.db')

    def _create_table(self):
        with self._get_connection() as conn:
            conn.execute('DROP TABLE IF EXISTS orders')
            conn.execute('''
                CREATE TABLE orders (
                    id INTEGER PRIMARY KEY,
                    user_id INTEGER,
                    product_id INTEGER,
                    quantity INTEGER
                )
            ''')
            print("Orders table created successfully")

    def validate(self, data: Dict[str, Any]) -> bool:
        if not isinstance(data.get('user_id'), int):
            print(f"Invalid user_id for order ID {data.get('id')}")
            return False

        if not isinstance(data.get('product_id'), int):
            print(f"Invalid product_id for order ID {data.get('id')}")
            return False

        if not isinstance(data.get('quantity'), int):
            print(f"Invalid quantity for order ID {data.get('id')}")
            return False

        return True

    def insert(self, data: Dict[str, Any]):
        if not self.validate(data):
            return False

        with self.lock:
            try:
                with self._get_connection() as conn:
                    conn.execute(
                        'INSERT INTO orders (id, user_id, product_id, quantity) VALUES (?, ?, ?, ?)',
                        (data['id'], data['user_id'], data['product_id'], data['quantity'])
                    )
                print(f"Inserted order: ID={data['id']}, UserID={data['user_id']}, ProductID={data['product_id']}, Quantity={data['quantity']}")
                return True
            except sqlite3.Error as e:
                print(f"Error inserting order {data['id']}: {e}")
                return False
