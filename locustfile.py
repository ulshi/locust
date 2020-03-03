from locust import HttpLocust, TaskSet, task, between
import json

host = "http://119.3.135.230:80"
loginUrl = "/eUrbanMIS/login/validpassword"

class WebsiteTasks(TaskSet):

    @task(10)
    def index(self):
        self.client.get("http://10.0.1.167:30051/2020/02/12/feiyan1/")
        
    @task(10)
    def on_start(self):
        data = json.dumps({
            "u": "egova",                                               
            "p": "+G0+zDMNG3UlrBx3A2AGOg==",                                                      
            "ip": "",                                                          
            "browserVersion": "chrome/78.0.3904.108",                                                                                                    
            "osVersion": "Win10/64"                                                                                                   
        })
        
        response = self.client.post(url= loginUrl,{
            "u": "egova",                                               
            "p": "+G0+zDMNG3UlrBx3A2AGOg=="
        })
 

class WebsiteUser(HttpLocust):
    task_set = WebsiteTasks
    host = host
    wait_time = between(0,0)
