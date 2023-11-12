# l = [11, 12, 13, 14]
# x = iter(l)
# x2 = iter(l)
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x2))

# for i in l:
#     print(i)

# ==============================================================

# def generator(n):
#     i = 0
#     while i < n:
#         yield i
#         i += 1


# for x in generator(5):
#     print(x)

# iterator = iter(generator(3))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

# ==============================================================

l = []
for i in range(11):
    if i % 2 != 0:
        l.append(i)

print(l)

l2 = [bilangan for bilangan in range(11) if bilangan % 2 != 0]
print(l2)

d = {bilangan: bilangan + 1 for bilangan in range(11) if bilangan % 2 == 0}
print(d)
