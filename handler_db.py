import sqlite3, sys, main

class Handler():
    def key_check_autorization(xz, login, passw):
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
    