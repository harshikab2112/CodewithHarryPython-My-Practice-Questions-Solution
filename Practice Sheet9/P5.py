# Repeat program 4 for a list of such words to be censored.

censor_words = ["crazy", "bullshit", "shitshow", "damn"]

# Read the file
with open("P5.txt", "rt") as f:
    content = f.read().lower()

# Replace each word with same-length #####
for word in censor_words:
    content = content.replace(word, "#" * len(word))

# Write the censored content back to the file
with open("P5.txt", "w") as f:
    f.write(content)

# Read and print the updated content
with open("P5.txt", "rt") as f:
    new_content = f.read()
    print(new_content)
