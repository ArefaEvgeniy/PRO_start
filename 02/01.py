text = "Цей текст містить деякі українські символи."
text_2 = "This text contains some Ukrainian characters"

with open("ukrainian_text.txt", "w") as file:
    file.write(text)

with open("ukrainian_text.txt", "r", encoding="Windows-1251") as file:
    content = file.read()
    print(content)

with open("new_text.txt", "w", encoding="utf-8") as file:
    file.write(text_2)

with open("new_text.txt", "rb") as file:
    print(file.read().decode("utf-8"))
