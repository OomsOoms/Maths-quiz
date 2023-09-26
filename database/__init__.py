import sqlite3

class DatabaseManager:
    def __init__(self):
        # Establish a connection to the SQLite database
        self.conn = sqlite3.connect("database/database.db")
        self.cursor = self.conn.cursor()
        self.init_db()  # Ensure the database exists

    def init_db(self):
        # Create the 'users' table if it doesn't already exist
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                username TEXT PRIMARY KEY,
                total_score INTEGER
            )
        """)
        self.conn.commit()

    def check_username(self, username):
        # Check if the given username already exists in the 'users' table
        self.cursor.execute("SELECT username FROM users WHERE username = ?", (username,))
        result = self.cursor.fetchone()
        if result:
            return username
        else:
            # Prompt the user to add the username to the database
            add_to_db = input("Username does not exist. Do you want to add it to the database? (y/n): ")
            if add_to_db.lower() == 'y':
                # Insert the new username with an initial total score of 0
                self.cursor.execute("INSERT INTO users (username, total_score) VALUES (?, 0)", (username,))
                self.conn.commit()
                return username
            else:
                return None
            
    def update_score(self, score, username):
        # Update the total score for the given username
        self.cursor.execute("""
            UPDATE users
            SET total_score = total_score + ?
            WHERE username = ?
        """, (score, username))
        self.conn.commit()

    def select_total(self, username):
        # Retrieve the total score for the given username
        self.cursor.execute("""
            SELECT total_score
            FROM users
            WHERE username = ?
        """, (username,))
        return self.cursor.fetchone()[0]

# Create an instance of DatabaseManager at the module level
database_manager = DatabaseManager()
