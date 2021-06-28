palindrome_list = list()
while True:
    current_int = input()
    if current_int == '0':
        break
    palindrome_list.append(current_int)

def check_palindrome(string):
    return string == string[::-1]

answer_list = ["yes" if check_palindrome(string) else "no" for string in palindrome_list]

for answer in answer_list:
    print(answer)