file = open("about.txt","r")
most_occured_word = ""
occurence = 0
words = []
six_letter_words = []
for line in file:
    line_word = line.lower().replace(',','').replace('.','').replace(':','').split(" ")
    
    for w in line_word:
        words.append(w)
        
for i in range(0, len(words)):
    count = 1
    length = len(words[i])
    for j in range(i+1, len(words)):
        if(words[i] == words[j]):
            count = count + 1

    if(count > occurence):
        occurence = count
        most_occured_word = words[i]

    if(length == 6):
        if(words[i] not in six_letter_words):
            six_letter_words.append(words[i])

    

print("\nMost repeated word: " + most_occured_word)
print("\nWords with six letters are:")
for i in six_letter_words:
    print(i)

file.close()
