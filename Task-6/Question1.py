with open('onelinefile.txt', 'r') as f:
    file_content = str(f.readline())

comma_counter = 0
modified_content = ""
counter = 0

for i in range(0, len(file_content)):
    if counter == 0:
        current_char = file_content[i]
    if i+1 < len(file_content):
        next_char = file_content[i+1]

    if current_char.isalpha():
        modified_content += str(current_char)

        if next_char != "":
            if next_char.isalpha() == False:
                if comma_counter != 3:
                    modified_content += ","
                comma_counter += 1

    elif current_char.isdigit():
        modified_content += str(current_char)

        if next_char == ".":
            modified_content += "."

        elif next_char.isdigit() == False and next_char != ".":
            if comma_counter != 3:
                modified_content += ","
            comma_counter += 1

    
    if comma_counter % 4 == 0:
        modified_content += "\n"
        comma_counter = 0
    

    current_char = next_char
    counter += 1

with open('NewFile.csv', 'w') as f:
    f.writelines(modified_content)

print("CSV file has been created with desired format.")