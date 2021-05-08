import sys
sys.path.append("..")

from apis.service_api import ServiceApi

class Service:
    def __init__(self, config):
        self.api = ServiceApi(config)
    
    def list(self):
        return self.api.list_services()
    
    def create(self, serviceData):
        return self.api.create_service(serviceData)
    
    def get(self, service_id):
        return self.api.get_service(service_id)
  
  # def delete(self, service_id):
  #     return self.api.delete_service(service_id)
