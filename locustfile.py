from locust import HttpLocust, TaskSet, task, between
class WebsiteTasks(TaskSet):

    @task(10)
    def index(self):
        self.client.get("http://10.0.1.58:30051/2020/02/12/git3/")

    @task(10)
    def index(self):
        self.client.get("http://10.0.1.58:30051/2020/02/12/feiyan3/")

    @task(10)
    def index(self):
        self.client.get("http://10.0.1.58:30051/2020/02/12/feiyan1/")


    @task(10)
    def about(self):
        response=self.client.get("http://10.0.1.58:30051/2020/02/12/bbc2/")
        '''print("Response status code:", response.status_code)
        print("Response content:", response.text)'''

class WebsiteUser(HttpLocust):
    task_set = WebsiteTasks
    wait_time = between(5, 15)
