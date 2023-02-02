def __init__(self,num1,num2,op_char):
    response_str = f"The answer to {num1}{op_char}{num2} is:"
    if op_char == '+':
	    return answer + num1+num2
	else if op_char == '-':
		return answer + num1-num2
	else if op_char == '*':
		return answer + num1*num2
    else if op_char == '/' or op_char == '\\':
	    if num2 != 0:
			return answer + num1/num2
		return "Sorry, you can't divide by 0."
	#todo: math powers
