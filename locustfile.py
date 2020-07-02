from locust import HttpLocust, TaskSet, task, between
import json

host = "http://119.3.135.230:80"
loginUrl = "/eUrbanMIS/login/validpassword"

class WebsiteTasks(TaskSet):

    @task(10)
    def index(self):
        self.client.post("http://ln3jd7py4cb0tr4r.zhutingxue.ap-southeast-3.huaweicse.com/ui/rest/userservice/registe",{
            "telNum": "5768578",
            "user": "675478"   
        })      

    @task(10)
    def index(self):
        self.client.get("http://ln3jd7py4cb0tr4r.zhutingxue.ap-southeast-3.huaweicse.com/weathermapweb/ui/fusionweatherdata?city=Shenzhen")       
        
class WebsiteUser(HttpLocust):
    task_set = WebsiteTasks
    host = host
    wait_time = between(0,0)
