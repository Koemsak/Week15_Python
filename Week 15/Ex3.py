studentsDic1 = eval(input())
studentsDic2 = eval(input())
# 1 copy the dic 1
mergedDictionary = studentsDic1.copy()
# 1 copy the dic 1
for dic2Class in (studentsDic2):
    dic2Number = studentsDic2[dic2Class]
    if dic2Class in studentsDic1:
        mergedDictionary[dic2Class] += dic2Number
    else:
        mergedDictionary[dic2Class] = dic2Number
print(mergedDictionary)