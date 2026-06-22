import requests

class PostsApi:
    URL_BASE = "https://jsonplaceholder.typicode.com/"

    # GET ONE POST
    def get_one_post(self, post_id):
        return requests.get(
            f"{self.URL_BASE}/posts/{post_id}"
        )

    # GET ALL POSTS
    def get_all_posts(self):
        return requests.get(
            f"{self.URL_BASE}/posts"
        )

    # SEND POST REQUEST
    def send_post(self, title, body, user_id):
        json_data = {
            "title": title,
            "body": body,
            "userId": user_id
            }

        return requests.post(
        f"{self.URL_BASE}/posts",
        json = json_data
        )