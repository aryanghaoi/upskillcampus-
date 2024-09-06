import sqlite3

def init_db():
    conn = sqlite3.connect("passwords.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS passwords 
                      (service TEXT PRIMARY KEY, encrypted_password BLOB)''')
    conn.commit()
    conn.close()

def save_password(service, encrypted_password):
    conn = sqlite3.connect("passwords.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO passwords (service, encrypted_password) VALUES (?, ?)", (service, encrypted_password))
    conn.commit()
    conn.close()

def get_password(service):
    conn = sqlite3.connect("passwords.db")
    cursor = conn.cursor()
    cursor.execute("SELECT encrypted_password FROM passwords WHERE service = ?", (service,))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else None

def update_password(service, encrypted_password):
    conn = sqlite3.connect("passwords.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE passwords SET encrypted_password = ? WHERE service = ?", (encrypted_password, service))
    conn.commit()
    conn.close()

def delete_password(service):
    conn = sqlite3.connect("passwords.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM passwords WHERE service = ?", (service,))
    conn.commit()
    conn.close()
