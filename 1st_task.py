stars = list(input())
result = []
for _ in range(2):
    data = input()
    for symb_num in range(len(stars), len(data) + 1):
        break_check_1 = False
        for iters in range(len(data) - symb_num + 1):
            count = 0
            break_check = False
            for symb in data[iters:symb_num+iters]:
                if symb in stars:
                    count += 1
                if count == 3:
                    result.append(str(len(data[iters:symb_num+iters])))
                    break_check = True
                    break
            if break_check:
                break_check_1 = True
                break
        if break_check_1:
            break
print(' '.join(result))
