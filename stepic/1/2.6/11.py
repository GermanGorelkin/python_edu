n = int(input())

matrix = [[None for j in range(n)] for i in range(n)]
rout_list = ['r', 'd', 'l', 'u']
rout = 0
cnt_step_by_rout = n
cnt_change_rout = 1
n *= n
num_print = 1
x, y = 0, 0
while n > num_print - 1:
    for i in range(cnt_step_by_rout):
        matrix[y][x] = num_print
        # print(num_print, rout_list[rout], cnt_step_by_rout, x, y)

        if rout_list[rout] == 'r':
            if i < cnt_step_by_rout - 1:
                x += 1
            else:
                y += 1
        elif rout_list[rout] == 'd':
            if i < cnt_step_by_rout - 1:
                y += 1
            else:
                x -= 1
        elif rout_list[rout] == 'l':
            if i < cnt_step_by_rout - 1:
                x -= 1
            else:
                y -= 1
        elif rout_list[rout] == 'u':
            if i < cnt_step_by_rout - 1:
                y -= 1
            else:
                x += 1

        num_print += 1
    if rout == len(rout_list) - 1:
        rout = 0
    else:
        rout += 1
    cnt_change_rout += 1
    if cnt_change_rout % 2 == 0 and cnt_change_rout != 0:
        cnt_step_by_rout -= 1

for i in matrix:
    print(' '.join(map(str, i)))
