# def sum_nestedlist(l):
#     total =  0
#     for j in range(len(l)):
#         if type(l[j]) == list:
#             total += sum_nestedlist(l[j])
#         else:
#             total += l[j]
#     return total
# print(sum_nestedlist([[1, 2, 3], [4, [5, 6]], 7]))



def sr2e(a,ans=0):
    if a==[]:
        return ans
    elif type(a[0]) is list:
        ans1=sr2e(a[0])
        return ans1+sr2e(a[1:])
    else:
        ans=a[0]
        return ans+sr2e(a[1:])
print(sr2e([1,3,1,4]))



