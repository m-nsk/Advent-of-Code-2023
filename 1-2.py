digits = [
    ["1", "one"],
    ["2", "two"],
    ["3", "three"],
    ["4", "four"],
    ["5", "five"],
    ["6", "six"],
    ["7", "seven"],
    ["8", "eight"],
    ["9", "nine"],
    ["0", "zero"]
    ]
input = open('./input.txt', 'r')

calibration_digits = []

for line in input:
    cal_value = []
    cal_pos = []
    for digit_pair in digits:
        for digit in digit_pair:
            first_index = line.find(digit)
            last_index = line.rfind(digit)
            if first_index == last_index and first_index != -1:
                cal_value.append(digit_pair[0])
                cal_pos.append(first_index)
            if first_index != -1:
                cal_value.append(digit_pair[0])
                cal_value.append(digit_pair[0])
                cal_pos.append(first_index)
                cal_pos.append(last_index)
    calibration_digits.append(int(str(cal_value[cal_pos.index(min(cal_pos))]) + str(cal_value[cal_pos.index(max(cal_pos))])))

print(sum(calibration_digits))
