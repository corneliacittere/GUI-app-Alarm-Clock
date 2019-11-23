
def func(a):
    a = a.partition(':')
    h, m = a[0], a[2]
    print(a)

    if h.isdigit() and m.isdigit():
        h, m = int(h), int(m)
        if 0 <= h < 24 and 0 <= m < 60:
            h, m = str(h), str(m)
            if len(h) == 1:
                h = '0' + h
            if len(m) == 1:
                m = '0' + m
            print(h + ':' + m)
        else:
            print('PLEASE ENTER THE CORRECT VALUE OF HOURS AND MINUTES')
    else:
        print('PLEASE ENTER DIGITS ONLY')

