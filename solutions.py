def unknown_program():
    a = int(input())
    b = int(input())
    s = a
    j = b
    i = 2
    if a > b:
        if a % b == 0:
            print(a)
        while s % b != 0:
            s = a * i
            i += 1
        print(s)
    elif b > a:
        if b % a == 0:
            print(b)
        while j % a != 0:
            j = b * i
            i += 1
        print(j)
    else:
        print(a)


def multiplication_table():
    a, b, c, d = int(input()), int(input()), int(input()), int(input())
    for i in range(c, d + 1):
        print(i, end="\t")
    print()
    for y in range(a, b + 1):
        print(y, end="\t")
        for r in range(c, d + 1):
            print(r * y, end="\t")
        print()


def average_value():
    # The average value for numbers that divisible by 3 from interval a, b
    a = int(input())
    b = int(input())
    general_sum = 0
    amount_of_numbers = 0
    for i in range(a, b + 1):
        if i % 3 == 0:
            general_sum += i
            amount_of_numbers += 1
    print(general_sum / amount_of_numbers)


def search_repeating_numbers():
    a = [int(i) for i in input().split()]
    a.sort()
    i = 0
    while i < len(a):
        if a.count(a[i]) > 1:
            print(a[i], end=" ")
            i += a.count(a[i])
        else:
            i += 1


def display_sum():
    """the console reads numbers (one per line)
       until the sum of the entered numbers is 0
       and immediately after that it displays the
       sum of the squares of all the numbers read"""
    sum_addition = 0
    sum_square = 0
    while True:
        num = int(input())
        sum_addition += num
        sum_square += (num ** 2)
        if sum_addition == 0:
            print(sum_square)
            break


def known_function():
    n = int(input())
    i = 1
    s = 0
    a = []
    while i <= n:
        for j in range(0, i):
            a.append(i)
        i += 1
    for p in a:
        print(p, end=" ")
        s += 1
        if s == n:
            break


def some_func():
    """reads a list of lst numbers from the first line
    and the number x from the second line, which displays all positions,
    on which the number x occurs in the transferred list lst."""
    lst = [int(i) for i in input().split()]
    x = int(input())
    counter = 0
    if x in lst:
        for j in lst:
            if x == j:
                print(counter)
            counter += 1
    else:
        print("Отсутствует")


# the unusual using of input
def unusual_input():
    n = 0
    for i in range(10):
        n += int(input())
    print(n)


def familiar_app():
    a = []

    while True:
        a.append([l for l in input().split()])
        if a[-1][-1] == "end":
            break
    a.pop()

    for i in range(len(a)):
        for j in range(len(a[i])):
            a[i][j] = int(a[i][j])

    if len(a[0]) > 1 and len(a) == 1:  # matrix 1 x n
        for i in range(len(a) - 1):
            print(a[0][i - 1] + a[0][i - len(a[0]) + 1] + a[0][i] * 2, end=" ")

    if len(a[0]) == 1 and len(a) >= 2:  # matrix n x 1
        for i in range(len(a[0]) - 1):
            print(a[i - 1][0] + a[i - len(a) + 1][0] + a[i][0] * 2)

    if len(a[0]) == len(a):  # matrix 1 x 1 and square matrix
        for i in range(len(a)):
            for j in range(len(a)):
                print(a[i - 1][j] + a[i - len(a) + 1][j] + a[i][j - 1] + a[i][j - len(a) + 1], end=" ")
            print()

    if len(a[0]) > len(a):  # matrix N x M, where N > M
        for i in range(len(a)):
            for j in range(len(a[0])):
                print(a[i][j - 1] + a[i][j - len(a[i]) + 1] + a[i - 1][j] + a[i - len(a) + 1][j], end=" ")
            print()

    if len(a[0]) < len(a):  # matrix N x M, where N < M
        for i in range(len(a)):
            for j in range(len(a[0])):
                print(a[i - 1][j] + a[i][j - 1] + a[i][j - len(a[0]) + 1] + a[i - len(a) + 1][j], end=" ")
            print()


# a unusual using of input 1
def unusual_input1():
    input_sum = 0
    for i in range(int(input())):
        input_sum += int(input())
    print(input_sum)


# a unusual using of input 2
def zero_counter():
    count_zero = 0
    for i in range(int(input())):
        if int(input()) == 0:
            count_zero += 1
    print(count_zero)


def spiral_realization():
    matrix_size = int(input())
    counter = 1
    i, j, t = 0, 0, 0
    p = -1
    q = -2
    w = q
    o = p
    positive_str = matrix_size
    positive_col = matrix_size
    negative_str = -matrix_size
    negative_col = -matrix_size
    array = [[0 for z in range(1, matrix_size + 1)] for v in range(1, matrix_size + 1)]

    while True:

        for j in range(t, positive_str):
            array[i][j] = counter
            counter += 1

        for i in range(i + 1, positive_col):
            array[i][j] = counter
            counter += 1

        for q in range(q, negative_str - 1, -1):
            array[p][q] = counter
            counter += 1

        for p in range(p - 1, negative_col, -1):
            array[p][q] = counter
            counter += 1

        positive_str -= 1
        positive_col -= 1
        j = 0
        t += 1
        i = t
        negative_str += 1
        negative_col += 1
        if negative_str == 0:
            break
        o -= 1
        p = o
        w -= 1
        q = w

    for n in range(len(array)):
        for h in range(len(array)):
            print(array[n][h], end=" ")
        print()


# Function that remove all odd values and even values divide entirely by 2
def modify_list(l):
    i = -1
    while i >= -len(l):
        if l[i] % 2 != 0:
            l.remove(l[i])
        else:
            i -= 1
    for j in range(len(l)):
        l[j] = l[j] // 2
    return l


def update_dictionary(d, key, value):
    if key in d:
        d[key] = d[key] + [value]
    elif key not in d:
        if 2 * key not in d:
            d[2 * key] = [value]
        else:
            d[2 * key] = d[2 * key] + [value]
    return d


def poems():
    poem = input()
    poem_list = poem.lower().split()
    poem_dictionary = dict.fromkeys(poem_list, 0)

    for i in poem_list:
        for j in poem_dictionary:
            if i == j:
                poem_dictionary[j] += 1

    for key in poem_dictionary.keys():
        print(key, poem_dictionary[key])


def decompression():
    with open("dataset_3363_2.txt", "r") as data:
        s = data.readline().strip()
        i = 1
        num_str = ""
        h = ""
        m = s[0]
        while True:

            while s[i].isdigit():
                num_str += s[i]
                i += 1
                if i == len(s):
                    h += (int(num_str) * m)
                    break
            if i == len(s):
                break

            while s[i].isalpha():
                h += (int(num_str) * m)
                m = s[i]
                i += 1
                num_str = ""
    print(h)


def count_word():
    with open("коран.txt", "r") as data:
        general_str = ""

        for line in data:
            general_str += line

        array = general_str.lower().split()
        dictionary = dict.fromkeys(array, 0)

        for i in array:
            if i in dictionary:
                dictionary[i] += 1

        for j in sorted(dictionary.keys()):
            if dictionary[j] == max(dictionary.values()):
                print(j, max(dictionary.values()))
                break


def average_estimating():
    with open("dataset_3363_4.txt", "r") as data:

        array = []
        rating = []
        general = 0
        math = 0
        physics = 0
        russian = 0
        h = 0
        m = 1
        p = 2
        r = 3

        for line in data:
            array += line.strip().split(';')

        for i in array:
            if i.isalpha():
                average = general / 3
                rating.append(average)
                general = 0
            if i.isdigit():
                general += int(i)

        rating.append(general / 3)
        del rating[0]

        for j in range(len(rating)):
            print(rating[j])

        while m < len(array):
            math += int(array[m])
            m += 4
            h += 1
        print(math / h, end=" ")

        while p < len(array):
            physics += int(array[p])
            p += 4
        print(physics / h, end=" ")

        while r < len(array):
            russian += int(array[r])
            r += 4
        print(russian / h, end=" ")


def football():
    n = int(input())
    array = []
    dictionary = {}

    for i in range(n):
        array.append(input())
        array[i] = array[i].split(";")

    for j in range(len(array)):
        for k in range(len(array[j])):
            if array[j][k].isdigit():
                array[j][k] = int(array[j][k])
            else:
                dictionary[array[j][k]] = [0, 0, 0, 0, 0]

    keys = list(dictionary.keys())

    for e in keys:
        for r in range(len(array)):
            if e in array[r]:
                dictionary[e][0] += 1
                if array[r].index(e) == 0:
                    if array[r][1] > array[r][3]:
                        dictionary[e][1] += 1
                    elif array[r][1] == array[r][3]:
                        dictionary[e][2] += 1
                    else:
                        dictionary[e][3] += 1
                else:
                    if array[r][3] > array[r][1]:
                        dictionary[e][1] += 1
                    elif array[r][3] == array[r][1]:
                        dictionary[e][2] += 1
                    else:
                        dictionary[e][3] += 1

    for a in dictionary:
        dictionary[a][4] = dictionary[a][1] * 3 + dictionary[a][2] * 1

    for q, w in dictionary.items():
        print((q + ':'), *w, end='\n')


def something():
    alphabet = input()
    cipher = input()
    encrypt = input()
    decrypt = input()
    dictionary = {}
    s1 = ""
    s2 = ""

    for i in range(len(alphabet)):
        dictionary[alphabet[i]] = cipher[i]

    for j in encrypt:
        if j in dictionary:
            s1 += dictionary[j]

    for t in decrypt:
        for k, v in dictionary.items():
            if t == v:
                s2 += k

    print(s1)
    print(s2)


def navigator():
    n = int(input())
    array = []

    for i in range(n):
        string = input()
        array.append(string.split())

    dictionary = dict.fromkeys(["север", "запад", "юг", "восток"], 0)

    for r in dictionary:
        for j in range(len(array)):
            if r in array[j]:
                dictionary[r] += int(array[j][1])

    print(dictionary["восток"] - dictionary["запад"], dictionary["север"] - dictionary["юг"])


def average_height():
    with open("dataset_3380_5.txt", "r") as data:
    array = []
    counter = 0
    general = 0

    s = data.readlines()

    for h in range(len(s)):
        array.append(s[h].strip().split("\t"))

    for i in range(1, 12):
        for j in array:
            if str(i) in j:
                general += int(j[2])
                counter += 1
        if counter != 0:
            print(str(i), general / counter)
        else:
            print(str(i), "-")
        general = 0
        counter = 0

# K. Оставить первого
r = int(input())
array = [int(i) for i in input().split()[:r]]
n = []

for i in array:
    if i not in n:
        n.append(i)

print(len(n))

for j in n:
    print(j, end=" ")


# K. Оставить первого2
r = int(input())
array = list(map(int, input().split()))
n = []

for i in array:
    if i not in n:
        n.append(i)

print(len(n))

for j in n:
    print(j, end=" ")


# J. Найти среднее
n = int(input())
array_of_n = [float(i) for i in input().split()]
q = int(input())
array_of_q = []
general = 0

for i in range(q):
    array_of_q.append(input().split())

for j in range(q):
    for k in range(int(array_of_q[j][0]), int(array_of_q[j][1]) + 1):
        general = general + (1 / array_of_n[k])
    print("%.6f" % ((int(array_of_q[j][1]) - int(array_of_q[j][0]) + 1) / general))
    general = 0


# K. Оставить первого3
r = int(input())
array = input().split()[:r]
n = []

for i in array:
    i = int(i)
    if i not in n:
        n.append(i)

print(len(n))

for j in n:
    print(j, end=" ")


# K. Оставить первого (предпологаю один из быстрых вариантов)
r = int(input())
array = input().split()[:r]
seen = set()
seen_add = seen.add
b = [x for x in array if not (x in seen or seen_add(x))]
print(len(b))
for i in b:
    print(int(i), end=" ")


# K. Оставить первого (самое быстрое решение)
from collections import OrderedDict
r = int(input())
array = input().split()[:r]
print(len(list(OrderedDict.fromkeys(array))))
for i in list(OrderedDict.fromkeys(array)):
    print(int(i), end=" ")


# J. Найти среднее (вариант по-лучше)
from statistics import harmonic_mean
n = int(input())
array_of_n = [float(i) for i in input().split()[:n]]
q = int(input())
array_of_q = []
for i in range(q):
    array_of_q.append(input().split())
for j in array_of_q:
    print("%.6f" % (harmonic_mean(array_of_n[int(j[0]):int(j[1]) + 1])))


# the important examples
print(dir(math))
print(help(input))



# оставить последнего
n = int(input())
array = [int(i) for i in input().split()]
k = []
i = -1

while i >= -len(array):
    if array[i] not in k:
        k.append(array[i])
        i -= 1
    else:
        i -= 1

k.reverse()
print(len(k))

for j in k:
    print(j, end=" ")


# оставить последнего
r = int(input())
array = input().split()[:r]
array.reverse()
seen = set()
seen_add = seen.add
b = [x for x in array if not (x in seen or seen_add(x))]
print(len(b))
for i in reversed(b):
    print(int(i), end=" ")


# about objects
objects = [1, 2, 1, 5, True, False, True, 'false', [], [1,2], [1,2]]
x = []
for obj in objects:
    x.append(id(obj))
print(x)



x = []
for obj in objects:
    x.append(id(obj))
print(len(set(x)))


# How to count binomial cofficient
n, k = map(int, input().split())
def binom(n, k):
    if k > n:
        return 0
    elif k == 0 and n > k:
        return 1
    elif k == n and k >= 0:
        return 1
    else:
        return binom(n - 1, k) + binom(n - 1, k - 1)
binom(3, 2)



