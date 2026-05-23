from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time = between(1, 2.5)  # пауза между действиями от 1 до 2.5 секунд

    @task(3)  # вес 3 (будет выполняться чаще)
    def homepage(self):
        self.client.get("/")

    @task(2)
    def masterclasses(self):
        self.client.get("/masterclasses/")

    @task(1)
    def library(self):
        self.client.get("/library/")