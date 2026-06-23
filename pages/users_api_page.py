import requests

class UsersApi:
    URL_BASE = "https://jsonplaceholder.typicode.com/"

    # GET ONE USER
    def get_one_user(self, user_id):
        return requests.get(
            f"{self.URL_BASE}/users/{user_id}"
        )

    # UPDATE COMPLETE USER
    def update_user(self, user_id, name, username, email):
        json_data = {
            "id": user_id,
            "name": name,
            "username": username,
            "email": email
        }

        return requests.put(
        f"{self.URL_BASE}/users/{user_id}",
        json= json_data
        )

    # DELETE USER
    def delete_user(self, user_id):
        return requests.delete(
            f"{self.URL_BASE}/users/{user_id}"
        )
