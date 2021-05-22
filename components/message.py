from apis.message_api import MessageApi

class Message:
    def __init__(self, config):
        self.api = MessageApi(config)
    
    def list(self, service_id, user_id):
        return self.api.list_messages(service_id, user_id)
    
    def resend(self, service_id, user_id, message_id):
        return self.api.resend_message(service_id, user_id, message_id)
    
    def get(self, service_id, user_id, message_id):
        return self.api.get_message(service_id, user_id, message_id)
