from locust import HttpLocust, TaskSet, task, between
class WebsiteTasks(TaskSet):
    def index(self):        
        self.client.get("http://159.138.106.243:30051/2020/02/13/mssql-backup-summary/")
        
class WebsiteUser(HttpLocust):
    task_set = WebsiteTasks
    wait_time = between(2, 4)
