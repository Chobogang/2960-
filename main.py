n, k = map(int, input().split())
arr = [i for i in range(2, n+1)]
result = [i for i in range(2, n+1)]
k1 = 0

for array in arr :
    num = 1
    while array * num <= arr[-1] :
        # 배수 존재 유무 및 카운팅
        if array * num in result :
            k1 += 1

            if k1 == k :
                print(num * array)
                break
            else :
                result.remove(array * num)
        num += 1
            
    if k1 == k :
        break