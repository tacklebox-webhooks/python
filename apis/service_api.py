from .error import *
from .http_request import HttpRequest
from .http_client import HttpClient

class ServiceApi:
    def __init__(self, config):
        self.base_url = config['base_url']
        self.http_client = HttpClient(config['api_key'])
        self.validator = Validation()

    def list_services(self):
        path = "services"
        request = HttpRequest("GET", self.base_url, path)
        return self.http_client.send(request)
  
    def create_service(self, service_data):
        if not self.validator.is_valid_data(service_data):
            return new_error(
                ERROR_TYPES['missing_parameter'],
                "The create_service method must be invoked with a non-empty string name argument."
            )
  
        path = "services"
        request = HttpRequest("POST", self.base_url, path, service_data)
        return self.http_client.send(request)
  
    def delete_service(self, service_id):
        if not self.validator.is_valid_id(service_id):
            return new_error(
                ERROR_TYPES['missing_parameter'],
                "The delete_service method must be invoked with a non-empty string service_id argument."
            )
    
        path = f"services/{service_id}"
        request = HttpRequest("DELETE", self.base_url, path)
        return self.http_client.send(request)
  
    def get_service(self, service_id):
        if not self.validator.is_valid_id(service_id):
            return new_error(
                ERROR_TYPES['missing_parameter'],
                "The get_service method must be invoked with a non-empty string service_id argument."
            )
    
        path = f"services/{service_id}"
        request = HttpRequest("GET", self.base_url, path)
        return self.http_client.send(request)
