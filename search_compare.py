import timeit
import random
import time

import random
import time


def CountTimer():
    s = time.time()
    time.sleep(0.1)
    return (time.time() - s)


# Code for Sequencial search
def Sequential_Search(list, ele, lim):
    countertime = 0
    position = 0
    isfound = False

    while position < lim and not isfound:

        # for i in 1000:
        time.sleep(1)  # sleep for 1 second
        countertime += CountTimer()

        if list[position] == ele:  # check for element ids found in list or not
            isfound = True
        else:
            position = position + 1

    countertime = countertime / 100
    print("Search result of value ", ele)
    print("Sequential search took %" + "{:.4f}".format(countertime) + "f seconds to run")

    if isfound:  # Check elemet found or not
        print('Element found ')
        print("Search result for element found at position", position)
    else:
        print('Element not found')

    return isfound, position


# ********************************************************************************

# code for order sequencial search
def order_Sequential_Search(list, ele, n):
    countertime = 0
    position = 0
    isfound = False
    stop = False
    while position < n and not isfound and not stop:

        time.sleep(1)  # sleep for 1 second
        countertime += CountTimer()

        if list[position] == ele:  # check for element ids found in list or not
            isfound = True
        else:
            position = position + 1

            if list[position] > ele:
                stop = True
            else:
                position = position + 1

    countertime = countertime / 100
    print("Search result of value ", ele)
    print("Order_Sequential search took %" + "{:.4f}".format(countertime) + "f seconds to run")

    if isfound == True:  # Check elemet found or not
        print('Element found ')
        print("Search result for element found at position", position)
    else:
        print('Element not found')

    return isfound, position


# *************************************************************************************


# Code for Binary serach iterative
def Binary_Search_Iterative(list, ele, n):
    start = 0
    end = n
    isfound = False
    countertime = 0
    midpoint = (start + end) // 2
    k = -1
    time.sleep(1)  # sleep for 1 second
    countertime += CountTimer()

    if list[midpoint] == ele:
        countertime = countertime / 100
        print("Search result of value ", ele)
        print("Binary search iterative took %" + "{:.4f}".format(countertime) + "f seconds to run")
        isfound = True
        if isfound == True:  # Check elemet found or notp
            print('Element found ')
            print("Search result for element found at position", midpoint)

    else:
        if ele < list[midpoint]:
            while k <= midpoint and not isfound:
                k = k + 1

                if list[k] == ele:
                    countertime = countertime / 100
                    print("Search result of value ", ele)
                    print("Binary search iterative took %" + "{:.4f}".format(countertime) + "f seconds to run")
                    isfound = True
                    print('Element found ')
                    print("Search result for element found at position", k)

                    return isfound


        else:
            while midpoint <= end and not isfound:
                if list[midpoint] == ele:
                    countertime = countertime / 100
                    print("Search result of value ", ele)
                    print("Binary search iterative took %" + "{:.4f}".format(countertime) + "f seconds to run")
                    isfound = True
                    print('Element found ')
                    print("Search result for element found at position", midpoint)

                    return isfound

                    midpoint = midpoint + 1

                if isfound == False:
                    print('Element is not found')
                return isfound

            # code for binary search recursive


def binary_search_recursive(list, first, last, elementvalue):
    countertime = 0
    isfound = False

    if not first < last:
        return isfound

    midvalue = (first + last) // 2
    if list[midvalue] < elementvalue:
        countertime = countertime / 100
        isfound = binary_search_recursive(list, midvalue + 1, last, elementvalue)
        return isfound
    elif list[midvalue] > elementvalue:
        countertime = countertime / 100
        isfound = binary_search_recursive(list, first, midvalue, elementvalue)
        return isfound
    else:
        countertime = countertime / 100
        if elementvalue == midvalue:
            return isfound


def main():
    datalist = []
    n = 10;
    for j in range(500, 1000):
        datalist.append(random.randint(1, 500))
    print('List is : ', datalist)

    print('***********Sequencial search**********')

    print('Enter negative value for search: ')
    inp1 = input()

    print('negative value is : ', inp1)

    Sequential_Search(datalist, int(inp1), n)

    print('\n\nEnter positive value for search: ')
    inp2 = input()
    print('You have enter : ', inp2)
    Sequential_Search(datalist, int(inp2), n)

    print('\n ***********End Sequencial search**********')

    print('\n\n ***********order Sequencial search**********')

    print('Enter negative value for search: ')
    inp3 = input()
    print('negative value is : ', inp3)

    order_Sequential_Search(datalist, int(inp3), n)

    data = []
    data = datalist

    data.sort()
    print('\n\n After Sort List  : ', data)

    print('\n\nEnter positive value for search: ')
    inp4 = input()
    print('You have enter : ', inp4)
    order_Sequential_Search(data, int(inp4), n)

    print('\n ***********End order Sequencial search**********')

    print('\n\n ***********Binary search Iterative**********')

    print('\n\n Sort list')
    # datalistsort=[]
    # datalistsort=
    b = False
    datalist.sort()
    print('\n\n After Sort List  : ', datalist)

    print('Enter negative value for search: ')
    inp5 = input()
    # input=-2
    print('negative value is : ', inp5)

    b = Binary_Search_Iterative(datalist, int(inp5), n)

    if b == None:
        print('Element not found')

    print('\n\nEnter positive value for search: ')
    inp6 = input()
    print('You have enter : ', inp6)
    Binary_Search_Iterative(datalist, int(inp6), n)

    print('\n ***********End Binary_Search_Iterative **********')

    print('\n\n ***********Binary search recursive**********')

    print('\n\n Sort list')
    datalist.sort()
    print('\n\nAfter Sort List  : ', datalist)
    timer = 0
    found = False
    countertime = 0

    datalist = [int(x) for x in datalist]
    element = int(input('\n\nEnter negative value for search: '))

    found = binary_search_recursive(datalist, 0, len(datalist), element)
    time.sleep(1)  # sleep for 1 second
    countertime += CountTimer()
    if found == False:
        print("binary search recursive took %" + "{:.4f}".format(countertime) + "f seconds to run")
        print('Element was not found.')
    else:
        print("Binary search recursive search took %" + "{:.4f}".format(countertime) + "f seconds to run")
        print('Element was found ')

    element = int(input('\n\nEnter positive value for search: '))

    found = binary_search_recursive(datalist, 0, len(datalist), element)
    time.sleep(1)  # sleep for 1 second
    countertime += CountTimer()
    if found == False:
        print("Binary recursive search took %" + "{:.4f}".format(countertime) + "f seconds to run")
        print('Element was not found.')
    else:
        print("Binary search recursive took %" + "{:.4f}".format(countertime) + "f seconds to run")
        print('Element was found ')

    print(' ***********End Binary_Search_recursion **********')


# ***********Calling function**********************
main()

#MANTRA:
# dl program that works > rename variables > dumb down to bare minimum > ask questions only of the dumb down


# # # sequential search
# # def sequential_search (a_list, item):
# #     pos= 0
# #     found= False
# #     begin= timeit.default_timer()
# #
# #     while pos < len(a_list) and not found:
# #         if a_list[pos]== item:
# #             found= True
# #         else:
# #             pos = pos+1
# #
# #     end= timeit.default_timer()- begin
# #     return found, end
# #
# # test_list = [1, 2, 32, 8, 17, 19, 42, 13, 0 ]
# # print (sequential_search(test_list, 3))
# # print (sequential_search(test_list, 13))
#
# #ordered sequential search
# def ordered_sequential_search(a_list, item):
#     pos= 0
#     found = False
#     stop = False
#     while pos<len (a_list) and not stop:
#         if a_list[pos]== item:
#             found = True
#         else:
#             if a_list[pos]> item:
#                 stop= True
#             else:
#                 pos = pos+1
#                 return found
#
# test_list = [1, 2, 32, 8, 17, 19, 42, 13, 0 ]
# # print (ordered_sequential_search(test_list, 3))
# print (ordered_sequential_search(test_list, 13))
#
#
# # binary_search_iterative
#
# def binary_search(a_list, item):
#     first= 0
#     last = len(a_list)-1
#     found= False
#
#     while first <= last and not found:
#         midpoint = (first + last )//2
#         if a_list[midpoint] == item:
#             found = True
#         else:
#             if item< a_list[midpoint]:
#                 last= midpoint-1
#
#     else:
#         first= midpoint+ 1
#     return found
#
# test_list = [1, 2, 32, 8, 17, 19, 42, 13, 0 ]
# print (binary_search(test_list, 3))
# print (binary_search(test_list, 13))
#
#
#
#
#
#
# #binary_search_recursive
#
#
