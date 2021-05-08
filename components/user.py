import sys
sys.path.append("..")

from apis.user_api import UserApi

class User:
    def __init__(self, config):
        self.api = UserApi(config)
    
    def list(self, service_id):
        return self.api.list_users(service_id)
    
    def create(self, service_id, userData):
        return self.api.create_user(service_id, userData)
    
    def get(self, service_id, user_id):
        return self.api.get_user(service_id, user_id)
    
    # def delete(self, service_id, user_id):
    #     return self.api.delete_user(service_id, user_id)
  