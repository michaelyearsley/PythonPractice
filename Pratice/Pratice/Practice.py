def avgList(nl):
    sum = 0
    count=0
    for x in nl:
        sum= sum +x
        count+=1
    avg = sum/count
    return round(avg, 2)
def avgOddList(nl):
    sum = 0
    count=0
    for x in nl:
        if x%2 != 0:
            sum= sum +x
            count+=1
    avg = sum/count
    return round(avg, 2)
def avgEvenList(nl):
    sum = 0
    count=0
    for x in nl:
        if x%2 == 0:
            sum= sum +x
            count+=1
    avg = sum/count
    return round(avg, 2)
def LargeList(nl):
    large = nl[0]
    for x in nl:
        if x > large:
            large = x
    return large
def smallList(nl):
    small = nl[0]
    for x in nl:
        if x < small:
            small = x
    return small
#list
lt = [5, 6, 4, 6, 7,9, 7]
print(avgList(lt))
print(avgOddList(lt))
print(avgEvenList(lt))
print(LargeList(lt))
print(smallList(lt))
def dictionary(AD):
    dict = {}
    for x in AD:
        if x in dict:
            dict[x] = dict[x]+1
        else:
             dict[x]=1
    return dict
def freqDict(AD):
    dict = {}
    for x in AD:
        if x in dict:
            dict[x] = dict[x]+1
        else:
             dict[x]=1
    freq = 0
    for x in dict:
        if freq == dict[x]:
            return " Multiple frequent numbers"
        if freq < dict[x]:
            freq = x
    return freq

dl = [1, 3, 5, 9, 8, 4, 6, 5, 4, 2, 3, 6, 5, 8, 4, 6, 6,]
print(dictionary(dl))
print ("The most Fequent Number is:", freqDict(dl))