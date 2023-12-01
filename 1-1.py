digits = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
input = open('./input.txt', 'r')

calibration_values = []

for line in input:
    cal_value = []
    for char in line:
        if char in digits:
            cal_value.append(char)
    if len(cal_value) == 1:
        calibration_values.append(int(cal_value[0] + cal_value[0]))
    else:
        calibration_values.append(int(cal_value[0] + cal_value[-1]))

print(sum(calibration_values))