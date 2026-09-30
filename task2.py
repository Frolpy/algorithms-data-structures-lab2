#Ищем пик горного массива
def binary_peak(arr):
    if len(arr) < 3:
        return 'Массив не является горным'
    
    start = 0
    end = len(arr) - 1
    
    while start < end:
        mid = start + (end - start)//2
        midVal = arr[mid]

        if midVal < arr[mid + 1]:
            start = mid + 1 #делаем mid + 1, так как mid точно не пик
        else:
            end = mid
    
    peak = start #start == end - индекс пика
    
    if peak == 0 or peak == len(arr) - 1: #проверяем не находится ли пик в начале или конце массива
        return 'Массив не является горным'
    
    #проверка на монотонность
    for i in range(peak):
        if arr[i] >= arr[i + 1]:
            return 'Массив не является горным'
    
    for i in range(peak, len(arr) - 1):
        if arr[i] <= arr[i + 1]:
            return 'Массив не является горным'
    
    return peak
    

    



a = [1,2,3,4,3,2,1]
print(binary_peak(a))
b = [1,2,3,4,5]
print(binary_peak(b))
c = [1,3,1,2,4,2]
print(binary_peak(c))
d = [1,1,1,1,1,1]
print(binary_peak(d))

