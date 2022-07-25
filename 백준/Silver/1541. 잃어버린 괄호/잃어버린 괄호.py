str = input()
str = str.split("-")

answer = 0
for i in range(len(str)):
    if str[i].isdigit():
        str[i] = int(str[i])
    else:
        str[i] = str[i].split("+")
        tmp = 0
        for j in range(len(str[i])):
            tmp += int(str[i][j])
        str[i] = tmp

    if i == 0:
        answer = str[i]
    else:
        answer -= str[i]

print(answer)
