import sqlite3, sys
import AppHotel.Main.Gostiniza

class Handler():
    def key_autorization(handler, login, passw):
        conn = sqlite3.connect('Guest.db')
        cur = conn.cursor()

        cur.execute("SELECT * FROM Accounts WHERE username = ?", (login,))
        user_data = cur.fetchone()

        if user_data != None:
            if user_data[5] >= 3:
                cur.execute("UPDATE Accounts SET account_status = ? WHERE username = ?", ("Забанен", login,))
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
        conn = sqlite3.connect('Guest.db')
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
        conn = sqlite3.connect('Guest.db')
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
        conn = sqlite3.connect('Guest.db')
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
        
    def key_change_current_user(handler, id, username, passw, role, status):
        conn = sqlite3.connect('Guest.db')
        cur = conn.cursor()

        cur.execute("SELECT * FROM Accounts WHERE account_id = ?", (id,))
        user_data = cur.fetchone()

        if len(username) > 3 and len(username) < 50:
            if len(passw) >= 8:
                if role == "admin" or role == "manager" or role == "staff" or role == "client": 
                    cur.execute("UPDATE Accounts SET username = ?, password_hash = ?, role = ?, account_status = ? WHERE account_id = ?", (username, passw, role, status, id,))
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
        
    def key_del_current_user(handler, id):
        conn = sqlite3.connect('Guest.db')
        cur = conn.cursor()

        cur.execute("DELETE FROM Accounts WHERE account_id = ?", (id,))
        cur.execute("SELECT * FROM Accounts ORDER BY account_id")
        all_accounts = cur.fetchall()
        cur.execute("DELETE FROM Accounts")
        for new_id, account in enumerate(all_accounts, start=1):
            cur.execute("INSERT INTO Accounts (account_id, username, password_hash, role, account_status, login_attempts) VALUES (?, ?, ?, ?, ?, ?)", (new_id, *account[1:]))
            conn.commit()
        cur.close()
        conn.close()

    def key_del_current_client(handler, id):
        conn = sqlite3.connect('Guest.db')
        cur = conn.cursor()

        cur.execute("DELETE FROM Clients WHERE client_id = ?", (id,))
        cur.execute("SELECT * FROM Clients ORDER BY client_id")
        all_accounts = cur.fetchall()
        cur.execute("DELETE FROM Clients")
        for new_id, account in enumerate(all_accounts, start=1):
            cur.execute(
                "INSERT INTO Clients (client_id, account_id, first_name, last_name, phone_number, email) VALUES (?, ?, ?, ?, ?,?)",
                (new_id, *account[1:]))
            conn.commit()
        cur.close()
        conn.close()


    