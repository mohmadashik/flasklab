n = int(input('give n number'))
arr = list(map(int,input().split()))
# arr = sorted(arr)5
# print(arr)
total = sum(arr)
actual_total = (n*(n+1))//2
print(actual_total-total)
# result= None
# for i in range(1,n+1):
#     if i in arr:
#         continue
#     else:
#         result = i
# print(result)
# MissingNumber([3,4,1,2],5)