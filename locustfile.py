from locust import HttpLocust, TaskSet, task, between
class WebsiteTasks(TaskSet):

    @task(10)
    def index(self):
        self.client.get("http://10.0.1.167:30051/2020/02/12/feiyan1/")


    @task(10)
    def about(self):
        response=self.client.get("http://10.0.1.167:30051/2020/02/12/bbc2/")

class WebsiteUser(HttpLocust):
    task_set = WebsiteTasks
    wait_time = between(0,0)
