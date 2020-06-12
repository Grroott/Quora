no=int(input())
v=(list(map(str,input().split(" ")))[:] for _ in range(no))
for i in v:

    try:
        ans=int(i[0])//int(i[1])
        print (ans)
    except ZeroDivisionError as e:
        print ("Error Code: ",e)
    except ValueError as ee:
        print ("Error Code: ",ee)


# from itertools import product
#
# K,M = map(int,input().split())
# print (type(K))
# print (M)
# N = (list(map(int, input().split()))[1:] for _ in range(K))
# # results = map(lambda x: sum(i**2 for i in x)%M, product(*N))
# print(N)
#
# s='sss r r'
# ss = ''
# count = 0
# for i in s:
#     if i.isspace():
#         count += 1
#     elif count == 1:
#         i = i.upper()
#         count = 0
#     ss += i
# temp=s.upper()
# temp=temp[0:1]
# print (temp)
# print (temp+ss[1:])
