from apis.event_api import EventApi

class Event:
  def __init__(self, config):
    self.api = EventApi(config)
  
  def list(self, service_id, user_id):
    return self.api.list_events(service_id, user_id)
  
  def create(self, service_id, user_id, event_data):
    return self.api.create_event(service_id, user_id, event_data)
  
  def get(self, service_id, user_id, event_id):
    return self.api.get_event(service_id, user_id, event_id)
