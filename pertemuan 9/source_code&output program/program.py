from class_program import mobil, mobil_balap, kereta, mobil_crossroad, motor_balap, motor_crossroad,motor

# Program
def jenis_lokomotif(jenis_kendaraan):
    if jenis_kendaraan == 1:   #-------1 adalah kerreta
        # Menampilkan menu layanan kereta
        jenis_layanan = kereta.akses_jenis_layanan_kereta()
        fitur_kereta_api(jenis_layanan)
        
    elif jenis_kendaraan == 2:   #-------2 adalah mobil
        print(f"Selamat datang di dalam menu {jenis_kendaraan}")
        
        # Menampilkan menu mobil
        print("1. Pencarian mobil yang lebih spesifik")
        print("2. Fitur mobil bergerak")
        
        pilihan = input("Masukkan pilihan Anda (1/2): ")
        # pilihan jenis mobil
        if pilihan == "1":
            print("\n=================")
            print("1.Mobil balap")
            print("2.Mobil crossroad")
            print("=================")
            jenis_mobil = input(f"Masukkan jenis {jenis_kendaraan} yang Anda pilih:\n").lower()
            fitur_mobil_tiap_jenis(jenis_mobil)
        elif pilihan == "2":
            fitur_mobil_bergerak()
        else:
            print("Pilihan tidak valid.")
        
    elif jenis_kendaraan == 3:        #-----3 adalah motor
        print(f"Selamat datang di dalam menu {jenis_kendaraan}")
        
        # Menampilkan menu motor
        print("1. Pencarian motor yang lebih spesifik")
        print("2. Fitur motor bergerak")
        
        pilihan = input("Masukkan pilihan Anda (1/2): ")
        # pilihan jenis motor
        if pilihan == "1":
            print("=================")
            print("1.Motor balap")
            print("2.Motor crossroad")
            print("=================")
            jenis_motor = input(f"Masukkan jenis {jenis_kendaraan} yang Anda pilih:\n").lower()
            fitur_motor(jenis_motor)
        elif pilihan == "2":
            fitur_motor_bergerak()
        else:
            print("Pilihan tidak valid.")

def fitur_kereta_api(jenis_layanan):
    # Menambah rute perjalanan
    print(f"Selamat datang dalam jenis layanan kereta api kelas {jenis_layanan}")
    
    # Menampilkan menu rute yang tersedia
    print("\n=================")
    print("1. Tambah rute")
    print("2. Kurangi rute")
    print("3. Menampilkan data")
    print("=================")
    
    pilih_rute = input("Pilih program:\n")
    
    # Kondisi pengecekan fitur yang digunakan
    if pilih_rute == "1":
        tambah_rute = input("Masukkan rute yang ingin ditambahkan: ")
        kereta.tambah_rute(tambah_rute)
    elif pilih_rute == "2":
        kurangi_rute = input("Masukkan rute yang ingin dikurangi: ")
        kereta.kurangi_rute(kurangi_rute)
    elif pilih_rute == "3":
        kereta.menampilkan_data()
    else:
        print("Pilihan tidak valid.")

# Definisi fitur mobil tanpa memilih jenisnya
def fitur_mobil_bergerak():
    # Bergerak ke kanan, kiri, maju, mundur, start engine
    print("Selamat datang di dalam menu TRANSPORTASI MOBIL")
    # Menampilkan daftar aktivitas yang dapat dilakukan mobil
    mobil.start_engine()

# fitur mobil tiap jenisnya
def fitur_mobil_tiap_jenis(jenis_mobil):
    if jenis_mobil == "mobil balap":
        # Fitur mobil balap
        mobil_balap.race()        
    elif jenis_mobil == "mobil crossroad":
        # Fitur mobil crossroad
        print("\n=================")
        print("1. Race")
        print("2. Buka sunroof")
        print("3. Tutup sunroof")
        print("=================")
        pilihan = input("Masukkan pilihan Anda: ")
        if pilihan == "1":
            mobil_crossroad.race()
        elif pilihan == "2":
            mobil_crossroad.sunroft_terbuka()
        elif pilihan == "3":
            mobil_crossroad.sunroft_tertutup()
        else:
            print("Pilihan tidak valid.")

# fitur motor bergerak tanpa memilih jenisnya
def fitur_motor_bergerak():
    # Bergerak ke kanan, kiri, maju, mundur, start engine
    print("Selamat datang di dalam menu TRANSPORTASI MOTOR\n")
    # Menampilkan daftar aktivitas yang dapat dilakukan motor
    motor.start_engine()
    
# fitur motor tiap jenisnya
def fitur_motor(jenis_motor):
    if jenis_motor == "motor balap":
        # Fitur motor balap
        motor_balap.race()        
    elif jenis_motor == "motor crossroad":
        # Fitur motor crossroad
        motor_crossroad.race()

def program():
    print("===== SELAMAT DATANG DI PROGRAM PENGATURAN SISTEM KENDARRAN DARAT =====")
    print("======= Melayani berbagai macam pengecekan kendaraan darat =======\n")
    # Menampilkan menu jenis kendaraan
    print("=================")
    print("1. Kereta api")
    print("2. Mobil")
    print("3. Motor")
    print("=================")
    
    jenis_kendaraan = int(input("Masukkan jenis kendaraan Anda yang ingin Anda gunakan (1/2/3): "))
    if jenis_kendaraan <= 3:
        jenis_lokomotif(jenis_kendaraan)
    else:
        print("yang anda masukan salah")

# Menjalankan program
while True:
    program()
# ====jalannya program=====
# Menampilkan menu program
# Pengguna memilih jenis kendaraan
# Program memilih jenis kendaraan dari turunan kendaraan yang dipilih
# Pengguna menggunakan program yang tersedia di dalam tiap sifat kendaraan
# Menampilkan hasil output dari program yang dipilih kendaraan