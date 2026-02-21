import sys
from collections import Counter

def count_words(filename):
    counter = Counter()

    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            counter.update(line.split())

    for word, count in sorted(counter.items(), key=lambda x: x[1]):
        print(f"{count} {word}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <filename>")
        sys.exit(1)

    count_words(sys.argv[1])