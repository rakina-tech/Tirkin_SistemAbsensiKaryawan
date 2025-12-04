# Sistem Absensi Karyawan
absensi = {}

def input_angka(pesan):
    while True:
        try:
            return int(input(pesan))
        except ValueError:
            print("Tolong masukkan angka!")

def input_huruf(pesan):
    while True:
        data = input(pesan)
        if data == "":
            print("Tolong masukkan huruf!")
            continue
        try:
            int(data)
            print("Tolong masukkan huruf!")
        except ValueError:
            return data

def hanya_angka(teks):
    for c in teks:
        if c < "0" or c > "9":
            return False
    return True

def input_jam(pesan):
    while True:
        jam = input(pesan)

        # menggunakan format dengan satu titik
        titik = 0
        for c in jam:
            if c == ".":
                titik += 1

        if titik != 1:
            print("Tolong masukkan angka dengan format 00.00–23.59!")
            continue

        # untuk memisahkan jam dan menit
        jam_part = ""
        menit_part = ""
        sebelum_titik = True

        for c in jam:
            if c == ".":
                sebelum_titik = False
            else:
                if sebelum_titik:
                    jam_part += c
                else:
                    menit_part += c

        if jam_part == "" or menit_part == "":
            print("Tolong masukkan angka dengan format 00.00–23.59!")
            continue

        if not (hanya_angka(jam_part) and hanya_angka(menit_part)):
            print("Tolong masukkan angka dengan format 00.00–23.59!")
            continue

        j = int(jam_part)
        m = int(menit_part)

        if 0 <= j <= 23 and 0 <= m <= 59:
            return j * 60 + m, jam

        print("Tolong masukkan angka dengan format 00.00–23.59!")

def menu():
    while True:
        print("\n===== SISTEM ABSENSI KARYAWAN =====")
        print("1. Tambah Karyawan")
        print("2. Tambah Absensi")
        print("3. Tampilkan Semua Data")
        print("4. Cari Karyawan")
        print("5. Update Absensi")
        print("6. Hapus Data Absensi")
        print("7. Keluar")

        pilihan = input_angka("Pilih menu (1-7): ")

        if pilihan == 1:
            tambah_karyawan()
        elif pilihan == 2:
            tambah_absensi()
        elif pilihan == 3:
            tampilkan_semua()
        elif pilihan == 4:
            cari_karyawan()
        elif pilihan == 5:
            update_absensi()
        elif pilihan == 6:
            hapus_data()
        elif pilihan == 7:
            print("Program selesai. Terima kasih.")
            break
        else:
            print("Pilihan tidak tersedia!")

def tambah_karyawan():
    nama = input_huruf("Masukkan nama karyawan baru: ")
    if nama in absensi:
        print("Nama sudah ada dalam sistem!")
    else:
        absensi[nama] = []
        print("Karyawan berhasil ditambahkan.")

def tambah_absensi():
    nama = input_huruf("Masukkan nama karyawan: ")
    if nama not in absensi:
        print("Nama tidak ditemukan!")
        return

    hari = input_huruf("Masukkan hari: ")
    tanggal = input_angka("Masukkan tanggal: ")
    bulan = input_angka("Masukkan bulan: ")
    tahun = input_angka("Masukkan tahun: ")
    masuk = input_huruf("Apakah karyawan masuk? (y/n): ")
    keterangan = input_huruf("Masukkan keterangan (Masuk/izin/Sakit): ")

    # Keterangan
    if keterangan.lower() == "izin" or keterangan.lower() == "sakit":
        status = keterangan
        jam_asli = None
    else:
        total_menit, jam_asli = input_jam("Masukkan jam kedatangan (00.00–23.59): ")

        jam_masuk_normal = 7 * 60
        batas_tepat_waktu = 8 * 60

        if total_menit < jam_masuk_normal:
            status = "Terlalu Awal"
        elif jam_masuk_normal <= total_menit < batas_tepat_waktu:
            status = "Tepat Waktu"
        else:
            status = "Terlambat"

    absensi[nama].append([f"{hari}-{tanggal}-{bulan}-{tahun}", keterangan, masuk, status, jam_asli])
    print("Data absensi berhasil ditambahkan.")

def tampilkan_semua():
    if not absensi:
        print("Belum ada data.")
        return

    for nama, data in absensi.items():
        print(f"\nNama: {nama}")
        if not data:
            print("Belum ada data absensi.")
        else:
            for hadir in data:
                jam_tampil = hadir[4] if hadir[4] is not None else "-"
                print(f"Tanggal: {hadir[0]} | Ket: {hadir[1]} | Masuk: {hadir[2]} | Status: {hadir[3]} | Jam: {jam_tampil}")

def cari_karyawan():
    nama = input_huruf("Masukkan nama yang ingin dicari: ")
    if nama not in absensi:
        print("Nama tidak ditemukan!")
        return

    print(f"Data absensi {nama}:")
    for hadir in absensi[nama]:
        jam_tampil = hadir[4] if hadir[4] is not None else "-"
        print(f"Tanggal: {hadir[0]} | Ket: {hadir[1]} | Masuk: {hadir[2]} | Status: {hadir[3]} | Jam: {jam_tampil}")

def update_absensi():
    nama = input_huruf("Masukkan nama karyawan: ")
    if nama not in absensi:
        print("Nama tidak ditemukan!")
        return

    tanggal_dicari = input_huruf("Masukkan hari-tanggal-bulan-tahun absensi yang dicari: ")

    for hadir in absensi[nama]:
        if hadir[0] == tanggal_dicari:
            keterangan_baru = input_huruf("Masukkan keterangan baru: ")

            # Jika izin atau sakit
            if keterangan_baru.lower() == "izin" or keterangan_baru.lower() == "sakit":
                hadir[1] = keterangan_baru
                hadir[3] = keterangan_baru
                hadir[4] = None

            else:
                total_menit, jam_asli = input_jam("Masukkan jam kedatangan baru: ")

                jam_masuk_normal = 7 * 60
                batas_tepat_waktu = 8 * 60

                if total_menit < jam_masuk_normal:
                    status = "Terlalu Awal"
                elif jam_masuk_normal <= total_menit < batas_tepat_waktu:
                    status = "Tepat Waktu"
                else:
                    status = "Terlambat"

                hadir[1] = keterangan_baru
                hadir[3] = status
                hadir[4] = jam_asli

            print("Data berhasil diperbarui.")
            return

    print("Tanggal tidak ditemukan!")

def hapus_data():
    nama = input_huruf("Masukkan nama karyawan: ")

    if nama not in absensi:
        print("Nama tidak ditemukan!")
        return

    tanggal_dicari = input_huruf("Masukkan hari-tanggal-bulan-tahun yang akan dihapus: ")

    for hadir in absensi[nama]:
        if hadir[0] == tanggal_dicari:
            absensi[nama].remove(hadir)
            print("Data berhasil dihapus.")
            return

    print("Tanggal tidak ditemukan.")

menu()