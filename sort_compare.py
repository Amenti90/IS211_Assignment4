import random
import time


def CountTimer():
    s = time.time()
    time.sleep(0.1)
    return (time.time() - s)


# ***********Code for insertion sort *************
def Insertion_Sort(list):
    countertime = 0
    for i in range(1, len(list)):

        keyvalue = list[i]
        # countertime += CountTimer()
        k = i - 1
        while k >= 0 and keyvalue < list[k]:
            # time.sleep(1) #sleep for 1 second

            list[k + 1] = list[k]
            k = k - 1

        list[k + 1] = keyvalue


# *************************************************

# ************code for shell sort******************
def gaps_Insert(lens):
    # uses the gap sequence 2^k - 1: 1, 3, 7, 15, 31, ...
    alength = lens.bit_length()
    for p in range(alength - 1, 0, -1):
        yield 2 ** p - 1


def shell_sort(lst):
    countertime = 0

    def sortwithgap(gap_value):
        for i in range(gap_value, len(lst)):
            tempvalue = lst[i]
            j = i - gap_value
            while (j >= 0 and tempvalue < lst[j]):
                time.sleep(1)  # sleep for 1 second
                countertime += CountTimer
                lst[j + gap_value] = lst[j]
                j = j - gap_value
            lst[j + gap_value] = tempvalue

    for gps in gaps_Insert(len(lst)):
        sortwithgap(gps)
    # print("Shell Sort took %" + "{:.4f}".format(countertime) +"f seconds to run")


# *************************************************

# *******code for Python sort for  order********
def Python_Sort(list, sort):
    countertime = 0
    if sort == 'asc':
        # time.sleep(1) #sleep for 1 second
        # countertime += CountTimer

        return sorted(list)  # list.sort()
    else:

        # time.sleep(1) #sleep for 1 second
        # countertime += CountTimer

        return list.sort(reverse=True)  # sorted(list,reverse=True)

    # print("Python Sort took %" + "{:.4f}".format(countertime) +"f seconds to run")


# *************************************************

def main():
    datlist = []
    n = 100;
    for j in range(500):
        datlist.append(random.randint(1, 500))

    print('List is : ', datlist)

    print(' ***********Insertion Sort **********')
    Insertion_Sort(datlist)

    print(' After Insertion Sorting')
    print(datlist)
    # print("Insertion Sort took %" + "{:.4f}".format(countertimeIr) +"f seconds to run")

    print('***********Shell Sort **********')
    shell_sort(datlist)

    print(' After Shell Sorting')
    print(datlist)

    print(' ***********Python Sort **********')
    Python_Sort(datlist, 'asc')

    print('After python Sorting in asc order')
    print(datlist)

    Python_Sort(datlist, 'desc')

    print('After python Sorting in desc order')
    print(datlist)


# ***********Calling function**********************
main()
