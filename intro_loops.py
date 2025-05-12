# 🎯 Goal: Loop through the list of coding languages and print a message about each one.

# 📜 Define a list of coding languages that we're learning about.
coding_languages = ["Javascript", "Python", "Java", "Bash", "Go"]

# 🔢 Get the length of the list. This will be used to control the while loop.
length = len(coding_languages)

# 🚦 Initialize the index to 0. This ensures we start at the first element in the list.
index = 0

while index < length:
    print("I am learning about " + coding_languages[index])
    
    # ➡️ Goal: Move to the next language by incrementing the index.
    # Without this, the loop would run indefinitely, printing the same item.
    index += 1

  