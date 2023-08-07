
while True:
    word = input('请输入一个单词：')
    if word.isalpha():
        first_char = word[0]
        second_to_last_char = word[1:]
        output = second_to_last_char + '-' + first_char + 'y'

        print(output)
        break
    else:
        print('重新输入')


