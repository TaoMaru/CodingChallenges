def count_by(x, n):
    multiples = []
    for multiple in range(1, n+1):
        multiples += [x * multiple]
    return multiples

#print(count_by(1, 3))

def sum_array(arr):
    if arr == None or len(arr) <= 1:
        return 0;
    else:
        arr.remove(max(arr))
        arr.remove(min(arr))
        sum = 0
        for num in arr:
            sum += num
        return sum

#print(sum_array(None))
#print(sum_array([]))
#print(sum_array([5]))
#print(sum_array([1, 2, 3, 4]))

def make_upper_case(s):
    upperS = s.upper()
    return upperS

#print(make_upper_case("hello"))

def simple_multiplication(number):
    if number % 2 == 0:
        return number * 8;
    else:
        return number * 9

#print(simple_multiplication(10))
#print(simple_multiplication(11))

def double_integer(i):
    return i * 2

#print(double_integer(9))

def is_divide_by(number, a, b):
    return number % a == 0 and number % b == 0

#print(is_divide_by(40, 4, 10))
#print(is_divide_by(40, 3, 10))

gameScores = ['1:0','2:0','3:0','4:0','2:1','3:1','4:1','3:2','4:2','4:3']
def points(games):
    score = 0
    for pair in games:
        if int(pair[0]) > int(pair[2]):
            score += 3
        if int(pair[0]) == int(pair[2]):
            score += 1
    return score

#print(points(gameScores))

#filter_list([1,2,'a','b']) == [1,2]
#filter_list([1,'a','b',0,15]) == [1,0,15]
#filter_list([1,2,'aasf','1','123',123]) == [1,2,123]
    
def filter_list(l):
    newList = []
    for item in l:
        if isinstance(item, int):
            newList += [item]
    return newList

#print(filter_list([1, 2, 'a', 'b']))

#1 = 1 (+7)
#3-5 = 8 (+19)
#7-9-11 = 27 (+37)
#13-15-17-19 = 64 (+61)
#21-23-25-27-29 = 125 (+91)
#31-33-35-37-39-41 = 216
# row num * (row num ** 2)
    
def row_sum_odd_numbers(n):
    return n * (n ** 2)

#print(row_sum_odd_numbers(13))

def get_middle(s):
    if len(s) == 1:
        return s
    elif len(s) % 2 == 0:
        return s[len(s) // 2 - 1] + s[len(s) // 2 ]
    else:
        return s[len(s) // 2 ]

#print(get_middle("hello"))
#print(get_middle("even"))
#print(get_middle("A"))
#print(get_middle("of"))
    
