text1 = input()
text2 = input()
text3 = input()
len(text1)
maxValue = max(len(text1), len(text2), len(text3))
minValue = min(len(text1), len(text2), len(text3))

value = len(text1) + len(text2) + len(text3) - int(minValue) - int(maxValue)

for i in range(int(maxValue),int(value),int(-minValue)):
    print(i, end="\t")