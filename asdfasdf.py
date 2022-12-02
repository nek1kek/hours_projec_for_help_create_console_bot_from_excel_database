def to_3(a):
    st = ''
    while a > 0:
        st = str(a % 3) + st
        a //= 3
    return st


step_from_answer = to_3(int(input()))

if (step_from_answer.count('2') > 0 or step_from_answer.count('1') == 0):
    print('NO')
else:
    print('YES')
    a = []
    for i in range(len(step_from_answer) - 1, -1, -1):
        if step_from_answer[i] != '0':
            a.append(str(len(step_from_answer) - i - 1))
    print(len(a))
    print(' '.join(a))
