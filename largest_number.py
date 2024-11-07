









def number_list(n):

    if number_list == 1:
        return 1
    else:
        return number_list * number_list(n - 1)

print(number_list())