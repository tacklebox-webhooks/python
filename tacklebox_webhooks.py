from components.service import Service
from components.event_type import EventType
from components.user import User
from components.subscription import Subscription
from components.event import Event
from components.message import Message

class Tacklebox:
    def __init__(self, api_key, base_url):
        config = {
            'api_key': api_key,
            'base_url': base_url,
        }
        
        self.service = Service(config)
        self.event_type = EventType(config)
        self.user = User(config)
        self.subscription = Subscription(config)
        self.event = Event(config)
        self.message = Message(config)