#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        j = 1
        try:
            new_list.append(my_list_1[i] / my_list_2[i])
        except ZeroDivisionError:
            print("division by 0")
            j = 0
            continue
        except TypeError:
            print("wrong type")
            j = 0
            continue
        except IndexError:
            print("out of range")
            j = 0
            continue
        finally:
            if not j:
                new_list.append(j)
    return new_list
