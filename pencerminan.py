nilXY = input('Masukkan nilai X dan Y: ')
split_XY = nilXY.split(',')
for i in range(len(split_XY)):
    split_XY[i]=int(split_XY[i])
print('pencerminan sumbu x : %d,%d'%(split_XY[0],-abs(split_XY[1])))
print('pencerminan sumbu Y : %d,%d'%(-abs(split_XY[0]),split_XY[1]))