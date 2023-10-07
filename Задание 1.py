count = 0
while True:
    text = input()
    if "волшебн" in text:
        count += len(text)
    if "Гэндальф" in text:
        break

print(count)