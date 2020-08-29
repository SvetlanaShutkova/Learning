answer = str()
with open('dataset_3363_2.txt') as text:
    string = text.readline()
    number, letter = str(), str()
    for symbol in string:
        if symbol.isalpha():
            if letter:
                answer += letter * int(number)
            letter = symbol
            number = str()
        else:
            number += symbol
    answer += letter * int(number)

with open('dataset_3363_2.txt', 'w') as text:
    text.write(answer)


