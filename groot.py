default_reply = "I am Groot"

while True:
  user_input = input("You: ")
  if user_input.lower() == "bye":
    break
  print("Groot:", default_reply)
