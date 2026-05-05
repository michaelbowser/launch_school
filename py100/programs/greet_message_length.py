def greet(name):
    return f"Hello, {name}!"

message = input("Hi there! What's your name? ", greet)

print("Message length is", len(message))
