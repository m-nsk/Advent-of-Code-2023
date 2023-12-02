input2 = open('./input2.txt', 'r')

r, g, b = "red", "green", "blue"

num_r, num_g, num_b= 12, 13, 14

id_sum = 0

for line in input2:
    parsed = list(enumerate(line.split(' ')))
    i = 0
    valid_line = True
    while i < len(parsed):
        if r in parsed[i][1]:
            if int(parsed[i - 1][1]) > num_r:
                valid_line = False
        if g in parsed[i][1]:
            if int(parsed[i - 1][1]) > num_g:
                valid_line = False
        if b in parsed[i][1]:
            if int(parsed[i - 1][1]) > num_b:
                valid_line = False
        i += 1
    
    if (valid_line):
        id_sum += int(parsed[1][1][:-1])

print(id_sum)