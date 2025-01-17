import os
cur = os.path.abspath(__file__)
file_path = os.path.dirname(cur).replace("\\", "/") + '/ex3.txt'

def word_count(file_path):
    result = {}
    with open(file_path, 'r') as f:
        for line in f:
            words = line.split()
            words = [word.lower() for word in words]
            for word in words:
                if word in result:
                    result[word] += 1
                else:
                    result[word] = 1
    return result

if __name__ == '__main__':
    print(word_count(file_path))
