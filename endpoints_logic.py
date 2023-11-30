import json

DATA_FILE = "data.json"

def load_data():
    try:
        with open(DATA_FILE, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []
    return data

def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=2)

data = load_data()

def get_users():
    return data

def get_user(user_id):
    for user in data:
        if user["id"] == user_id:
            return user
    return None

def create_user(user_data):
    user_id = len(data) + 1
    user = {"id": user_id, **user_data}
    data.append(user)
    save_data(data)
    return {"user_id": user_id}

def update_user(user_id, updated_data):
    for user in data:
        if user["id"] == user_id:
            user.update(updated_data)
            save_data(data)
            return {}
    raise ValueError("User not found")

def delete_user(user_id):
    for i, user in enumerate(data):
        if user["id"] == user_id:
            del data[i]
            save_data(data)
            return {}
    raise ValueError("User not found")
