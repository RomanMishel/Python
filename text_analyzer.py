def text_analyzer():
    text = input("Enter text to analyze: ")
    # Analyze the text
    text_length = len(text) # Calculate the length of the text
    word_count = len(text.split()) # Calculate the number of words in the text
    char_count = sum(1 for char in text if char.isalnum()) # Calculate the number of alphanumeric characters in the text
    sentence_count = text.count('.') + text.count('!') + text.count('?') # Calculate the number of sentences in the text

    print(f"Text Length: {text_length} characters")
    print(f"Word Count: {word_count} words")
    print(f"Character Count (alphanumeric): {char_count} characters")
    print(f"Sentence Count: {sentence_count} sentences")

text_analyzer()