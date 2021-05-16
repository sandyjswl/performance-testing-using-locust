from locust import task, between, tag
from locust.user.users import HttpUser


class WebsiteUser(HttpUser):
    wait_time = between(5, 15)
    host = "http://localhost:5000"

    @task(1)
    @tag("Get User")
    def get_user(self):
        self.client.get("/user",)

    @task(1)
    @tag("Post User")
    def post_user(self):
        self.client.post("/user", data={"name": "sandeep", "city": "bangalore"})

    @task(1)
    @tag("Get Version")
    def version(self):
        self.client.get("/version")
