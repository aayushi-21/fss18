from num import Num
from row import rows
import random, math
import re, traceback
samples = 100

class O():
    y = n = 0

    @staticmethod
    def report():
        print("\n# pass= %s fail= %s %%pass = %s%%" % (
            O.y, O.n, int(round(O.y * 100 / (O.y + O.n + 0.001)))))

    @staticmethod
    def k(f):
        try:
            print("\n-----| %s |-----------------------" % f.__name__)
            if f.__doc__:
                print("# " + re.sub(r'\n[ \t]*', "\n# ", f.__doc__))
            f()
            print("# pass")
            O.y += 1
        except:
            O.n += 1
            print(traceback.format_exc())
        return f


def cp(i, l, u):
    if i in range(l, u):
        return i
    elif i >= u:
        return u
    elif i <= l:
        return l

def another(x, t):
    y = cp(math.floor(0.5 + random.random() * len(t)), 0, len(t) - 1)
    if x == y:
        return another(x, t)
    if t[y]:
        return t[y]
    return another(x, t)

def dom(data, row1, row2):
    s1 = 0
    s2 = 0
    n = (len(data.w))
    for c, w in enumerate(data.w):
        a0 = row1[c]
        b0 = row2[c]
        a = Num.numNorm(data.nums[c], a0)
        b = Num.numNorm(data.nums[c], b0)
        s1 = s1 - 10 ^ (w * (a - b) / n)
        s2 = s2 - 10 ^ (w * (b - a) / n)
    return s1 / n < s2 / n


def doms(data,count):
    n = samples
    c = len(data.name)
    title = data.name + ['>dom']
    for r1, row1 in enumerate(data.rows):
        row1.append(0)
        for i in range(n):
            row2 = another(r1, data.rows)
            s = dom(data, row1, row2) and 1 / n or 0
            row1[c] += s
    if(count==1):
        new_header = ' '.join(new_header)
        print(new_header)
        df_all = data.rows
        for s in df_all:
            print(*s)
    else:
        output = sorted(data.rows, key=lambda x: x[-1])
        print("First Ten rows")
        #Printing first 10 rows
        new_header = ' '.join(new_header)
        print(new_header)
        count = 0
        for s in output:
            count += 1
            if(count<=10):
                print(*s)
        #Printing Last ten rows
        print("\n\nLast Ten rows")
        print(new_header)
        allrows = [row for row in output]
        count = len(output)
        for i in range(count-10,count):
            print(*allrows[i])

def mainDom(source,count):
    print(source)
    doms(rows(source),count)

@O.k
def domTest1():
        mainDom("Weather.csv",1)
        
@O.k
def domTest2():
        mainDom("auto.csv",2)
