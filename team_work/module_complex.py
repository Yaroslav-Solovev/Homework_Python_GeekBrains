def merge_element(expression, count):
    expression[count-1] = expression[count-1] + expression[count]
    expression.pop(count)
    return expression

def preparation(expression):
    count = 1
    while " " in expression:
        expression = expression.replace(" ", "")
    expression = list(expression)
    while count < len(expression):
        if expression[count].isdigit() and expression[count-1].isdigit():
            merge_element(expression, count)
        elif expression[count] == "." and expression[count-1].isdigit():
            merge_element(expression, count)
        elif expression[count].isdigit() and "." in expression[count-1]:
            merge_element(expression, count)
        elif (expression[count] == 'i' or expression[count] == 'j') and (expression[count-1].isdigit() or "." in expression[count-1]):
            expression[count-1] = expression[count-1] + 'j'
            expression.pop(count)
            count += 2
        else:
            count += 1
    count = 3
    while count < len(expression):
        if (('i' in expression[count]) or ('j' in expression[count])) and expression[count-3] == "(" and expression[count+1] == ")":
            expression[count-2] = expression[count-2] + expression[count-1] + expression[count]
            expression.pop(count)
            expression.pop(count-1)
            count += 3
        else:
            count += 1
    count = 1
    while count < len(expression):
        if 'j' in expression[count] and expression[count-1] == "(" and expression[count+1] == ")":
            expression.pop(count+1)
            expression.pop(count-1)
            count += 2
        else:
            count += 1
    return expression

def priority(oper):
    if oper == '*':
        return 2
    elif oper == '/':
        return 2
    elif oper == '+':
        return 1
    elif oper == '-':
        return 1
    elif oper == '(':
        return 0

def is_number_f(str):
    try:
        float(str)
        return True
    except ValueError:
        return False

def is_number_c(str):
    try:
        complex(str)
        return True
    except ValueError:
        return False

def opz(expression):
    result=[]
    oper_stack=[]
    for i in expression:
        if is_number_f(i):
            result.append(float(i))
        elif is_number_c(i):
            result.append(complex(i))
        elif i in ['*','/','+','-']:
            token_tmp = ''
            if len(oper_stack) > 0:
                token_tmp = oper_stack[len(oper_stack) - 1]
                while (len(oper_stack) > 0 and token_tmp != '('):
                    if (priority(i) <= priority(token_tmp)):
                        result.append(oper_stack.pop())
                        if len(oper_stack) > 0:
                            token_tmp = oper_stack[len(oper_stack) - 1]
                    else:
                        break     
            oper_stack.append(i)
        elif i == '(':
            oper_stack.append(i)
        elif i == ')':
            token_tmp = oper_stack[len(oper_stack) - 1]
            while token_tmp != '(':
                result.append(oper_stack.pop())
                token_tmp = oper_stack[len(oper_stack) - 1]              
                # if len(oper_stack) == 0:
                #     raise RuntimeError('V virajenii propushena (') 
                if token_tmp == '(':
                    oper_stack.pop()
    while len(oper_stack) > 0:
        result.append(oper_stack.pop())
    return result

def count_opz(list):
    final_result = []
    for item in list:
        if type(item) == complex or type(item) == float:
            final_result.append(item)
        else:
            left_oper = final_result.pop()
            right_oper = final_result.pop()
            if item == "-":
                final_result.append(right_oper - left_oper)
            elif item == "+":
                final_result.append(right_oper + left_oper)
            elif item == "*":
                final_result.append(right_oper * left_oper)
            elif item == "/":
                final_result.append(right_oper / left_oper)
            elif item == "^":
                final_result.append(right_oper ** left_oper)
    return final_result[0]










