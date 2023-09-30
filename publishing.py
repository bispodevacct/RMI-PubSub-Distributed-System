import Pyro4

# The publisher topic
topic = input('Type the publisher topic: ')

# The publisher instance
publisher = Pyro4.Proxy(f'PYRONAME:{topic}-server')

# The system to publish messages and subscribe its subscribers
while True:
    print('1 - Publish a new message')
    print('2 - Register a new subscriber')
    print('3 - Unregister a subscriber')
    print('4 - Quit')

    option = int(input('Type an option: '))

    if option == 1:
        message = input('Type a message to publish: ')
        publisher.publish(message)
    elif option == 2:
        name = input('Type the subscriber name: ')
        subscriber = Pyro4.Proxy(f'PYRONAME:{name}-server')
        publisher.subscribe(name)
    elif option == 3:
        name = input('Type the subscriber name: ')
        subscriber = Pyro4.Proxy(f'PYRONAME:{name}-server')
        publisher.unsubscribe(name)
    else:
        break