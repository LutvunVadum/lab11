import csv
from collections import Counter

with open('words.txt', 'r') as txt_file:
    words = txt_file.read().splitlines() 

word_counts = Counter(words)

with open('words.csv', 'w', newline='') as csv_file:
    fieldnames = ['Word', 'Frequency']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()  
    for word, count in word_counts.items():
        writer.writerow({'Word': word, 'Frequency': count})

print("Файл words.csv успішно створений з частотою слів.")
