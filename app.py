print("Welcome to Bihar Local Guide 🇮🇳")
print("Ask me about Bihar street food or local culture.")

while True:
    user_input = input("\nYou: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Dhanyavaad! Visit Bihar again 🙏")
        break
    else:
        print("Local Guide:")
        print(
            "You should try Litti Chokha, Chana Ghugni, or Sattu Sharbat "
            "based on local Bihar culture and season."
        )
