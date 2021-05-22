from apis.event_type_api import EventTypeApi

class EventType:
    def __init__(self, config):
        self.api = EventTypeApi(config)
    
    def list(self, service_id):
        return self.api.list_event_types(service_id)
    
    def create(self, service_id, event_typeData):
        return self.api.create_event_type(service_id, event_typeData)
    
    def get(self, service_id, event_typeId):
        return self.api.get_event_type(service_id, event_typeId)
    
    # def delete(self, service_id, event_typeId):
    #     return self.api.deleteEventType(service_id, event_typeId)
