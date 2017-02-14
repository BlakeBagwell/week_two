def word_histogram(sentence):
    #word list is a list containing each word in sentence
    #because of the .split
    word_list = sentence.split()
    #we need a dict to keep track of unchanging keys
    #and a value of how many times they appear
    word_lib = {}
    #this loop checks if the word we are looking at
    #appears in the dict. if not, we add it to the dict
    #and its value is 1 since it appears at least once
    for word in word_list:
        if word not in word_lib:
            word_lib[word] = 1
    #then if we run into that same key again, we just add 1
    #to its value, updating how many times we've seen it.
        else:
            word_lib[word] += 1
    #now we print the dictionary, which shows the key and values, or
    #how many times each word appeared.
    print word_lib
word_histogram('to be or not to be')
