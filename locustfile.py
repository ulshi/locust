from locust import HttpLocust, TaskSet, task, between
import json

host = "http://114.116.172.56:8080"
loginUrl = "/eUrbanMIS/api/pnemonic/ifbind"

class WebsiteTasks(TaskSet):

    @task(10)
    def index(self):
        self.client.get("http://10.0.1.167:30051/2020/02/12/feiyan1/")
        

    @task(10)
    def on_start(self):
        data = json.dumps({
            "uniqueCode": "oR0PfwNo3DTzkm4zb7BHawFB",                                               
            "cityCode": "3001",                                                      
            "isJsonp": "1",                                                          
            "terminalID": "2",                                                                                                    
            "subCityCode": ""                                                                                                   
        })
        
        response = self.client.post(url= loginUrl,
                                       data = data,
                                       headers = None)
        print("LOGIN RESULT:", response.status_code, response.content)
 

class WebsiteUser(HttpLocust):
    task_set = WebsiteTasks
    wait_time = between(0,0)
