# НЕЛЬЗЯ ИСПОЛЬЗОВАТЬ EVAL! максимум для тестирования
# Задача 2. Напишите программу вычисления арифметического выражения заданного строкой. Используйте операции +,-,/,*. приоритет операций стандартный.
# *Пример:* 
# 2+2 => 4; 
# 1+2*3 => 7; 
# 1-2*3 => -5;
# - Добавьте возможность использования скобок, меняющих приоритет операций.
#     *Пример:* 
#     1+2*3 => 7; 
#     (1+2)*3 => 9;

def calculate(exp):
    def format(res):
        if '.' in res:
            try:
                res = float(res)
            except ValueError:
                pass
        else:
            try:
                res = int(res)
            except ValueError:
                pass
        return res
    def splitter(item, op):
        mul = item.split(op)
        if len(mul) == 2:
            for x in ['*', '/', '+', '-']:
                if x in mul[0]:
                    mul = [mul[0].split(x)[1], mul[1]]
                if x in mul[1]:
                    mul = [mul[0], mul[1].split(x)[0]]
        elif len(mul) > 2:
            pass
        else:
            pass
        for x in range(len(mul)):
            mul[x] = format(mul[x])
        return mul
    exp = exp.replace(' ', '')
    if '=' in exp:
        res = exp.split('=')[1]
        res = format(res)
        exp = exp.replace('=%s' % res, '')
    while '/' in exp:
        if '/' in exp:
            itm = splitter(exp, '/')
            res = itm[0] / itm[1]
            exp = exp.replace('%s/%s' % (str(itm[0]), str(itm[1])), str(res))
    while '*' in exp:
        if '*' in exp:
            itm = splitter(exp, '*')
            res = itm[0] * itm[1]
            exp = exp.replace('%s*%s' % (str(itm[0]), str(itm[1])), str(res))
    while '+' in exp:
        if '+' in exp:
            itm = splitter(exp, '+')
            res = itm[0] + itm[1]
            exp = exp.replace('%s+%s' % (str(itm[0]), str(itm[1])), str(res))
    while '-' in exp:
        if '-' in exp:
            itm = splitter(exp, '-')
            res = itm[0] - itm[1]
            exp = exp.replace('%s-%s' % (str(itm[0]), str(itm[1])), str(res))
    return format(exp)
