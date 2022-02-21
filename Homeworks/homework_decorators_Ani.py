# """decorators"""
#
# def decorated_number(myfunc):
#     def mult_number(n):
#         res = myfunc(n)
#         return  10 * res
#     return mult_number
#
# @decorated_number
# def number(n):
#     return n
#
# nmb = int(input('n = '))
# print(number(nmb))
#
#
# def check_type(myfunc):
#     def checking(_a,_b):
#         if type(_a) == int and type(_b) == int:
#             return add_integers
#         raise TypeError
#     return checking
#
# @check_type
# def add_integers(_a, _b):
#     return  _a + _b
#
# print(add_integers(2, 2))
#
# """Recursion_sum_of_list"""
# def sum_of_list_recursion(lst):
#     if len(lst) == 1:
#         return lst[0]
#     return lst[0] + sum_of_list(lst[1:])
#
# l = [1,2,1,4,3,5,3,5]
# res = sum_of_list_recursion(l)
# print(res)
#
# """Geometric sum of number"""
# SUM(a * (r ** k))

def geometric_sum_of_number(_n, a = 1, r = 2):
    if _n == 0:
        return 0
    return a * (r ** _n) + geometric_sum_of_number(_n - 1, a, r)

n = int(input("number = "))
res = geometric_sum_of_number(n, 1, 2)
print(res)


