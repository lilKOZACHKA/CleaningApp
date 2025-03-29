import sqlite3, sys
import AuthWindow

class Handler():
    def key_autorization(handler, login, passw):
        conn = sqlite3.connect('database.db')
        cur = conn.cursor()

        cur.execute("SELECT * FROM Accounts WHERE username = ?", (login,))
        user_data = cur.fetchone()

        if user_data != None:
            if user_data[5] >= 3:
                cur.execute("UPDATE Accounts SET account_status = ? WHERE username = ?", ("Забаннен", login,))
                conn.commit()
                cur.close()
                conn.close()
                return 2
            elif user_data[2] == passw:
                cur.execute("UPDATE Accounts SET login_attempts = ? WHERE username = ?", (0, login,))
                conn.commit()
                cur.close()
                conn.close()
                return 0
            else:  
                cur.execute("UPDATE Accounts SET login_attempts = ? WHERE username = ?", (user_data[5] + 1, login,))
                conn.commit()
                cur.close()
                conn.close()
                return 1
        cur.close()
        conn.close()
        return 1
    
    def key_check_user_type(handler, login):
        conn = sqlite3.connect('database.db')
        cur = conn.cursor()

        cur.execute("SELECT * FROM Accounts WHERE username = ?", (login,))
        user_data = cur.fetchone()

        if user_data != None:
            if user_data[3] == "admin":
                cur.close()
                conn.close()
                return 0
            if user_data[3] == "client":
                cur.close()
                conn.close()
                return 1
        cur.close()
        conn.close()
        return 2
            
    def key_change_user_password(handler, old_passw, new_passw, conf_new_passw):
        conn = sqlite3.connect('database.db')
        cur = conn.cursor()

        cur.execute("SELECT * FROM Accounts WHERE password_hash = ?", (old_passw,))
        user_data = cur.fetchone()

        if user_data != None:
            if old_passw == user_data[2]:
                if new_passw != old_passw:
                    if new_passw == conf_new_passw:
                        cur.execute("UPDATE Accounts SET password_hash = ? WHERE username = ?", (new_passw, user_data[1],))
                        conn.commit()
                        cur.close()
                        conn.close()
                        return 1
                    else:
                        cur.close()
                        conn.close()
                        return 2
                else:
                    cur.close()
                    conn.close()
                    return 2
            else:
                cur.close()
                conn.close()
                return 3
        else:
            cur.close()
            conn.close()
            
    
    def key_add_new_user(handler, username, passw, role):
        conn = sqlite3.connect('database.db')
        cur = conn.cursor()

        if len(username) > 3 and len(username) < 50:
            if len(passw) >= 8:
                if role == "admin" or role == "manager" or role == "staff" or role == "client":
                    cur.execute("INSERT INTO accounts (username, password_hash, role) VALUES (?, ?, ?)", (username, passw, role,))
                    conn.commit()
                    cur.close()
                    conn.close()
                    return 0
                else:
                    return 1
            else:
                return 2
        else:
            return 3





    