from locust import HttpLocust, TaskSet, task, between, requests
class WebsiteTasks(TaskSet):

    def index(self):
        payload={'uniqueCode': 'oR0PfwNo3DTzkm4zb7BHawFB', 'cityCode': '3009', 'isJsonp': '1', 'terminalID': '2', 'subCityCode': None}
        requests.get("http://114.116.172.56:8080/eUrbanMIS/api/pnemonic/ifbind",payload)
        
     

class WebsiteUser(HttpLocust):
    task_set = WebsiteTasks
    wait_time = between(1, 3)
