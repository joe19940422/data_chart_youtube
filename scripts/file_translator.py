from googletrans import Translator

# Initialize the translator
translator = Translator()

# Read the file content
with open('your_file.txt', 'r', encoding='utf-8') as file:
    content = file.read()

# Translate the content to Traditional Chinese
translated_content = translator.translate(content, src='auto', dest='zh-TW').text

# Save the translated content to a new file
with open('translated_file.txt', 'w', encoding='utf-8') as file:
    file.write(translated_content)

print("Translation completed and saved to 'translated_file.txt'")
