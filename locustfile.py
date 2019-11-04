from locust import HttpLocust, TaskSet, task

class UserBehavior(TaskSet):

    @task
    def get_tests(self):
        self.client.get("/user/2972307e-f087-4072-8e6a-e523791e85d5")
        
#     @task
#     def put_tests(self):
#         self.client.post("/user", {
#   "email": "gg@gg.com",
#   "username": "user",
#   "password": "pass"
# })
        

class WebsiteUser(HttpLocust):
    task_set = UserBehavior