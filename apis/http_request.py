class HttpRequest:
    def __init__(self, method, base_url, path=None, data=None):
        self.attempt = 1
        self.method = method
        self.base_url = base_url
        self.path = path
        
        if bool(data) and bool(data.get('event_types')):
            data['eventTypes'] = data['event_types']
            data.pop('event_types')
        
        self.data = data
