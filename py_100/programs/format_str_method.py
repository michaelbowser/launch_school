
name = input("Hello! What is your name?  ")
job = input(f"Hi {name}! Now, what do you do for a living? ")
greeting = "Hello, {}. Ah, you're a {}! Nice to meet you!"
formatted_greeting = greeting.format(name, job)
print(formatted_greeting)


