"""
You are given a dictionary consisting of pairs of words. Each word is synonymous with its paired word. All words in the dictionary are different. For one given word, define its synonym.

Input format
The program receives the number of pairs of synonyms as input N. Followed by N
N lines, each line contains exactly two synonymous words. After this comes one word.

Output format
The program must display a synonym for this word.
"""

def main():

    n = int (input())

    synonyms = {}

    for _ in range(n):
        w1, w2 = input().split()
        synonyms[w1] = w2
        synonyms[w2] = w1
    
    word = input()
    print(synonyms[word])
        


if __name__ == '__main__':

    synonyms = main()