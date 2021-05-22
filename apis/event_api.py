from .error import *
from .http_request import HttpRequest
from .http_client import HttpClient

class EventApi:
    def __init__(self, config):
        self.base_url = config['base_url']
        self.http_client = HttpClient(config['api_key'])
        self.validator = Validation()
  
    def list_events(self, service_id, user_id):
        if not self.validator.is_valid_id(service_id):
            return new_error(
                ERROR_TYPES['missing_parameter'],
                "The list_events method must be invoked with a non-empty string service_id argument."
            )
        
        if not self.validator.is_valid_id(user_id):
            return new_error(
                ERROR_TYPES['missing_parameter'],
                "The list_events method must be invoked with a non-empty string user_id argument."
            )
    
        path = f"services/{service_id}/users/{user_id}/events"
        request = HttpRequest("GET", self.base_url, path)
        return self.http_client.send(request)
  
    def create_event(self, service_id, user_id, event_data):
        if not self.validator.is_valid_id(service_id):
            return new_error(
                ERROR_TYPES['missing_parameter'],
                "The create_event method must be invoked with a non-empty string service_id argument."
            )
        
        if not self.validator.is_valid_id(user_id):
            return new_error(
                ERROR_TYPES['missing_parameter'],
                "The create_event method must be invoked with a non-empty string user_id argument."
            )
        
        if not self.validator.is_valid_event_data(event_data):
            return new_error(
                ERROR_TYPES['missing_parameter'],
                "The create_event method must be invoked with an event_data argument containing non-empty event_type and payload properties."
            )
    
        path = f"services/{service_id}/users/{user_id}/events"
        request = HttpRequest("POST", self.base_url, path, event_data)
        return self.http_client.send(request)
  
    def get_event(self, service_id, user_id, event_id):
        if not self.validator.is_valid_id(service_id):
            return new_error(
                ERROR_TYPES['missing_parameter'],
                "The get_event method must be invoked with a non-empty string service_id argument."
            )
        
        if not self.validator.is_valid_id(user_id):
            return new_error(
                ERROR_TYPES['missing_parameter'],
                "The get_event method must be invoked with a non-empty string user_id argument."
            )
        
        if not self.validator.is_valid_id(event_id):
            return new_error(
                ERROR_TYPES['missing_parameter'],
                "The get_event method must be invoked with a non-empty string event_id argument."
            )
    
        path = f"services/{service_id}/users/{user_id}/events/{event_id}"
        request = HttpRequest("GET", self.base_url, path)
        return self.http_client.send(request)
