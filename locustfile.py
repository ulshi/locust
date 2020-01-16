from locust import HttpLocust, TaskSet, task, between
class WebsiteTasks(TaskSet):
    @task(1)
    def on_start(self):
        self.client.post("http://159.138.93.135:8080/login", {
            "username": "admin_wp",
            "password": "EL&FK6xsZ&oZCL^MIq"
        })

    @task(10)
    def index(self):
        self.client.get("http://159.138.93.135:8080/2020/01/15/docker-run/")


    @task(10)
    def about(self):
        response=self.client.get("http://159.138.93.135:8080/2020/01/15/docker-import/")
        '''print("Response status code:", response.status_code)
        print("Response content:", response.text)'''

class WebsiteUser(HttpLocust):
    task_set = WebsiteTasks
    wait_time = between(5, 15)
