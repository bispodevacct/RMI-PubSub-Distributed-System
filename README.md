# RMI-PubSub-Distributed-System

The RMI PubSub Distributed System is a Python Publish/Subscribe program implemented using the remote method invocation library Pyro4. It was developed to the Distributed Systems discipline of my Computer Science college degree.

## How to run it?

To run the system, you must follow some steps:

### 1. The Pyro4 Name Server

First of all, run your first shell and run the 'pyro4-ns' command.

### 2. The Publisher Server

Next, you must open another shell and run the 'publish.py' script. Give it a topic and it will initialize a publisher server.

### 3. The Publishing Client

Now, you must open one more shell and run the 'publishing.py' script. This shell will be your publishing and subscribing window. Give it the same topic to make a connection and go to the next step.

### 4. The Subcriber Server

In the "final step", you must open another shell and run the 'subscriber.py' script. Give it a name to your subscriber and this shell will be its server. Return to the publishing client and register this subscriber to receive messages.

### 5. Repeat the three last steps to add another publisher or subscriber

That is it.

## The Publisher Methods

The Publisher Class has some methods to subscribe, unsubscribe subscribers and to publish messages to them. 

## The Subscriber Methods

The subscriber Class has only one method that is the notify to receive messages from the publishers.

## The Publishing Script

The publishing script allow us to publish messages and subscribe or unsubscribe subscribers.
