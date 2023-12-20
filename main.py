with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    words = file_contents.split()
    count_letters = {}
    for letter in words:
        lowercase = letter.lower()
        for count in lowercase:
           if count in count_letters:
               count_letters[count] += 1 
           else:
               count_letters[count] = 1
    #ls = list(count_letters)
    listed = []
    for letters in count_letters:
        listed.append((count_letters[letters], letters))
    listed.sort(reverse = True)
    
    print("--- Begin reprot of books/frankenstein.txt ---")
    print(f"{len(words)} words found in the document")
    print("")
    print("")
    
    for letters in listed:
        if letters[1].isalpha():
            print(f"The {letters[1]} character was found {letters[0]} times")
    
    print("--- End report ---")
    