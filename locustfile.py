from locust import HttpLocust, TaskSet, task, between
class WebsiteTasks(TaskSet):
    '''
    http://114.116.172.56:8080
    '''
    def index(self):
        payload={'uniqueCode': 'oR0PfwNo3DTzkm4zb7BHawFB', 'cityCode': '3009', 'isJsonp': '1', 'terminalID': '2', 'subCityCode': None}
        self.client.get("eUrbanMIS/api/pnemonic/ifbind",params=payload)
        
     '''   
    def on_start(self):
        self.client.post("http://159.138.93.135:8080/login", {
            "username": "admin_wp",
            "password": "EL&FK6xsZ&oZCL^MIq"
        })

    @task
    def index(self):
        self.client.get("http://159.138.93.135:8080/wp-admin/edit.php")


    @task
    def about(self):
        response=self.client.get("http://159.138.93.135:8080/wp-admin/post.php?post=1&action=edit")
        print("Response status code:", response.status_code)
        print("Response content:", response.text)
    '''
class WebsiteUser(HttpLocust):
    task_set = WebsiteTasks
    wait_time = between(2, 4)
