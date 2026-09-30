#для каждого элемента проходим всех его правых соседей и считаем меньших
def count_smaller_num(nums):
    n = len(nums)
    counts = [0] * n
    for i in range(n):
        for j in range(i + 1, n):
            if nums[j] < nums[i]:
                counts[i] += 1
    
    return counts
    

a = [5,2,6,1]
print(count_smaller_num(a))
b = [10,9,8,7,6,7,8,9]
print(count_smaller_num(b))




