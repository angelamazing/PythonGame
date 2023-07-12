def my_print(content, count):
    print(content)
    if count == 1:
        return
    my_print(content, count-1)

my_print('ok', 2)

def move_last(lst,max_index):
    for i in range(max_index):
        if lst[i] > lst[i+1]:
            lst[i],lst[i+1] = lst[i+1],lst[i]

def pop_sort(lst):
    for i in range(len(lst)-1,1,-1):
        move_last(lst,i)

a = [123,443,23,44,2,3]

pop_sort(a)
print(a)