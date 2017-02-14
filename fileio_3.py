import word_summary

myFile = open(raw_input("Enter file name: ")).read()

word_summary.word_histogram(myFile)
