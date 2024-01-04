def avg(**args):
    if not args:
        return 0.0
    total = sum(args)
    average = total/len(args)
    return average

user_input_list = [int(num) for num in input().split()]

result = avg(*user_input_list)
print(f"The average is : {result:.2f}")
    