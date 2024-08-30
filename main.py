def calculate_frequency(text):
  frequency = {}
  total_chars = len(text)
  characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

  for char in text:
    if char.isalpha():
      char = char.upper()
      frequency[char] = frequency.get(char, 0) + 1

  for character in characters:
    frequency.setdefault(character, 0)

  sorted_frequency = dict(
      sorted(frequency.items(), key=lambda item: item[1], reverse=True))

  for char, count in sorted_frequency.items():
    percentage = (count / total_chars) * 100
    print(f"{char}: {count} ({percentage:.2f}%)")


def count_occurrences(text):
  char_count = {}
  for char in text:
    if char.isalpha():
      char_count[char.upper()] = char_count.get(char.upper(), 0) + 1
  return char_count


def change_top_occurrences(text, replacements):
  char_count = count_occurrences(text)
  top_chars = sorted(char_count, key=char_count.get,
                     reverse=True)[:len(replacements)]

  for i, char in enumerate(top_chars):
    text = text.replace(char,
                        '$$').replace(replacements[i],
                                      char).replace('$$', replacements[i])

  return text


def change_characters(modified_text, replacements):
  while True:
    user_input = input(
        "Enter the characters you want to change (or -1 to quit): ")
    for char in replacements:
      if user_input == char:
        print('E T or A Cannot be changed!!!')
        change_characters(modified_text, replacements)
    if user_input == '-1':
      break
    replacement_input = input("Enter the characters for replacement: ")
    for char in replacements:
      if replacement_input == char:
        print('E T or A Cannot be changed!!!')
        change_characters(modified_text, replacements)

    modified_text = modified_text.replace(user_input, '$$').replace(
        replacement_input, user_input).replace('$$', replacement_input)
    print()
    print(modified_text)

  print()
  print('\t\t\t\t\t\t\t\t\t\t\t\t\t\t\bNEW TEXT:')

  with open('example.txt', 'w') as file:
    file.write(modified_text)

    return modified_text


if __name__ == "__main__":
  print("""
														 -----------------------------------
														 ||                               ||   
														 ||  WELCOME TO FREQUENCY ANALYSIS||
														 ||  DECRYPT AT YOUR OWN WILL...  ||
														 -----------------------------------  
														 """)

  
  
  print ("Please Select an option:")
  
  while True:
    passage_select = input("""Press 1 to select passage1
Press 2 to select passage2
Your Input: """)

    if passage_select == '2':
      with open('passage2.txt', 'r') as file:
        content = file.read()
      print("PASSAGE 2")
      print("-" * 32)
      print(content)
      break

    elif passage_select == '1':
      with open('passage1.txt', 'r') as file:
        content = file.read()
      print("PASSAGE 1")
      print("-" * 32)
      print(content)
      break

    else:
      print("Wrong input!!!")

  input("Press Enter to continue: ")
  print()
  calculate_frequency(content)
  print()
  input("Press Enter to continue: ")

  replacements = ['E', 'T', 'A']
  print()
  modified_content = change_top_occurrences(content, replacements)

  print()
  print(modified_content)
  print()
  modified_content = change_characters(modified_content, replacements)
  print(modified_content)
