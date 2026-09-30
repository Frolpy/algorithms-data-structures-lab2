#Бинарный поиск количества положительных и отрицательных чисел
def binary_count(arr):
    start = 0
    end = len(arr)
    
    #бинарный поиск первого элемента >= 0 (граница отрицательных)
    while start < end:
        mid = start + (end - start)//2
        if arr[mid] < 0:
            start = mid + 1
        else:
            end = mid
    
    first_non_neg = start
    
    #бинарный поиск первого элемента > 0 (граница положительных)
    left, right = 0, len(arr)
    while left < right:
        mid = left + (right - left)//2
        if arr[mid] <= 0:
            left = mid + 1
        else:
            right = mid
            
    first_positive = left
    
    negatives = first_non_neg
    positives = len(arr) - first_positive
    
    
    if positives > negatives:
        return positives
    elif negatives > positives:
        return negatives
    else:
        return 0
    
a = [-2,-1,0,1,1,2,3,4]
b = [-1,0,0,0,0,0,1,2,3]

print(binary_count(a))
print(binary_count(b))
    