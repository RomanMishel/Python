user_text = input("Enter you word: ")

most_frequent = max(user_text, key=user_text.count)

print("Most frequent symbol: ", most_frequent)
print("Repeats counter: ", user_text.count(most_frequent))