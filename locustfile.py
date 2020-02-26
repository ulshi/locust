from locust import HttpLocust, TaskSet, task, between
class WebsiteTasks(TaskSet):
    def index(self):        
        self.client.get("http://114.116.172.56:8080/eGovaPublic/view/mobileapp/publicinspect/index.html?cityCode=3009&isWechat=1&other=1&moduleId=266&openId=oR0PfwNo3DTzkm4zb7BHawFB#/epidemicHome?VNK=c18082cb")
        
class WebsiteUser(HttpLocust):
    task_set = WebsiteTasks
    wait_time = between(2, 4)
