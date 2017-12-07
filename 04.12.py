lines2016 = []
with open("happiness-cantril-ladder.csv", encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines:
        #print(line)
        cells = line.split(',')
        if cells[2] == '2016':
            lines2016.append(cells)
user_country = input()
found_answer = False
for line in lines2016[:15]:
    if line[0] == user_country:
        value = float(line[3],strip())
        print(value)
        found_answer = True
        break
if not found_answer:
    print("It doesn't work")
