import mysql.connector

def connect_db():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='varun',
        database='quiz_game'
    )

def load_q():
    q = {}
    conn = connect_db()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM questions")
    rows = cursor.fetchall()
    for row in rows:
        t = row['topic']
        if t not in q:
            q[t] = []
        q[t].append({
            "q": row['question'],
            "o": [row['option1'], row['option2'], row['option3'], row['option4']],
            "a": row['answer']
        })
    conn.close()
    return q

def load_u():
    u = {}
    conn = connect_db()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    for row in rows:
        u[row['username']] = row['password']
    conn.close()
    return u

def load_r():
    r = {}
    conn = connect_db()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM results")
    rows = cursor.fetchall()
    for row in rows:
        un = row['username']
        t = row['topic']
        s = int(row['score'])
        if un not in r:
            r[un] = {}
        r[un][t] = s
    conn.close()
    return r

def save_u(u):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users")
    for un, p in u.items():
        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (un, p))
    conn.commit()
    conn.close()

def save_r(r):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM results")
    for un, t in r.items():
        for topic, s in t.items():
            cursor.execute("INSERT INTO results (username, topic, score) VALUES (%s, %s, %s)", (un, topic, s))
    conn.commit()
    conn.close()

def reg(u):
    un = input("Enter username: ")
    if un in u:
        print("Username already exists!")
        return
    p = input("Enter a password: ")
    u[un] = p
    print("Registration successful!")
    save_u(u)

def log(u):
    un = input("Enter username: ")
    p = input("Enter password: ")
    if un in u and u[un] == p:
        print("Login successful!")
        return True, un
    else:
        print("Invalid username or password!")
        return False, None

def tq(t, un, q, r):
    if t not in q:
        print("Invalid topic!")
        return 0
    s = 0
    for x in q[t]:
        print(f"\n{x['q']}")
        for i, o in enumerate(x['o']):
            print(f"{i + 1}. {o}")
        a = input("Your answer (1-4): ")
        if x['o'][int(a) - 1] == x['a']:
            s += 1
    if un not in r:
        r[un] = {}
    r[un][t] = s
    save_r(r)
    return s

def main():
    u = load_u()
    r = load_r()
    q = load_q()
    
    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Exit")
        ch = input("Choose an option: ")
        if ch == "1":
            reg(u)
        elif ch == "2":
            li, un = log(u)
            if li:
                while True:
                    print("\n1. Take Quiz")
                    print("2. Show Result")
                    print("3. Logout")
                    opt = input("Choose an option: ")
                    if opt == "1":
                        print("Choose a topic: DSA, DBMS, Python")
                        t = input("Your choice: ")
                        s = tq(t, un, q, r)
                        print(f"Your score: {s}/{len(q[t])}")
                    elif opt == "2":
                        print(f"{un}'s results:")
                        for t, s in r[un].items():
                            print(f"{t}: {s}/{len(q[t])}")
                    elif opt == "3":
                        break
                    else:
                        print("Invalid option!")
        elif ch == "3":
            print("Thank you for using the Quiz Game. Goodbye!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
