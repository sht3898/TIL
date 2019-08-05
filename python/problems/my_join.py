def my_join(target, word):
    result = ''
    for idx in range(len(target)):
        if idx == len(target)-1:
            result += target[idx]
        else:
            result += target[idx] + word
    return result

print(my_join('배고파','.'))

