x = input("nilai A.absis , A.ordinat:")
y = input("nilai B.absis, B.ordinat: ")
split_x = x.split(',')
split_y = y.split(',')

for i in range (len(split_x)):
    split_x[i] = int(split_x[i])
for j in range (len(split_y)):
    split_y[j] = int(split_y[j])
T_absis = (split_x[0]+split_y[1])/2
T_ordinat = (split_x[1]+split_y[1])/2
print(f"nilai titik tengahnya (T) adalah : {T_absis},{T_ordinat}")