List = [-8, 8, 6.0, 5, 'строка', -3.1]
sum=0
for i in List:
    if type(i)==float or type(i)==int:
        sum+=float(i)
print("%.1f" %(sum))