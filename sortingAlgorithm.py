

Skip to content
Using Gmail with screen readers

Conversations
5.18 GB (34%) of 15 GB used
Manage
Terms · Privacy · Program Policies
Last account activity: 3 hours ago
Details

import math

# always provide a beforeString and an afterString such as beforeString < afterString
smallestLetter = '0'
largestLetter = 'z'
defaultStep = 1
middle = "MIDDLE"

"""
0,....,9,
:
;
<
? 
@
A , ..., Z
[
\
]
^
-
'
a, ..., z  #74
"""

class InsertSortedStrings:
    def __init__(self, beforeString, afterString, defaultStep, middle, elements):
        self.beforeString = beforeString
        self.afterString = afterString
        self.defaultStep = defaultStep # when we add elements between an empty and a non empty string we take a default step instead of the middle
        self.m = 75                    ###
        self.beginString = "N"         ###
        self.middle = middle           ###  
        if elements < 1:
            raise ValueError("number of elements must be at least one")
        self.elements = elements

    # general functions
    def value (self, char):
        return ord (char) - ord (smallestLetter)
    def character (self, value):
        return chr (value+ord(smallestLetter))
    def maxDistance (self):
        return ord (largestLetter) - ord (smallestLetter)
    def distance(self, beforeLetter, afterLetter): # if two letters have negative distance then the distance is replaced with self.m + abs(dis)
        if beforeLetter == afterLetter:
            dis = 0
        else:
            dis = self.value (afterLetter)-self.value (beforeLetter)
        return dis

    # test case 3
    def insertOneBefore(self, afterString, defaultStep): # insert closer to the afterString string than the middle
        k = len(afterString)
        beforeString = smallestLetter*k
        distance = self.stringsDistance(beforeString, afterString)
        newL = ""
        if distance > defaultStep:
            d = distance - defaultStep
            lis = []
            for i in range(0,k):
                k = k - 1
                currBase = self.m**k
                result = float(d)/currBase
                r = math.floor(result)
                d = d - r*currBase
                if r == self.m:
                    lis.append(smallestLetter)
                else:
                    lis.append(self.character(r))
            for ll in lis:
                newL = newL + ll
        else:
            d = math.ceil(self.stringsDistance(beforeString, afterString)/2.0)
            lis = []
            for i in range(0,k):
                k = k - 1
                currBase = self.m**k
                result = float(d)/currBase
                r = math.floor(result)
                d = d - r*currBase
                if r == self.m:
                    lis.append(smallestLetter)
                else:
                    lis.append(self.character(r))
            for ll in lis:
                newL = newL + ll
        return newL

    # test case 2
    def insertOneAfter(self, beforeString, defaultStep): # insert closer to the beforeString than the middle using the defaultstep
        k = len(beforeString)
        afterString = largestLetter*k
        distance = self.stringsDistance(beforeString, afterString)    
        newL = ""
        if distance > defaultStep:
            d = defaultStep
            lis = []
            for i in range(0,k):
                k = k - 1
                currBase = self.m**k
                result = float(d)/currBase
                r = math.floor(result)
                d = d - r*currBase
                if r == self.m:
                    lis.append(smallestLetter)
                else:
                    lis.append(self.character(r))
            for ll in lis:
                newL = newL + ll
        else:
            d = math.ceil(self.stringsDistance(beforeString, afterString)/2.0)
            lis = []
            for i in range(0,k):
                k = k - 1
                currBase = self.m**k
                result = float(d)/currBase
                r = math.floor(result)
                d = d - r*currBase
                if r == self.m:
                    lis.append(smallestLetter)
                else:
                    lis.append(self.character(r))
            for ll in lis:
                newL = newL + ll
        return newL

    # tested - case1
    def stringsDistance(self, beforeString, afterString): # both strings have to have the same length
        nn = 0
        next = 0
        po = 0
        for l in range(1,len(beforeString)+1):
            per = self.distance(beforeString[-l],afterString[-l])
            nn = nn + per*self.m**po
            po = po + 1
        return nn

    # tested - case1
    def nexthalf_samelen(self, beforeString, dis):
        k = len(beforeString)
        start = k*smallestLetter
        start_dis = self.stringsDistance(start, beforeString)
        d = start_dis + math.ceil(dis/2.0)
        
        # build a string of len k and distance d
        lis = []
        newL = ""
        for i in range(0,k):
            k = k - 1
            currBase = self.m**k
            result = float(d)/currBase
            r = math.floor(result)
            d = d - r*currBase
            if r == self.m:
                lis.append(smallestLetter)
            else:
                lis.append(self.character(r))
        for ll in lis:
            newL = newL + ll
        if dis%2.0 != 0:
            return newL  
        else:
            return newL + "2"

    # tested - case1
    def nexthalf_difflen(self, beforeString, afterString):
        k1 = len(beforeString)
        k2 = len(afterString)
        if k1<k2:
            beforeString = beforeString + smallestLetter*(k2-k1)
        if k1>k2:
            afterString = afterString + smallestLetter*(k1-k2)

        start = max(k1,k2)*smallestLetter
        start_dis = self.stringsDistance(start, beforeString)

        dis = self.stringsDistance(beforeString, afterString)
        d = start_dis + math.ceil(dis/2.0)

        # build a string of len k and distance d
        lis = []
        newL = ""
        k = len(afterString)
        for i in range(0,k):
            k = k - 1
            currBase = self.m**k
            result = float(d)/currBase
            r = math.floor(result)
            d = d - r*currBase
            if r == self.m:
                lis.append(smallestLetter)
            else:
                lis.append(self.character(r))
        for ll in lis:
            newL = newL + ll
        if dis%2.0 != 0:
            return newL  
        else:
            return newL + "2"

    # tested - case1
    def insertMiddle(self, beforeString, afterString):
        count = 0
        for i,j in zip(beforeString,afterString):
            if i != j:
                break
            count = count + 1

        if count == len(beforeString) & count == len(afterString):
            return "error sequent identical items"
            
        st = beforeString[0:count]
        beforeString = beforeString[count:]
        afterString = afterString[count:]
        
        if len(beforeString) == len(afterString): # check if there is distance
            dis = self.stringsDistance(beforeString, afterString)
            if dis == 0:  # keep the beforestring as newstring and add a letter at it
                newItem = st + beforeString + "N"
                return newItem
            if dis == 1:
                newItem = st + beforeString + "N"
                return newItem
            newItem = st + self.nexthalf_samelen(beforeString, dis)
        else:
            newItem = st + self.nexthalf_difflen(beforeString, afterString) 
        return newItem



    def insertMultipleMiddle(self, beforeString, afterString, elements):
        count = 0
        for i,j in zip(beforeString,afterString):
            if i != j:
                break
            count = count + 1

        if count == len(beforeString) & count == len(afterString):
            return "error sequent identical items"
            
        st = beforeString[0:count]
        beforeString = beforeString[count:]
        afterString = afterString[count:]
        newItemList = []
        
        if len(beforeString) == len(afterString): # check if there is distance
            dis = self.stringsDistance(beforeString, afterString)
            if (dis / float(elements)) > 1: # there is space
                d1 = math.floor(dis / float(elements))
                for elem in range(0, elements):
                     
                    if dis == 0:  # keep the beforestring as newstring and add a letter at it
                        print("dis is 0")
                        newItem = st + beforeString + "N"
                        beforeString = newItem
                        dis = self.stringsDistance(beforeString, afterString)
                        newItemList.append(newItem)
                        continue
                    if dis == 1:
                        print("dis is 1")
                        newItem = st + beforeString + "N"
                        beforeString = newItem
                        dis = self.stringsDistance(beforeString, afterString)
                        newItemList.append(newItem)
                        continue
                    newItem = st + self.nexthalf_samelen(beforeString, (elem + 1)*dis / float(elements))
                    print(newItem, (elem + 1)*dis / float(elements))
                    newItemList.append(newItem)
        else:
            newItem = st + self.nexthalf_difflen(beforeString, afterString)
            beforeString = newItem
            newItemList.append(newItem)
        return newItemList






















    
    def createNew(self):
        if self.beforeString == "":
            if self.afterString == "":
                if self.elements == 1:
                    print(" test case 4: 2 empty stings, enter the pre-selected middle string")
                    return self.middle
                else:
                    print(" test case 5: insert more than 1 elements between 2 empty stings, using the defaultstep")
                    dd = self.stringsDistance(smallestLetter, largestLetter)
                    if self.defaultStep > dd:
                        return "reduce the defaultStep"
                    newIList = []
                    ddn = math.ceil(dd/float(self.elements))
                    first = smallestLetter
                    l = 1
                    for i in range(self.elements):
                        second = self.character( self.value(first) + l*self.defaultStep)
                        l = l + 1
                        newItem = self.insertMiddle(first, second)
                        newIList.append(newItem)
                    return newIList  # return distributed between 0 and z elements
            else:
                if self.elements == 1: # tested - case3
                    print( "tested - case3 - enter 1 element in the middle of 1 given non empty string and the end '' ")
                    newItem = self.insertOneBefore(self.afterString, self.defaultStep)
                    return newItem
                else:
                    print(" test case 6: insert more than 1 elements between 1 empty stings and the self.afterString, using the defaultstep")
                    dd = self.stringsDistance(smallestLetter, self.afterString)
                    if self.defaultStep > dd:
                        return "reduce the defaultStep"
                    newIList = []
                    ddn = math.ceil(dd/float(self.elements))
                    last = self.afterString
                    l = 1
                    for i in range(self.elements):
                        print(char(self.afterString), l*int(self.defaultStep))
                        second = self.character( self.value(last) - l*int(self.defaultStep))
                        print(second, 'jjsjs')
                        l = l + 1
                        newItem = self.insertMiddle(second, last)
                        newIList.append(newItem)
                    return newIList




                
        else:
            if self.afterString == "":
                if self.elements == 1: # test - case 2
                    print( "tested - case2 - enter 1 element in the middle of 1 given non empty string and the end '' ")
                    newItem = self.insertOneAfter(self.beforeString, self.defaultStep)
                else:
                    newItem = ["fgafa"] # a list of distributed between beforeString and z elements
            else:
                if self.elements == 1: # tested - case1
                    print(" tested - case1 - enter 1 element in the middle of 2 given non empty strings")
                    newItem = self.insertMiddle(self.beforeString, self.afterString)
                else:
                    newItem = self.insertMultipleMiddle(self.beforeString, self.afterString, self.elements) # a list of distributed between beforeString and afterString elements
            return newItem

########### test cases ####################
# tested - case1 - enter 1 element in the middle of 2 given non empty strings
# tested - case2 - enter 1 element between 1 given non empty string and the end "", using the default step that counts backward from the largest string positions or enter it in the middle if the default step is higher than the distance between the non empty string and the largest string
# tested - case3 - enter 1 element between 1 given non empty string and the begging  "", using the default step that counts from the smallest string and after positions or enter it in the middle if the default step is higher than the distance between the non empty string and the smallest string
# tested - case 4: 2 empty stings, enter the pre-selected middle string
# tested - case 5: insert more than 1 elements between 2 empty stings, using the defaultstep

##############################################

beforeString = "" #, "AAA", "ZZ", "K", "HBK", "HKKLIOMNO", "12a", "", ""]
afterString = "BHJ" #, "BHJ", "", "L", "HBKIKAL", "HKKM", "", "[^a",""]
elements = 23   # number of inserts

newItem = InsertSortedStrings(beforeString, afterString, defaultStep, middle, elements).createNew()  # test ("AD", "BA") should return 23
print(newItem)
lexorank.txt
Displaying lexorank.txt.