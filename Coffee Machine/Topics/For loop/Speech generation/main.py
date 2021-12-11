textual_nums = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
input_text = input()

for number in input_text:
    print(textual_nums[int(number)])
