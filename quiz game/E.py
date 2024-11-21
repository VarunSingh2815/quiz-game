questions = {
    "DSA": [
        {"question": "What is the time complexity of binary search?", "options": ["O(n)", "O(log n)", "O(n^2)", "O(1)"], "answer": "O(log n)"},
        {"question": "Which data structure uses LIFO principle?", "options": ["Queue", "Stack", "Tree", "Graph"], "answer": "Stack"},
        {"question": "What is the maximum number of children a binary tree node can have?", "options": ["1", "2", "3", "4"], "answer": "2"},
        {"question": "Which algorithm is used to find the shortest path in a graph?", "options": ["DFS", "BFS", "Dijkstra", "Kruskal"], "answer": "Dijkstra"},
        {"question": "What data structure is used in a BFS algorithm?", "options": ["Stack", "Queue", "Tree", "Graph"], "answer": "Queue"},
    ],
    "DBMS": [
        {"question": "What is a primary key?", "options": ["A unique identifier", "A foreign key", "A secondary key", "A primary function"], "answer": "A unique identifier"},
        {"question": "What does SQL stand for?", "options": ["Structured Query Language", "Standard Query Language", "Simple Query Language", "Sequential Query Language"], "answer": "Structured Query Language"},
        {"question": "Which type of join returns all rows from the left table and the matched rows from the right table?", "options": ["Inner Join", "Left Join", "Right Join", "Full Join"], "answer": "Left Join"},
        {"question": "What is normalization?", "options": ["The process of organizing data", "The process of defining keys", "The process of creating indexes", "The process of deleting data"], "answer": "The process of organizing data"},
        {"question": "What does ACID stand for in databases?", "options": ["Atomicity, Consistency, Isolation, Durability", "Access, Consistency, Isolation, Durability", "Atomicity, Consistency, Inconsistency, Durability", "Atomicity, Clarity, Isolation, Durability"], "answer": "Atomicity, Consistency, Isolation, Durability"},
    ],
    "Python": [
        {"question": "Which keyword is used to define a function in Python?", "options": ["func", "def", "function", "define"], "answer": "def"},
        {"question": "Which data type is immutable in Python?", "options": ["List", "Dict", "Set", "Tuple"], "answer": "Tuple"},
        {"question": "What is the output of print(2**3)?", "options": ["6", "8", "9", "12"], "answer": "8"},
        {"question": "Which method is used to add an element at the end of a list?", "options": ["append()", "insert()", "add()", "extend()"], "answer": "append()"},
        {"question": "What does PEP stand for?", "options": ["Python Enhancement Proposal", "Python Easy Program", "Python Execution Process", "Python Environmental Policy"], "answer": "Python Enhancement Proposal"},
    ]
}

users = {}
results = {}

def register():
    un = input("ENTER USERNAME: ")
    if un in users:
        print("Username Already Exists")
        return
    password = input("Enter a Password: ")
    users[un] = password
    results[un] = {}
    print("Registration Successful")

def login():
    un = input("Enter username for login: ")
    password = input("Enter password for login: ")
    if un in users and users[un] == password:
        print("Login Successful")
        return True, un
    else:
        print("Invalid Username or Password")
        return False, None

def tq(topic, username):
    if topic not in questions:
        print("Invalid Topic")
        return 0
    score = 0
    for q in questions[topic]:
        print(q["question"])
        for i, option in enumerate(q["options"]):
            print(f"{i + 1}. {option}")
        answer = input("Your answer: ")
        if q["options"][int(answer) - 1] == q["answer"]:
            score += 1
    results[username][topic] = score
    return score

def main():
    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            register()
        elif choice == "2":
            logged_in, username = login()
            if logged_in:
                while True:
                    print("\n1. Take Quiz")
                    print("2. Show Result")
                    print("3. Logout")
                    option = input("Choose an option: ")
                    if option == "1":
                        print("Choose a topic: DSA, DBMS, Python")
                        topic = input("Your choice: ")
                        score = tq(topic, username)
                        print(f"Your score: {score}/{len(questions[topic])}")
                    elif option == "2":
                        print(f"{username}'s results:")
                        for topic, score in results[username].items():
                            print(f"{topic}: {score}/{len(questions[topic])}")
                    elif option == "3":
                        break
                    else:
                        print("Invalid option!")
        elif choice == "3":
            print("Thank you for using the Quiz Game. Goodbye!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()

