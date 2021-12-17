jamDatang = input("Jam Parkir: ")
split_jamDatang = jamDatang.split(':')
jamPulang = input("Jam Pulang: ")
split_jamPulang = jamPulang.split(':')
bayar = 0
biayaPerJam = 3000

for i in range (len(split_jamDatang)):
    split_jamDatang[i] = int(split_jamDatang[i])
for i in range (len(split_jamPulang)):
    split_jamPulang[i] = int(split_jamPulang[i])
jam = split_jamPulang[0]-split_jamDatang[0]
menit = split_jamPulang[1]-split_jamDatang[1]
detik = split_jamPulang[2]-split_jamDatang[2]

if menit < 0:
    jam -= 1
    menit+=60
if detik < 0:
    detik+=60

if jam == 0:
    bayar = biayaPerJam
else:
    bayar = biayaPerJam+ biayaPerJam *(jam - 1)
    if menit > 0 :
        bayar = biayaPerJam * (jam +1)  
    if detik > 0 :
        bayar = biayaPerJam * (jam +1)

print('Jam Datang',(' ')*5,'= %d:%d:%d'%(split_jamDatang[0],split_jamDatang[1],split_jamDatang[2]))
print('Jam Pulang',(' ')*5,'= %d:%d:%d'%(split_jamPulang[0],split_jamPulang[1],split_jamPulang[2]))
print('Lama Parkir',(' ')*4,'= %d:%d:%d'%(jam,menit,detik))
print ('Bayar',(' ')*10,'= %d'%(bayar))