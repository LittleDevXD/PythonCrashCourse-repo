def send_messages(messages):
    sent_messages = []

    while messages:
        message = messages.pop()
        print(f"Sending message: {message}")
        sent_messages.insert(0, message)

    return sent_messages

def show_messages(messages, sent_messages):
    print("\nMessages to send: ")
    for message in messages:
        print(message)

    print("\nMessage already sent: ")
    for message in sent_messages:
        print(message)
        
messages = ["Hello World", "Hello class", "Are you serious?"]
sent_messages = send_messages(messages[:])

send_messages(messages[:])
show_messages(messages, sent_messages)