import re

# Function to replace a word in a paragraph
def replace_word_in_paragraph(paragraph, old_word, new_word):
    # Use regular expressions to match the whole word
    # r'\b' is a word boundary anchor, ensuring we match the whole word only
    updated_paragraph = re.sub(r'\b' + re.escape(old_word) + r'\b', new_word, paragraph)
    return updated_paragraph

# Main program
def main():
    # Accept the paragraph from the user
    paragraph = input("Enter a paragraph: ")

    # Ask the user for the word they want to replace
    old_word = input("Enter the word you want to replace: ")

    # Ask the user for the word to replace it with
    new_word = input("Enter the word you want to use as replacement: ")

    # Call the function to replace the word in the paragraph
    updated_paragraph = replace_word_in_paragraph(paragraph, old_word, new_word)

    # Display the updated paragraph
    print("\nUpdated Paragraph:")
    print(updated_paragraph)

# Run the main program
if __name__ == "__main__":
    main()
