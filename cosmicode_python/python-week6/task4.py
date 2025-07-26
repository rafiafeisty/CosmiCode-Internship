from collections import Counter,deque,namedtuple,OrderedDict,ChainMap,defaultdict

def counting():
    print("Counting through sequence of items")
    print(Counter(['B','B','A','B','C','A','B','B','A','C']))
    print("\n")
    print("Counting through dictionary")
    print(Counter({'A':3, 'B':5, 'C':2}))
    print("\n")
    print("Counting through arguments")
    print(Counter(A=3, B=5,C=2))
    print("\n")
    print("Counter most common:")
    print(Counter(['B','B','A','B','C','A','B','B','A','C']).most_common(2))

def diction():
    print("making a dictionary through ordered dictionary")
    dictionary=OrderedDict()
    dictionary['a']=1
    dictionary['b']=2
    dictionary['c']=3
    dictionary['d']=4

    for key,value in dictionary.items():
        print(key, value)
    print("\n")
    print("Deleting from the dictionary")
    dictionary.pop('a')
    for key,value in dictionary.items():
        print(key, value)
    print("\n")
    print("Re-inserting in the dictionary")
    dictionary['a']=1
    for key,value in dictionary.items():
        print(key, value)
    print("\n")
    print("Moving value to the end")
    dictionary.move_to_end('b')
    for key,value in dictionary.items():
        print(key, value)


def chain_mapping():
    d1={'a':1, 'b':2}
    d2={'c':3, 'd':4}
    d3={'e':5, 'f':6}

    res=ChainMap(d1,d2,d3)
    print(res)

    dic3 = { 'g' : 5 }

    res = res.new_child(dic3) 
    print ("Displaying new ChainMap : ") 
    print (res)

def named_tuples_def():
    student=namedtuple('Student',['name','age','dob'])
    s=student('alex','18','2541997')

    print("Student age: ",s[1])
    print("name of student: ",s.name)

def queuing():
    de = deque([1,2,3]) 
    print(de)
    print("\n")
    print("Adding value")
    de.append(4)
    print(de)
    print("\n")
    print("Adding value at the left")
    de.appendleft(5)
    print(de)
    print("\n")
    print("deleting value")
    de.pop()
    print(de)
    print("\n")
    print("deleting value at the left")
    de.popleft()
    print(de)
    print("\n")
    print("rotating")
    de.rotate(1)
    print(de)

print("COUNTING")
counting()
print("---------------------------")
print("\n")
print("DICTIONARY")
diction()
print("---------------------------")
print("\n")
print("CHAIN MAPPING")
chain_mapping()
print("---------------------------")
print("\n")
print("NAMED TUPLES")
named_tuples_def()
print("---------------------------")
print("\n")
print("DEQUE")
queuing()