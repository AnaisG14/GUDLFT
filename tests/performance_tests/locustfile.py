from locust import HttpUser, task


class ProjectPerfTest(HttpUser):
    @task
    def home(self):
        self.client.get('/')

    @task(2)
    def board(self):
        self.client.get('/board')

    @task
    def show_summary(self):
        self.client.post('/showSummary', {"email": "john@simplylift.co"})

    @task(3)
    def purchase_place(self):
        self.client.post('/purchasePlaces', {"club": "Simply Lift", "competition": "Fall Classic", "places": 4})


