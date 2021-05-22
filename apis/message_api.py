from .error import *
from .http_request import HttpRequest
from .http_client import HttpClient

class MessageApi:
    def __init__(self, config):
        self.base_url = config['base_url']
        self.http_client = HttpClient(config['api_key'])
        self.validator = Validation()
  
    def list_messages(self, service_id, user_id):
        if not self.validator.is_valid_id(service_id):
            return new_error(
                ERROR_TYPES['missing_parameter'],
                "The list_messages method must be invoked with a non-empty string service_id argument."
            )
        
        if not self.validator.is_valid_id(user_id):
            return new_error(
                ERROR_TYPES['missing_parameter'],
                "The list_messages method must be invoked with a non-empty string user_id argument."
            )
    
        path = f"services/{service_id}/users/{user_id}/messages"
        request = HttpRequest("GET", self.base_url, path)
        return self.http_client.send(request)
  
    def resend_message(self, service_id, user_id, message_id):
        if not self.validator.is_valid_id(service_id):
            return new_error(
                ERROR_TYPES['missing_parameter'],
                "The resend_message method must be invoked with a non-empty string service_id argument."
            )
    
        if not self.validator.is_valid_id(user_id):
            return new_error(
                ERROR_TYPES['missing_parameter'],
                "The resend_message method must be invoked with a non-empty string user_id argument."
            )
        
        if not self.validator.is_valid_id(message_id):
            return new_error(
                ERROR_TYPES['missing_parameter'],
                "The resend_message method must be invoked with a non-empty string message_id argument."
            )
        
    
        path = f"services/{service_id}/users/{user_id}/messages/{message_id}/resend"
        request = HttpRequest("POST", self.base_url, path)
        return self.http_client.send(request)
  
    def get_message(self, service_id, user_id, message_id):
        if not self.validator.is_valid_id(service_id):
            return new_error(
                ERROR_TYPES['missing_parameter'],
                "The get_message method must be invoked with a non-empty string service_id argument."
            )
        
        if not self.validator.is_valid_id(user_id):
            return new_error(
                ERROR_TYPES['missing_parameter'],
                "The get_message method must be invoked with a non-empty string user_id argument."
            )
        
        
        if not self.validator.is_valid_id(message_id):
            return new_error(
                ERROR_TYPES['missing_parameter'],
                "The get_message method must be invoked with a non-empty string message_id argument."
            )
        
    
        path = f"services/{service_id}/users/{user_id}/messages/{message_id}"
        request = HttpRequest("GET", self.base_url, path)
        return self.http_client.send(request)
