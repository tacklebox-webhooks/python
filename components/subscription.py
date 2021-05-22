from apis.subscription_api import SubscriptionApi

class Subscription:
    def __init__(self, config):
        self.api = SubscriptionApi(config)
    
    def list(self, service_id, user_id):
        return self.api.list_subscriptions(service_id, user_id)
    
    def create(self, service_id, user_id, subscription_data):
        return self.api.create_subscription(
          service_id,
          user_id,
          subscription_data
        )
    
    def get(self, service_id, user_id, subscription_id):
        return self.api.get_subscription(service_id, user_id, subscription_id)
    
    def delete(self, service_id, user_id, subscription_id):
        return self.api.delete_subscription(service_id, user_id, subscription_id)
  