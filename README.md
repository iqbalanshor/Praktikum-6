# Praktikum 6
# Latihan
## Fungsi Lambda
```python
a = lambda x: x**2
b = lambda x, y: math.sqrt(x*2 + y*2)
c = lambda *args: sum(args) / len(args)
d = lambda s: "".join(set(s))
```

## fungsi a
```python
result_a = a(8)
print(result_a)
```

## fungsi b
```python
result_b = b(2, 2)
print(result_b)
```

## fungsi c
```python
result_c = c(2,4,6,8,10)
print(result_c)
```

## fungsi d
```python
result_d = d("M IQBAL AL ANSHORI")
print(*result_d," ")
```
# Praktikum
## Program Data Mahasiswa

![gambar](Screenshot/ss1.png)

- Membuat Dictionary
```python
data_mahasiswa = {}
```
- Menambah Data
```python
def tambah():
    print("Tambah Data")
    nama = input("Nama\t\t: ")
    nim = int(input("NIM\t\t: "))
    tugas = int(input("NIlai Tugas\t: "))
    uts = int(input("Nilai UTS\t: "))
    uas = int(input("Nilai UAS\t: "))
    nilaiakhir = (tugas * 0.3 + uts * 0.35 + uas * 0.35)
    data_mahasiswa[nama] = nim, tugas, uts, uas, nilaiakhir
```
- Menampilkan Data
```python
def tampilkan():
    if data_mahasiswa.items():
        print("===================================| Daftar Nilai |===================================")
        print("______________________________________________________________________________________")
        print("|  No  |      NAMA      |      NIM         |    TUGAS   |   UTS   |   UAS   | AKHIR  |")
        print("|______|________________|__________________|____________|_________|_________|________|")
        i = 0
        for a in data_mahasiswa.items():
            i += 1
            print(f"| {i:4} | {a[0]:14s} | {a[1][0]:16} | {a[1][1]:10d} |  {a[1][2]:6d} | {a[1][2]:7d} | {a[1][4]:6.2f} | ")
    else:
        print("===================================| Daftar Nilai |===================================")
        print("______________________________________________________________________________________")
        print("|  No  |      Nama     |      NIM      |   TUGAS  |   UTS   |   UAS   | Nilai Akhir  |")
        print("______________________________________________________________________________________")
        print("|      |               |             Tidak Ada Data         |         |               ")
    print("______________________________________________________________________________________")
```
- Menghapus Data
```python
def hapus():
    print("Hapus Data Nilai Mahasiswa")
    nama = input(" Masukan Nama\t:")
    if nama in data_mahasiswa.keys():
        del data_mahasiswa[nama]
        print()
        print("=================================")
        print("===| BERHASIL MENGHAPUS DATA |===")
        print("=================================")
    else:
        print("Data {0} tidak ada".format(nama))
```
- Mengubah Data
```python
def ubah():
    print("===================================")
    print("===| Edit Data Nilai Mahasiswa |===")
    print("===================================")
    nama = input("Masukan Nama\t\t: ")
    print("___________________________________")
    if nama in data_mahasiswa.keys():
        nim = input("NIM baru\t\t: ")
        tugas = int(input("Nilai Tugas Baru\t: "))
        uts = int(input("Nilai UTS Baru\t\t: "))
        uas = int(input("Nilai UAS Baru\t\t: "))
        nilaiakhir = (tugas * 30 / 100 + uts * 35 / 100 + uas * 35 / 100)
        data_mahasiswa[nama] = nim, tugas, uts, uas, nilaiakhir
        print()
        print("================================")
        print("====| BERHASIL MENGUBAH DATA |====")
        print("================================")
    else:
        print("Data nilai {0} tidak ada ".format(nama))
```
- Membuat kondisi perulangan dan keterangan untuk pilihan menu
```python
while True:
    print("")
    print("|====================================|")
    print("|========| DATA MAHASISWA |==========|")
    print("|====================================|")
    x = input("1.| Lihat Data \n2.| Tambah Data \n3.| Ubah Data \n4.| Hapus Data \n0.| Keluar Aplikasi \nPilih menu : ")
    if x.lower() == "1":
        tampilkan()
    elif x.lower() == "2":
        tambah()
    elif x.lower() == "3":
        ubah()
    elif x.lower() == "4":
        hapus()
    elif x.lower() == "0":
        print()
        print("=================================")
        print("====== KELUAR DARI PROGRAM ======")
        print("=================================")
        break
```
```python
else:
        print()
        print("================================")
        print("== Pilihan Anda Tidak Tersedia ==")
        print("== Pilihlah Menu Yang Tersedia ==")
        print("================================")
```

# Flowchart
![gambar](Screenshot/Flowchart.png)
