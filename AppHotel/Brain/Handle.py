import sqlite3


class Handler:
    @staticmethod
    def key_autorization(login, passw):
        conn = sqlite3.connect('Gostiniza.db')
        cur = conn.cursor()

        cur.execute("SELECT * FROM Accounts WHERE username = ?", (login,))
        user_data = cur.fetchone()

        if user_data is not None:
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

    @staticmethod
    def key_check_user_type(login):
        conn = sqlite3.connect('Gostiniza.db')
        cur = conn.cursor()

        cur.execute("SELECT * FROM Accounts WHERE username = ?", (login,))
        user_data = cur.fetchone()

        if user_data is not None:
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

    @staticmethod
    def key_change_user_password(old_passw, new_passw, conf_new_passw):
        conn = sqlite3.connect('Gostiniza.db')
        cur = conn.cursor()

        cur.execute("SELECT * FROM Accounts WHERE password_hash = ?", (old_passw,))
        user_data = cur.fetchone()

        if user_data is not None:
            if old_passw == user_data[2]:
                if new_passw != old_passw:
                    if new_passw == conf_new_passw:
                        cur.execute("UPDATE Accounts SET password_hash = ? WHERE username = ?",
                                    (new_passw, user_data[1],))
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

    @staticmethod
    def key_add_new_user(username, passw, role):
        conn = sqlite3.connect('Gostiniza.db')
        cur = conn.cursor()

        if 3 < len(username) < 50:
            if len(passw) >= 8:
                if role == "admin" or role == "manager" or role == "staff" or role == "client":
                    cur.execute('INSERT INTO accounts (username, password_hash, role) VALUES (?, ?, ?)',
                                (username, passw, role,))
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

    @staticmethod
    def key_change_current_user(id, username, passw, role, status):
        conn = sqlite3.connect('Gostiniza.db')
        cur = conn.cursor()

        cur.execute("SELECT * FROM Accounts WHERE account_id = ?", (id,))
        if 3 < len(username) < 50:
            if len(passw) >= 8:
                if role == "admin" or role == "manager" or role == "staff" or role == "client":
                    cur.execute("UPDATE Accounts SET username = ?, password_hash = ?, role = ?, account_status = ? "
                                "WHERE account_id = ?", (username, passw, role, status, id,))
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

    @staticmethod
    def key_del_current_user(id):
        conn = sqlite3.connect('Gostiniza.db')
        cur = conn.cursor()

        cur.execute("DELETE FROM Accounts WHERE account_id = ?", (id,))
        cur.execute("SELECT * FROM Accounts ORDER BY account_id")
        all_accounts = cur.fetchall()
        cur.execute("DELETE FROM Accounts")
        for new_id, account in enumerate(all_accounts, start=1):
            cur.execute("INSERT INTO Accounts (account_id, username, password_hash, role, account_status, "
                        "login_attempts) VALUES (?, ?, ?, ?, ?, ?)", (new_id, *account[1:]))
            conn.commit()
        cur.close()
        conn.close()

    @staticmethod
    def key_del_current_client(id):
        conn = sqlite3.connect('Gostiniza.db')
        cur = conn.cursor()

        cur.execute("DELETE FROM Clients WHERE client_id = ?", (id,))
        cur.execute("SELECT * FROM Clients ORDER BY client_id")
        all_accounts = cur.fetchall()
        cur.execute("DELETE FROM Clients")
        for new_id, account in enumerate(all_accounts, start=1):
            cur.execute(
                "INSERT INTO Clients (client_id, account_id, first_name, last_name, phone_number, email) VALUES (?, "
                "?, ?, ?, ?,?)",
                (new_id, *account[1:]))
            conn.commit()
        cur.close()
        conn.close()
