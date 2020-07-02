from locust import HttpLocust, TaskSet, task, between
import json


class WebsiteTasks(TaskSet):

    @task(10)
    def index(self):
        self.client.get("http://ln3jd7py4cb0tr4r.zhutingxue.ap-southeast-3.huaweicse.com/weathermapweb/ui/fusionweatherdata?city=Shenzhen")       
        
class WebsiteUser(HttpLocust):
    task_set = WebsiteTasks
    host = host
    wait_time = between(0,10)
