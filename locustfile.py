from locust import HttpLocust, TaskSet, task, between
class WebsiteTasks(TaskSet):

    @task(10)
    def index(self):
        self.client.get("http://119.3.146.15:8081/standard-linkage/qyfg/index.html")

    @task(10)
    def index(self):
        self.client.get("http://10.0.1.167:30051/2020/02/12/feiyan1/")
    
    @task(10)
    def index(self):
        payload={'uniqueCode': 'oR0PfwNo3DTzkm4zb7BHawFB', 'cityCode': '3009', 'isJsonp': '1', 'terminalID': '2', 'subCityCode': None}
        self.client.get("http://114.116.172.56:8080/eUrbanMIS/api/pnemonic/ifbind",payload)
class WebsiteUser(HttpLocust):
    task_set = WebsiteTasks
    wait_time = between(5, 15)
