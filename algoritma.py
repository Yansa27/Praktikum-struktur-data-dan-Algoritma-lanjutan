# Buatlah program dalam bahasa pascal/C Plus/Python pilih salah satu untuk menghitung 10 data nilai mahasiswa dengan menggunakan tipe data array.
# 10 Data yang di input : nama, nilai quis, nilai mid dan nilai semester.
# data yang di proses total nilai dan nilai rata.
# tampilkan 10 data diatas dalam bentuk tabel laporan nilai mahasiswa
# Sreenshot listing program dan tampilan program di word dan kirim ke elearning.
# informasi lebih lanjut akan disampaikan pada pertemuan ke dua

#! Nama : JULIANSA
#! Nim  : 231420073
#! Kelas : IF2C

nilai_mahasiswa = []

for i in range(10):
    nomor = i + 1
    print("Mahasiswa nomor ", nomor)
    nama = input("Masukkan nama mahasiswa: ")
    nilai_quis = float(input("Masukkan nilai quis: "))
    nilai_mid = float(input("Masukkan nilai mid: "))
    nilai_semester = float(input("Masukkan nilai semester: "))
    print(f"Berhasil menambahkan data nilai mahasiswa {nama}")
    print("")
    nilai_mahasiswa.append([nomor, nama, nilai_quis, nilai_mid, nilai_semester])

for data in nilai_mahasiswa:
    total_nilai = data[2] + data[3] + data[4]
    nilai_rata = total_nilai / 3
    data.extend([total_nilai, nilai_rata])

header = ["Nomor","Nama", "Nilai Quis", "Nilai Mid", "Nilai Semester", "Total Nilai", "Nilai Rata"]

print("{:<9} {:<15} {:<11} {:<9} {:<15} {:<11} {:<11}".format(*header))
for data in nilai_mahasiswa:
    print("{:<9} {:<15} {:<11} {:<9} {:<15} {:<11} {:<11}".format(*data))
