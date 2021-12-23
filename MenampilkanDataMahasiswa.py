from datetime import date

dataNama = []
dataNim = []
dataThnLahir = []
stop = False
foo = 0
class dataMahasiswa:
    def __init__(self,nama,nim,ThnLahir):
        self.nama = nama
        dataNama.append(nama)
        self.nim = nim
        dataNim.append(nim)
        self.ThnLahir = ThnLahir
        dataThnLahir.append(ThnLahir)
    def tampilMhs():
        n = 0
        for i in range (foo):
            n+=1
            hari = date.today()
            umur = hari.year - dataThnLahir[i]
            print(f'mahasiswa ke{n}......\nNama = {dataNama[i]}\nNIM = {dataNim[i]}\nTahun Lahir = {dataThnLahir[i]}\nUmur = {umur}')
while(not stop):
    inputNama = input('masukkan nama mahasiswa = ')
    inputNim = input('masukkan NIM = ')
    inputThnLahir = int(input('masukkan Tahun Lahir = '))
    mahasiswa = dataMahasiswa(inputNama,inputNim,inputThnLahir)
    ulang = input('apakah ingin input ulang (y/t) = ')
    foo +=1
    if ulang == 't':
        stop = True
dataMahasiswa.tampilMhs()