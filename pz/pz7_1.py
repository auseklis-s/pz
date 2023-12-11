def evaluate_expression(expression):
    expression = expression.replace(" ", "")

    current_number = 0
    total_sum = 0
    current_sign = 1 

    for i in expression:
        if i.isdigit():
            current_number = current_number + int(i)
        elif i == '+':
            total_sum += current_sign * current_number
            current_number = 0
            current_sign = 1  
        elif i == '-':
            total_sum += current_sign * current_number
            current_number = 0
            current_sign = -1  

    
    total_sum += current_sign * current_number

    return total_sum

expression = "4+7-2-8"
result = evaluate_expression(expression)
print(f"Результат: {result}")
