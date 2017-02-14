def letter_summary(word):

    counts = {}

    for char in word:
        #counts[char] = counts.get(char, 0) + 1
        #a broken down example of what is above
        #current_count = counts.get(char, 0)
        #counts[char] = current_count + 1
        if char not in counts:
            counts[char] = 1
        else:
            ocunts[char] += 1

    for char, count in counts.items():
        print "%d %s's" % (count, char)
