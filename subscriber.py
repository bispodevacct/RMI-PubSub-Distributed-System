import Pyro4

# The Subscriber class
@Pyro4.expose
class Subscriber:
    # The method to notify the subscriber
    def notify(self, message):
        print(f'Received message: {message}')


# The subscriber name
name = input('Type your name: ')

# The subscriber server
Pyro4.Daemon.serveSimple(
    {
        Subscriber: f'{name}-server'
    },
    ns = True
)