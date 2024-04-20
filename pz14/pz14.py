import re

count1 = 0
count2 = 0

with open ('pz14/ip_address.txt' , 'r') as file1, open('pz14/output_file1.txt' , 'w') as file2, open('pz14/output_file2.txt', 'w') as file3:
    for i in file1:
        if re.match(r'\d{1,3}\.\d{1,3}', i):
            test = i.strip().split('.')
            if int(test[0])>0 and int(test[1])>0:
                file2.write(i)
                count1 += 1
            else:
                file3.write(i)
                count2 += 1

print(count1)
print(count2)