input = r"D:\GitHub\AWSCC-CodeQuest-Backend\backend\day-11\names.txt"
output= r"D:\GitHub\AWSCC-CodeQuest-Backend\backend\day-11\sorted_names.txt"

with open(input, 'r') as file:
    content = file.readlines()

sortedNames = sorted(content)

with open(output, 'w') as file:
    for name in sortedNames:
        file.write(name)