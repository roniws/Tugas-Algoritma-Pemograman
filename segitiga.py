def segitiga(tinggi):
    for i in range(0,tinggi):
        for j in range(0,tinggi-i-1):
            print(end=' ')
        for k in range(0,i+1):
            print('*',end=' ')
        print()

    for x in range(tinggi,0,-1):
        for y in range(tinggi-x,0,-1):
            print(end=' ')
        for z in range(x,0,-1):
            print('*',end=' ')
        print()

segitiga(int(input('masukkan tinggi: ')))
