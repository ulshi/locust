from locust import HttpLocust, TaskSet, task, between
class WebsiteTasks(TaskSet):

    def index(self):
        self.client.post("http://114.116.172.56:8080/eUrbanMIS/api/pnemonic/ifbind",{'uniqueCode': 'oR0PfwNo3DTzkm4zb7BHawFB', 'cityCode': '3009', 'isJsonp': '1', 'terminalID': '2', 'subCityCode': None})
        
     

class WebsiteUser(HttpLocust):
    task_set = WebsiteTasks
    wait_time = between(1, 3)
