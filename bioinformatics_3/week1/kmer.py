import os

def count(text: str, pattern: str) -> int:
    count: int = 0
    pattern_length = len(pattern)
    text_length = len(text)
    for i in range(text_length - pattern_length):
        if text[i:i+pattern_length] == pattern:
            count += 1
    return count

def read_file(file_path: str) -> int:
    with open(path, "r") as f:
        text: str = f.readline().rstrip()
        pattern: str = f.readline().rstrip()
        return text, pattern


path = "C:/Users/Paul/src/bioinformatics/week1/dataset_2_6(1).txt"
text, pattern = read_file(path)
print(count(text, pattern))