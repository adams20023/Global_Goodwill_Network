import os
import json
from datetime import datetime

# File to store data
DATA_FILE = "ggn_data.json"

# Initialize data structure if file doesn't exist
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as file:
        json.dump({"users": [], "ideas": []}, file)

def load_data():
    """Load data from the JSON file."""
    with open(DATA_FILE, "r") as file:
        return json.load(file)

def save_data(data):
    """Save data to the JSON file."""
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

def register_user():
    """Register a new user."""
    print("\n--- User Registration ---")
    name = input("Enter your name: ")
    email = input("Enter your email: ")

    data = load_data()
    if any(user["email"] == email for user in data["users"]):
        print("Error: A user with this email already exists.")
        return

    data["users"].append({"name": name, "email": email})
    save_data(data)
    print(f"Success: {name} has been registered!")

def submit_idea():
    """Submit a new idea."""
    print("\n--- Submit an Idea ---")
    title = input("Enter the title of your idea: ")
    description = input("Describe your idea: ")

    data = load_data()
    idea_id = len(data["ideas"]) + 1
    data["ideas"].append({
        "id": idea_id,
        "title": title,
        "description": description,
        "votes": 0,
        "submitted_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })
    save_data(data)
    print(f"Success: Your idea '{title}' has been submitted!")

def vote_on_idea():
    """Vote on an existing idea."""
    print("\n--- Vote on an Idea ---")
    data = load_data()
    if not data["ideas"]:
        print("No ideas available to vote on.")
        return

    print("Available Ideas:")
    for idea in data["ideas"]:
        print(f"{idea['id']}. {idea['title']} (Votes: {idea['votes']})")

    try:
        choice = int(input("Enter the ID of the idea you want to vote for: "))
        idea = next((i for i in data["ideas"] if i["id"] == choice), None)
        if idea:
            idea["votes"] += 1
            save_data(data)
            print(f"Success: You voted for '{idea['title']}'!")
        else:
            print("Error: Invalid idea ID.")
    except ValueError:
        print("Error: Please enter a valid number.")

def view_progress():
    """View the progress of all ideas."""
    print("\n--- Progress Tracker ---")
    data = load_data()
    if not data["ideas"]:
        print("No ideas available to track.")
        return

    print("Current Ideas:")
    for idea in data["ideas"]:
        print(f"{idea['id']}. {idea['title']} (Votes: {idea['votes']}) - Submitted on {idea['submitted_at']}")

def main():
    """Main function to run the CLI tool."""
    while True:
        print("\n--- Global Goodwill Network (GGN) ---")
        print("1. Register as a User")
        print("2. Submit an Idea")
        print("3. Vote on an Idea")
        print("4. View Progress")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            register_user()
        elif choice == "2":
            submit_idea()
        elif choice == "3":
            vote_on_idea()
        elif choice == "4":
            view_progress()
        elif choice == "5":
            print("Thank you for using GGN. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
