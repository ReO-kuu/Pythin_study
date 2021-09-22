def add(num1, num2):
    result = num1 + num2

    return result

def sub(num1, num2):
    result =num1 - num2

    return result

def mul(num1, num2):
    result = num1 * num2

    return result

def div(num1, num2):
    if num2 == 0:
        result = 0
    else:
        result = num1 / num2
    return result

def rem(num1, num2):
    if num2 == 0:
        result = num1
    else:
        result =num1 % num2

        return result

input_num1 = int(input("1つ目の整数："))
input_num2 = int(input("2つ目の整数："))

add_result = add(input_num1, input_num2)
print(input_num1, "+", input_num2, "=", add_result, sep="")

sub_result = sub(input_num1, input_num2)
print(input_num1, "-", input_num2, "=", sub_result, sep="")

div_result = div(input_num1, input_num2)
print(input_num1, "*", input_num2, "=", div_result, sep="")

rem_result = rem(input_num1, input_num2)
print(input_num1, "%", input_num2, "=", rem_result, sep="")