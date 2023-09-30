import Pyro4

# The Publisher Class
@Pyro4.expose
class Publisher:
    # The list that contain the subscribers
    def __init__(self):
        self.subscribers = []
    
    # The method to subscribe a subscriber
    def subscribe(self, name):
        subscriber = Pyro4.Proxy(f'PYRONAME:{name}-server')

        if subscriber not in self.subscribers:
            self.subscribers.append(subscriber)
            print(f'{subscriber} successfully subscribed!')
        else:
            print(f'{subscriber} already subscribed.')
    
    # The method to unsubscribe a subscriber
    def unsubscribe(self, name):
        subscriber = Pyro4.Proxy(f'PYRONAME:{name}-server')

        if subscriber in self.subscribers:
            self.subscribers.remove(subscriber)
            print(f'{subscriber} successfully unsubscribed!')
        else:
            print(f'{subscriber} not previously subscribed.')
    
    # The method to publish a message to the subscribers
    def publish(self, message):
        for subscriber in self.subscribers:
            subscriber.notify(message)

# The publisher topic
topic = input('Type the publisher topic: ')

# The publisher server
Pyro4.Daemon.serveSimple(
    {
        Publisher: f'{topic}-server'
    },
    ns = True
)