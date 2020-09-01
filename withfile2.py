
def print_freq(input_string):
    d = {}
    list_freq = []
    max_value = 0
    lowercase = input_string.lower().split()
    for x in lowercase:
        c = lowercase.count(x)
        d.update({x: c})
        if c > max_value:
            max_value = c
    for key, value in d.items():
        if value == max_value:
            list_freq.append(key)
    print(min(list_freq), max_value)



with open("/home/svetlana/Downloads/dataset_3363_3.txt") as file:
    text = str()
    for line in file:
        text += line
    print_freq(text)



