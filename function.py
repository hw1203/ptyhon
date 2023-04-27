#두 정수를 더한 값을 반환하는 함수 add_numbers를 작성하시오.
def add_numbers(num1, num2):
    result = num1 + num2
    return result

input1 = 30
input2 = 40
add_result = add_numbers(input1, input2)

print(f"{input1} + {input2} = {add_result}")