from collections import Counter
def word_count(fname):
    with open(fname) as f:
        return Counter(f.read().split())
print("Number of words in the file : ",word_count("file1.txt"))
