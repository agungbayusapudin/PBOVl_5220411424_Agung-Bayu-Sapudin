# import module
from turtle import Screen, Turtle
from tabulate import tabulate
from ffpyplayer.player import MediaPlayer
import time
import cv2

# class induk
class kendaraam_darat:
    def __init__(self, tahun_keluaran, nama, warna, kecepatan, bahan_bakar, jumlah_roda, kapasitas_penumpang):
        self.tahun_keluaran = tahun_keluaran
        self.nama = nama
        self.warna = warna
        self.kecepatan = kecepatan
        self.bahan_bakar = bahan_bakar
        self.jumlah_roda = jumlah_roda
        self.kapasitas_penumpang = kapasitas_penumpang

# classs turunan kendaraan darat = kereta api
class kreta_api(kendaraam_darat):
    def __init__(self, tahun_keluaran, nama, warna, kecepatan, bahan_bakar, jumlah_roda, kapasitas_penumpang,jenis_gerbong,jumlah_kursi, jenis_layanan_kereta,rute):
        super().__init__(tahun_keluaran, nama, warna, kecepatan, bahan_bakar, jumlah_roda, kapasitas_penumpang)
        self.jenis_gerbong = jenis_gerbong
        self.jumlah_kursi = jumlah_kursi
        self.__jenis_layanan_kereta = jenis_layanan_kereta
        self.rute = rute

    def akses_jenis_layanan_kereta(self):
        return self.__jenis_layanan_kereta
    
    def tambah_rute(self,rute):
        print("Menu penambahan rute")
        # penambahan rute
        self.rute.append(rute)        
        print("Berhasil menambahkan rute")
        
    def kurangi_rute(self,rute):
        print("Menu kurangi rute")
        # perulangan mengecek value in self.rute
        for value_in_rote in self.rute:
            if rute == value_in_rote:
                self.rute.remove(rute)
                print("Berhasil menghapus rute")
            else:
                # ketika rute tidak ada dalam self.rute
                pass
    
    def menampilkan_data(self):
        data = {
            "nama" :[ self.nama],
            "kapasitas" : [self.kapasitas_penumpang],
            "rute perjalanan" : [self.rute],
            "jenis layanan" : [kreta_api.akses_jenis_layanan_kereta(self)]
        }
        print(tabulate(data, headers="keys",tablefmt="fancy-grid"))

# class tutunan dari kendaraan darat = mobil
class Mobil(kendaraam_darat):
    def __init__(self, tahun_keluaran, nama, warna, kecepatan, bahan_bakar, jumlah_roda, kapasitas_penumpang,jenis_mobil):
        super().__init__(tahun_keluaran, nama, warna, kecepatan, bahan_bakar, jumlah_roda, kapasitas_penumpang)
        self.jenis_mobil = jenis_mobil

    def start_engine(self):
        print("Start engine untuk dapat bergerak")
        start = input("Apakah yakin akan start : ")
        if start == "ya":
            mobil.bergerak()

    def bergerak(self):
        # nested function untuk mempermudah akses dalam fungsinya
        def bergerak_ke_kanan():
            turtle.setheading(0)
            turtle.fd(50)

        def bergerak_ke_kiri():
            turtle.setheading(180)
            turtle.fd(50)

        def bergerak_maju():
            turtle.setheading(90)
            turtle.fd(50)

        def bergerak_mundur():
            turtle.setheading(270)
            turtle.fd(50)
            
        def catat_waktu():
            waktu = round(time.time() - start, 2)
            print(waktu, "s")
        
        def stop_time():
            print("apakah anda ingin stop engine")
            stop_engine = input("apakah anda akan stop engine : ")
            if stop_engine == "ya":
                print("Berhasil stop engine")
                exit()
            
        # membuat layar
        screen = Screen()
        screen.setup(600, 600)
        turtle = Turtle('circle')
        turtle.speed('slow')
        # bergerak sesuai arah pada keyboard
        screen.onkey(bergerak_ke_kanan, 'Right')
        screen.onkey(bergerak_ke_kiri, 'Left')
        screen.onkey(bergerak_maju, 'Up')
        screen.onkey(bergerak_mundur, 'Down')
        screen.onkeypress(catat_waktu, 'space')
        screen.onkeypress(stop_time, 'c')
        
        screen.listen()
        # waktu mulai
        start = time.time()
        # program berulang
        screen.mainloop() 

# class tutunan dari mobil = mobil balap
class Mobil_balap(Mobil):
    def __init__(self, tahun_keluaran, nama, warna, kecepatan, bahan_bakar, jumlah_roda, kapasitas_penumpang, jenis_mobil, front_wing, rear_wing):
        super().__init__(tahun_keluaran, nama, warna, kecepatan, bahan_bakar, jumlah_roda, kapasitas_penumpang, jenis_mobil)
        self.front_wing = front_wing
        self.rear_wing = rear_wing

    def race(self):
        # akan menampilkan video dengan memanggil function menampilkan_video()
        file = "source_code&output program/mobil_balap.mp4"
        menampilkan_video(file)
        
        print("ada sedang berada pada mobil balap : ")
        print("sekarang mobil balap memiliki spesifikasi sebagai berikut: ")
        print(f"nama mobil : {self.nama}")
        print(f"front_wing : {self.front_wing}")
        print(f"rear wing : {self.rear_wing}")
        if self.front_wing == "ada":
            self.kecepatan += 50
            print("Menambah kecepatan 50 km\jam")
        elif self.rear_wing == "ada":
            self.kecepatan += 50
            print("Menambah kecepatan 50 km\jam")
        else:
            pass
        print(f"kecepatan : {self.kecepatan}")
        
# class turunan dari mobil = mobil crossroad
class Mobil_crossroad(Mobil):
    def __init__(self, tahun_keluaran, nama, warna, kecepatan, bahan_bakar, jumlah_roda, kapasitas_penumpang, jenis_mobil,sunroft_type, shock_bracker):
        super().__init__(tahun_keluaran, nama, warna, kecepatan, bahan_bakar, jumlah_roda, kapasitas_penumpang, jenis_mobil)
        self.sunroft_type = sunroft_type
        self.shock_bracker = shock_bracker
        self.keadaan_sunrroof = None

    def race(self):
        if self.keadaan_sunrroof == None:
            print("ada sedang berada pada mobil balap : ")
            print("sekarang mobil balap memiliki spesifikasi sebagai berikut: ")
            print(f"nama mobil : {self.nama}")
            print(f"kecepatan : {self.kecepatan}")
            print("siap dilintasan")
        else:
            print("kondisi sunroof masih terbuka")

    def sunroft_terbuka(self):
        # masukan jenis sunroft
        print("tipe sunroft")
        # menampilkan menu
        daftar_sunroft_dapat_dibuka = ["panaromic roof", "panaromic sunroof","panaromic monoroof", "sunroot", "monoroof"]
        # mengecek sunroft yang dapat dibuka
        if self.sunroft_type in daftar_sunroft_dapat_dibuka:
            print("sunroft bisa dibuka ")
            self.keadaan_sunrroof = "buka"
        else:
            print("sunroft tidak dapat dibuka karena memiliki jenis yang berbeda")

    def sunroft_tertutup(self):
        # masukan jenis sunroft
        print("tipe sunroft")
        # menampilkan menu
        daftar_sunroft_dapat_dibuka = ["panaromic roof", "panaromic sunroof","panaromic monoroof", "sunroot", "monoroof"]
        # mengecek sunroft yang dapat ditutup
        if self.sunroft_type in daftar_sunroft_dapat_dibuka:
            print("sunroft bisa ditutup")
            self.keadaan_sunrroof = None    
        else:
            print("sunroft tidak dapat dibuka karena memiliki jenis yang berbeda")

class Motor(kendaraam_darat):
    def __init__(self, tahun_keluaran, nama, warna, kecepatan, bahan_bakar, jumlah_roda, kapasitas_penumpang, jenis_motor):
        super().__init__(tahun_keluaran, nama, warna, kecepatan, bahan_bakar, jumlah_roda, kapasitas_penumpang)
        self.jenis_motor = jenis_motor
        
    def start_engine(self):
        print("Start engine untuk dapat bergerak")
        start = input("Apakah yakin akan start : ")
        if start == "ya":
            mobil.bergerak()
            
    def bergerak(self):
        # nested function untuk mempermudah akses dalam fungsinya
        def bergerak_ke_kanan():
            turtle.setheading(0)
            turtle.fd(50)

        def bergerak_ke_kiri():
            turtle.setheading(180)
            turtle.fd(50)

        def bergerak_maju():
            turtle.setheading(90)
            turtle.fd(50)

        def bergerak_mundur():
            turtle.setheading(270)
            turtle.fd(50)
            
        def catat_waktu():
            waktu = round(time.time() - start, 2)
            print(waktu, "s")
        
        def stop_time():
            print("apakah anda ingin stop engine")
            stop_engine = input("apakah anda akan stop engine : ")
            if stop_engine == "ya":
                print("Berhasil stop engine")
                exit()
            
        # membuat layar
        screen = Screen()
        screen.setup(600, 600)
        turtle = Turtle('circle')
        turtle.speed('slow')
        # bergerak sesuai arah pada keyboard
        screen.onkey(bergerak_ke_kanan, 'Right')
        screen.onkey(bergerak_ke_kiri, 'Left')
        screen.onkey(bergerak_maju, 'Up')
        screen.onkey(bergerak_mundur, 'Down')
        screen.onkeypress(catat_waktu, 'space')
        screen.onkeypress(stop_time, 'c')
        
        screen.listen()
        # waktu mulai
        start = time.time()
        # program berulang
        screen.mainloop()

class Motor_balap(Motor):
    def __init__(self, tahun_keluaran, nama, warna, kecepatan, bahan_bakar, jumlah_roda, kapasitas_penumpang, jenis_motor, jenis_ban):
        super().__init__(tahun_keluaran, nama, warna, kecepatan, bahan_bakar, jumlah_roda, kapasitas_penumpang, jenis_motor)
        self.jenis_ban = jenis_ban

    def race(self):
        standar_kecepatan_motor_balap = 200
        if self.kecepatan >= standar_kecepatan_motor_balap:
            # menampilkan video
            file = 'source_code&output program/motor_balap.mp4'
            menampilkan_video(file)
            
            print("ada sedang berada pada motor balap : ")
            print("sekarang motor balap memiliki spesifikasi sebagai berikut: ")
            print(f"nama motor : {self.nama}")
            print(f"kecepatan : {self.kecepatan}")
            print("siap dilintasan")
        else:
            print("Tidak mempenuhi spesifikasi")

class Motor_crossroad(Motor):
    def __init__(self, tahun_keluaran, nama, warna, kecepatan, bahan_bakar, jumlah_roda, kapasitas_penumpang, jenis_motor,jenis_lintasan):
        super().__init__(tahun_keluaran, nama, warna, kecepatan, bahan_bakar, jumlah_roda, kapasitas_penumpang, jenis_motor)
        self.jenis_lintasan = jenis_lintasan

    def race(self):
        standar_kecepatan_motor_balap = 200
        jenis_lintasan_balap = ["berlumpur","berbatu","berair"]
        if self.kecepatan >= standar_kecepatan_motor_balap and self.jenis_lintasan in jenis_lintasan_balap:
            file="source_code&output program/motorcross.mp4"
            menampilkan_video(file) 
            
            print("ada sedang berada pada motor balap crosroad : ")
            print("sekarang motor balap memiliki spesifikasi sebagai berikut: ")
            print(f"nama motor : {self.nama}")
            print(f"kecepatan : {self.kecepatan}")
            print("siap dilintasan")
                
# object
kereta = kreta_api("2022", "kai", "biru", 200, "batu bara", "10", "200 orang","angkutan manusia","400", "ekonomi",["pekalongan","jawabarat"])
mobil = Mobil( "2013", "brio", "biru", 200, "solar", "4", "2","pribadi")
mobil_balap = Mobil_balap("2011", "suprak", "biru", 200, "pertamax turbo", 2, "2 orang", "balap", "ada", "tidak ada")
mobil_crossroad = Mobil_crossroad("2016", "jimny", "kuning", 200, "solar", 4, "4 orang", "crossroad", "panaromic sunroof", "double action")
motor = Motor("2022", "beat", "hitam", 100, "pertamax", 2, "2 orang", "transportasi")
motor_balap = Motor_balap("2023", "R1M", "biru", 1000, "pertamax turbo", 2, "1 orang", "balap","roadrace")
motor_crossroad = Motor_crossroad("2015", "CRF250L", "merah", 250, "pertamax", 1, "2 orang", "crossroad", "berlumpur")

# FUNCTION YANG DIGUNAKAN UNTUK MENAMPILKAN VIDEO
def menampilkan_video(file):
    video=cv2.VideoCapture(file)
    player = MediaPlayer(file)
    while True:
        ret, frame=video.read()
        audio_frame, val = player.get_frame()
        if not ret:
            print("selesai")
            break
        if cv2.waitKey(1) == ord("c"):
            break
        cv2.imshow("Video", frame)
        if val != 'eof' and audio_frame is not None:
            #audio
            img, t = audio_frame
    video.release()
    cv2.destroyAllWindows()