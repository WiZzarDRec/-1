n = int(input())
word = input("Введите ключевое слово ")
count = 0
for i in range (1, n):
    text = input()
    if "забыл" in text or word in text:
        count += 1
if count<n/2:
    print("НЕ ТАК И МНОГО")
else:
    print("ВСЕ РАВНО НИЧЕГО СТРАШНОГО")
print(count+n)