def show_messages(messages):
    for message in messages:
        print(message)

def send_messages(messages_to_send, sent_messages):
    while messages_to_send:
        message = messages_to_send.pop()
        print(message)
        sent_messages.append(message)


messages = ["Hello everyone!", "See you later"]
sent_messages = []

# show_messages(messages)

send_messages(messages, sent_messages)

print("Original messages:")
show_messages(messages)
print("Sent messages:")
show_messages(sent_messages)
