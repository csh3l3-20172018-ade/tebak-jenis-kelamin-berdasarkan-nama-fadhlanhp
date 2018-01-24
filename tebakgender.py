def array(enternama):
    lk=['d','o','b']              #isi array lk dan pr yang nantinya digunakan untuk membaca dan menghitung file yang muncul
    pr=['a','i','u','e','t','l']
    

    perempuan = 0
    pria = 0

    for x in enternama:
        if x in lk:
            pria=pria+1             #menghitung jumlah array yang muncul pada x ,dan +1 jika isi array muncul pada x
        if x in pr:
            perempuan=perempuan+1


    print ("Jenis kelamin")
    if pria>perempuan:
        print("pria")    #output nilai variabel tertinggi
    if perempuan>pria:
        print("perempuan")

nama=input("masukan nama :")
array(nama)
