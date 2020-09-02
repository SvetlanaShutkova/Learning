def mean_rows(students):
    students = students.split(';')
    a = []
    n = 0
    for x in students:
        if x.isdigit():
            a.append(x)
    for i in a:
        n += int(i)
    return n / len(a)


def mean_columns(z):
    print(z)
    subject = []
    sum_marks = 0
    amount_marks = 0
    for mark in z:
        subject.append(mark)
    for v in subject:
        amount_marks += 1
        sum_marks += int(v)
    return float(sum_marks / amount_marks)


with open('dataset_3363_4(3).txt') as file:
    with open("456", "w") as file_2:
        text = list()
        for line in file:
            file_2.write(str(mean_rows(line[:-1] if "\n" in line else line)) + "\n")
            text += line[:-1].split(';') if "\n" in line else line.split(';')
        file_2.write(str(mean_columns(text[1::4])) + " ")
        file_2.write(str(mean_columns(text[2::4])) + " ")
        file_2.write(str(mean_columns(text[3::4])))

