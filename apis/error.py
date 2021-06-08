def new_error(error_type, detail):
    return {
        "Error": {
            "error_type": error_type,
            "detail": detail,
        },
    }

ERROR_TYPES = {
    "missing_parameter": "missing_parameter",
    "max_retries_reached": "max_retries_reached",
}

class Validation:
    def is_valid_id(self, id):
        return bool(id) and isinstance(id, str)
    
    def is_valid_data(self, data):
        return bool(data)
    
    def is_valid_name(self, data):
        return bool(data['name']) and isinstance(data['name'], str)
    
    def is_valid_subscription_data(self, data):
        if data['eventTypes']:
            data['event_types'] = data['eventTypes']
        
        return (
            bool(data['url']) and
            isinstance(data['url'], str) and
            bool(data['event_types']) and
            len(data['event_types']) > 0
        )
    
    def is_valid_event_data(self, data):
        if data['eventType']:
            data['event_type'] = data['eventType']
        
        if data['idempotencyKey']:
            data['idempotency_key'] = data['idempotencyKey']
        
        return (
            bool(data['event_type']) and
            isinstance(data['event_type'], str) and
            bool(data['idempotency_key']) and
            isinstance(data['idempotency_key'], str) and
            bool(data['payload'])
        )
