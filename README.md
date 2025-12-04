Kelompok 4:
Tema Project: Sistem Absensi Karyawan
25-150 Rakina Pandini Rifda
25-106 Crysoli Tiara Simanjuntak

Program ini berisi sistem absensi karyawan menggunakan sistem CRUD (Create, Read, Update & Delete)
dan dalam kode tersebut terdapat 7 fitur, antara lain:
1. Tambah Karyawan
2. Tambah Absensi
3. Tampilkan Semua Data
4. Cari Karyawan
5. Update Absensi
6. Hapus Data Absensi
7. Keluar

Program tersebut dimulai dari menambahkan nama karyawan lalu setelah di enter akan dimasukkan data karyawan di bagian tambah absensi
setelah itu data akan ditampilkan jika pengguna mengetik no 3 atau tampilkan data. Jika sudah maka pengguna bisa mencari nama karyawan jika mengetik no 4 di bagian input_angka("Pilih menu (1-7): "). Setelahnya data yang dimasukkan bisa di update dan juga bisa dihapus. Program akan selesai apabila karyawan tersebut mengetik no 7.

Dalam program karyawan akan disuruh untuk memasukkan:

hari = input_huruf("Masukkan hari: ")
tanggal = input_angka("Masukkan tanggal: ")
bulan = input_angka("Masukkan bulan: ")
tahun = input_angka("Masukkan tahun: ")
masuk = input_huruf("Apakah karyawan masuk? (y/n): ")
keterangan = input_huruf("Masukkan keterangan (Masuk/izin/Sakit): ")

Dengan data yang telah dimasukkan, program akan mencetak format data dalam bentuk:
absensi[nama].append([f"{hari}-{tanggal}-{bulan}-{tahun}", keterangan, masuk, status, jam_asli])

Di dalam program ini juga memuat penyeleksian kondisi jika karyawan tersebut memasukkan jam, seperti:

 if total_menit < jam_masuk_normal:
            status = "Terlalu Awal"
        elif jam_masuk_normal <= total_menit < batas_tepat_waktu:
            status = "Tepat Waktu"
        else:
            status = "Terlambat"

Dari kode diatas ada 3 pilihan status yang akan dikeluarkan sesuai dengan jam yang dimasukkan oleh karyawan.

Dalam program ini dibuat jika karyawan mengetik sakit atau izin maka karyawan tidak disuruh untuk memasukkan jam kedatangan.
Terdapat pula dalam program ini, jika pengguna salah memasukkan data di bagian yang tidak seharusnya, misalnya masukkan jam dalam bentuk angka tapi pengguna malah memasukkan huruf, program akan menampilkan pesan peringatan kepada si karyawan tersebut untuk memasukkan data dengan benar sesuai ketentuannya.