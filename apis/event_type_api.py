from .error import *
from .http_request import HttpRequest
from .http_client import HttpClient

class EventTypeApi:
    def __init__(self, config):
        self.base_url = config['base_url']
        self.http_client = HttpClient(config['api_key'])
        self.validator = Validation()
  
    def list_event_types(self, service_id):
        if not self.validator.is_valid_id(service_id):
            return new_error(
                ERROR_TYPES['missing_parameter'],
                "The list_event_types method must be invoked with a non-empty string service_id argument."
            )
    
        path = f"services/{service_id}/event_types"
        request = HttpRequest("GET", self.base_url, path)
        return self.http_client.send(request)
  
    def create_event_type(self, service_id, event_type_data):
        if not self.validator.is_valid_id(service_id):
            return new_error(
                ERROR_TYPES['missing_parameter'],
                "The create_event_types method must be invoked with a non-empty string service_id argument."
            )
        elif not self.validator.is_valid_data(event_type_data):
            return new_error(
                ERROR_TYPES['missing_parameter'],
                "The create_event_types method must be invoked with an event_type_data object that contains a non-empty string name property."
            )
    
        path = f"services/{service_id}/event_types"
        request = HttpRequest("POST", self.base_url, path, event_type_data)
        return self.http_client.send(request)
  
    def delete_event_type(self, service_id, event_type_id):
        if not self.validator.is_valid_service_id(service_id):
            return new_error(
                ERROR_TYPES['missing_parameter'],
                "The delete_event_type method must be invoked with a non-empty string service_id argument."
            )
        elif not self.validator.event_type_id(event_type_id):
            return new_error(
                ERROR_TYPES['missing_parameter'],
                "The delete_event_type method must be invoked with a non-empty string event_type_id argument."
            )
    
        path = f"services/{service_id}/event_types/{event_type_id}"
        request = HttpRequest("DELETE", self.base_url, path)
        return self.http_client.send(request)
  
    def get_event_type(self, service_id, event_type_id):
        if not self.validator.is_valid_service_id(service_id):
            return new_error(
                ERROR_TYPES['missing_parameter'],
                "The get_event_type method must be invoked with a non-empty string service_id argument."
            )
        elif not self.validator.event_type_id(event_type_id):
            return new_error(
                ERROR_TYPES['missing_parameter'],
                "The get_event_type method must be invoked with a non-empty string event_type_id argument."
            )
    
        path = f"services/{service_id}/event_types/{event_type_id}"
        request = HttpRequest("GET", self.base_url, path)
        return self.http_client.send(request)
