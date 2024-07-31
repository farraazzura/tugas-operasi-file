print ("Selamat datang di Program Biodata Zuraa")
print ("=================================")

def baca_file(nama_file):
    biodata = open(nama_file, "r")
    print(biodata.read())
    biodata.close()

baca_file("biodata.txt")
print("Tambahkan Biodata !")

def tulis_file(nama_file):
    nama = input("Nama: ")
    umur = input("Umur: ")
    alamat = input("Alamat: ")
    teks = "\nNama: {}\nUmur: {}\nAlamat: {}\n---".format(nama, umur, alamat)
    biodata = open(nama_file, "a")
    print(biodata.write(teks))
    biodata.close()

tulis_file("biodata.txt")
print("Biodata Behasil Di Tambahkan")