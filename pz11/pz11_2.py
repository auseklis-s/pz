# with open('text18-23.txt', 'r', encoding='utf-8') as file:
#     content = file.readlines()

a = open('text18-23.txt', 'r', encoding='utf-16')
content = a.readlines()
cont = content[:4]
print(*a)
punctuation = 0
for i in cont:
    for y in i:
        if y in ",.:;?!":
            punctuation +=1
print(punctuation)
