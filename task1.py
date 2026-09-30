#Бинарный поиск
def binary_search(arr, key):
    start = 0
    end = len(arr) - 1
    
    while start <= end:
        mid = start + (end-start)//2
        midVal = arr[mid]
        if midVal == key:
            return mid
        if midVal > key:
            end = mid - 1
        else:
            start = mid + 1
    
    arr.insert(start, key)#Если элемент не найден, вставляем его в массив
    return start
    

a = [1, 2, 3, 4, 5, 6, 7]
print(binary_search(a,3))
print(binary_search(a,8))