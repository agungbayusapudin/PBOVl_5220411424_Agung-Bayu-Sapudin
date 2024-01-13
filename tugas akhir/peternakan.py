# kofigurasi database
import mysql.connector

con = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "5220411424"
)

cursor = con.cursor()

# ------- end konfigurasi database ---------

import datetime
from tabulate import tabulate

class perusahaan():
    def __init__(self,lokasi,nama_perusahaan):
        self.lokasi = lokasi
        self.nama_perusahaan = nama_perusahaan
        
# login akses pada system
    def login_akses(self,role):
        if role == "users":
            # input username dan password
            print("======= MASUKAN PASSWORD DAN USERNAME=======")
            username = input("Masukan Username.....")
            password = input("Masukan Password.....")
            # mengambil data dari tabel dari username dan password yang dicocokan dengan inputan
            cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s",(username,password))
            data = cursor.fetchall()
            con.commit()
            # cek data apakah ada
            if data != []:
                home()
            else :
                return "gagal"
                
                
            
        elif role == "admin":
            # input username dan password
            print("======= MASUKAN PASSWORD DAN USERNAME=======")
            username = input("Masukan Username.....")
            password = input("Masukan Password.....")
            # mengambil data dari tabel username dan password yang dicocokan dengan inputan
            cursor.execute("SELECT * FROM admin WHERE username = %s AND password = %s",(username,password))
            data = cursor.fetchall()
            con.commit()
            # cek data apakah ada
            if data != []:
                home()
            
            else :
                return "gagal"
                    
    def register(self,role):
        if role == "users":
            # input username ,password, and email
            print("======= MASUKAN PASSWORD DAN USERNAME DAN EMAIL=======")
            username = input("Masukan Username.....")
            email = input("Masukan email....")
            password = input("Masukan Password.....")
            # memasukan data dengan data yang sudah diinputkan
            cursor.execute("INSERT INTO users (username,email,password) values (%s,%s,%s)",(username,email,password))
            con.commit()
            # hasil dari inputan data yang sudah di eksekusi
            return "berhasil"
                
        elif role == "admin":
            # input username ,email,password
            print("======= MASUKAN PASSWORD DAN USERNAME DAN EMAIL=======")
            username = input("Masukan Username.....")
            email = input("Masukan email....")
            password = input("Masukan Password.....")
            
            cursor.execute("INSERT INTO admin (username,email,password) values (%s,%s,%s)",(username,email,password))
            con.commit()
            # hasil dari inputan data yang sudah dieksekusi
            return "berhasil"
    
    
class peternakan_hewan(perusahaan):
    def __init__(self,lokasi,nama_perusahaan,jenis,kandang):
        super().__init__(lokasi,nama_perusahaan)
        self.jenis = jenis
        self.kandang = kandang
    
    def pemberian_makan(self,jenis_hewan):
        jumlah = int(input("Masukan jumlah pakan ....")) # jumlah dalam kilo,1 kilo nambah 0.01 kwintal
        penambahan_berat = jumlah * 1
        # menambah berat sapi setelah pemberian makan
        if jenis_hewan == "sapi":
            # update setelah memberi makan
            berat = Sapi.berat + penambahan_berat
            cursor.execute(f"UPDATE sapi SET berat = {berat}")
            con.commit()
            print(f"Berhasil memberi pakan pada {datetime.datetime.now()}")
        elif jenis_hewan == "kambing":
            # update setelah memberi makan
            berat = Kambing.berat + penambahan_berat
            cursor.execute(f"UPDATE kambing SET berat = {berat}")
            con.commit()
            print(f"Berhasil memberi pakan pada {datetime.datetime.now()}")
        else:
            print("gagal memberikan pakan jenis hewan salah")
            
    def patau_kesehatan(self,jenis_hewan, role):
        if role == 'admin':
            print("====== PILIHAN MENU PANTAU KESEHATAN UNTUK ADMIN ======")
            print("| 1.menambah data cara penanganan")
            print("| 2.menampilkan data cara penanganan")
            print("| 3.menghapus data cara penanganan")
            
            pilihan_admin = int(input("Masukan pilihan anda....."))
            
            if pilihan_admin == 1:
                print("===== MENAMBAH DATA SILAHKAN INPUT DATA DENGAN BENAR =====")
                
                akibat = input("Masukan akibat yang ingin ada masukan ......")
                gejala_spesifik = input("Masukan gejala spesifiknya ......")
                penanganan = input("Masukan penanganan")
                
                cursor.execute(f"INSERT INTO info_kesehatan_{jenis_hewan} (akibat,gejala_spesifik,penanganan) values (%s,%s,%s)",(akibat,gejala_spesifik,penanganan))
                con.commit()
                return "berhasil"
            
            elif pilihan_admin == 2:
                
                cursor.execute(f"SELECT * FROM info_kesehatan_{jenis_hewan}")
                
                data_penyakit = cursor.fetchall()
                con.commit()
                # menampilkan seluruh data
                for one_data in data_penyakit:
                    print(one_data)
                    
            elif pilihan_admin == 3:
                print("====MASUKAN DATA YANG INGIN DI HAPUS KARNA RISKAN ====")
                keyword = input("Masukan data yang ingin anda hapus.....")
                
                cursor.execute(f"DELETE FROM info_kesehatan_{jenis_hewan} WHERE akibat = %s", (keyword,))
                con.commit()
                return "berhasil"
            
        elif role == "users":
            
            print("===== ANDA SEBAGAI USERS PILIHLAH MENU SESUAI YANG ANDA PILIH =====")
            print("| 1.Isi jawaban hasil survey hewan secara langsung")
            
            pilihan_user = int(input("Masukan Pilihan anda ....."))
            # data final dari hasil encarian
            data_hasil_final = []
            
            if pilihan_user == 1:
                data_hasil_gejala = []
                
                # kondisi gejala kurus
                berat_badan = input(f"Apakah {jenis_hewan} tersebut mengalami penurunan berat badan yang signifikan? ")
                # kondisi gejala penolakan majan
                perubahan_makan_minum = input(f"Apakah ada perubahan pada makan atau minum {jenis_hewan}?")
                #kondisi geala lambatnya proses makan,pengunyahan terganggu
                perubahan_prilaku_makan = input(f"Apakah ada perubahan dalam perilaku makan {jenis_hewan}?") 
                #kondisi sapi lemas
                konsisi_lemas = input(f"Apakah {jenis_hewan} tersebut tampak lemas atau tidak bersemangat?")
                # kondisi perubahan pada kulit
                perubahan_kondisi_kulit = input(f"Apakah ada perubahan pada kulit atau bulu {jenis_hewan}?")
                # kondisi perubahan warna bau dan konsistensi pada kotoran sapi
                perubahan_kotoran = input(f" Apakah terdapat perubahan pada warna, bau, atau konsistensi kotoran {jenis_hewan}?")
                # kondisi perubahan warna bau urin 
                perubahan_warna_bau_urin = input(f"Apakah terdapat perubahan pada warna atau bau urin {jenis_hewan}?")
                # kondisi perubahan padd hasil produksi susu
                perubahan_produksi_susu = input(f"Apakah ada perubahan pada hasil produksi susu (jika sapi adalah {jenis_hewan} perahan)?")
                
                for value in [berat_badan,perubahan_makan_minum,perubahan_prilaku_makan,konsisi_lemas,perubahan_kondisi_kulit,perubahan_kotoran,perubahan_warna_bau_urin,perubahan_produksi_susu]:
                    data_hasil_gejala.append(value)
    
                # mengambil nilai dictionary dengan menggunakan key dari dictionary dimana key tersebut sesuai isi dari pertanyaan sesuai index
                for index in range(0,len(data_hasil_gejala)):
                    if data_hasil_gejala[index] == "ya":
                        index_database = index + 1
                        cursor.execute(f"SELECT gejala_spesifik,penanganan  FROM info_kesehatan_{jenis_hewan} WHERE id_{jenis_hewan} = {index_database}")
                        data_hasil_final.append(cursor.fetchone())
                        con.commit()
                        print(data_hasil_final)
                    else:
                        pass
            
    def penempatan_kandang(self):
        if Susu_sapi.umur > 2: # 2 bulan usia sapi
            kandang_baru = 'kandang sapi dewasa'
            # update table 
            cursor.execute(f"UPDATE sapi SET kandang = %s",(kandang_baru,))
            con.commit()  
            
        else:
            kandang_baru = 'kandang sapi anakan'
            # update table 
            cursor.execute(f"UPDATE sapi SET kandang = %s",(kandang_baru,))
            con.commit()  
                        
class sapi(peternakan_hewan):
    def __init__(self,lokasi,nama_perusahaan,jenis,kandang,ras,umur,berat):
        super().__init__(lokasi,nama_perusahaan,jenis,kandang)
        self.ras = ras
        self.berat = berat
        self.umur = umur
        
    def menambahkan_data(self):
        cursor.execute("INSERT INTO sapi (jenis,kandang,ras,berat,umur) values (%s,%s,%s,%s,%s)",(self.jenis,self.kandang,self.ras,self.berat,self.umur))
        con.commit()
    
    def kesehatan(self,aksses):
        if aksses == 2:
            print(Susu_sapi.patau_kesehatan())

        else:
            print("belum melakukan pemantauan atau pengecekan terhadap hewan ternak")
            print("Perlu melakukan pengecekan terhadap hewan ternak")
        
                   
    
class sapi_susu(sapi):
    def __init__(self,lokasi,nama_perusahaan,jenis,kandang,ras,berat,umur,jumlah_produksi_susu):
        super().__init__(lokasi,nama_perusahaan,jenis,kandang,ras,berat,umur)
        self.__jumlah_produksi_susu = jumlah_produksi_susu
    
    def produksi_susu(self):
        return self.__jumlah_produksi_susu
            
            
class kambing(peternakan_hewan):
    def __init__(self,lokasi,nama_perusahaan,jenis,kandang,ras,umur,berat):
        super().__init__(lokasi,nama_perusahaan,jenis,kandang)
        self.ras = ras
        self.berat = berat
        self.umur = umur
        
    def menambahkan_data(self):
        cursor.execute("INSERT INTO kambing (jenis,kandang,ras,berat,umur) values (%s,%s,%s,%s,%s)",(self.jenis,self.kandang,self.ras,self.berat,self.umur))
        con.commit()
        
    def kesehatan(self,aksses):
        if aksses == 2:
            print(Daging_kambing.patau_kesehatan())

        else:
            print("belum melakukan pemantauan atau pengecekan terhadap hewan ternak")
            print("Perlu melakukan pengecekan terhadap hewan ternak")
        
class kambing_daging(kambing):
    def __init__(self,lokasi,nama_perusahaan,jenis,kandang,ras,berat,umur,jumlah_produksi_daging):
        super().__init__(lokasi,nama_perusahaan,jenis,kandang,ras,berat,umur)
        self.__jumlah_produksi_daging = jumlah_produksi_daging
        
    def produksi_daging(self):
        return self.__jumlah_produksi_daging
    
    
# Perusahaan = perusahaan("jl cikarang","PT Agung Bayu",0)
# tanah ke database
Peternakan_hewan = peternakan_hewan("CIkarang barat","PT agung bayu","sapi","Dewasa")
Sapi = sapi("CIkarang barat","PT agung bayu","sapi","Dewasa","Limousin",6,600) # waktu dalam bulan berat dalam kuwintal
Kambing = kambing("CIkarang barat","PT agung bayu","kambing","Dewasa","etawa",70,40) # waktu dalam bulan berat dalam kuwintal
Susu_sapi = sapi_susu("CIkarang barat","PT agung bayu","sapi","Dewasa","Limosin",6,6,10)
Daging_kambing = kambing_daging("CIkarang barat","PT agung bayu","kambing","Dewasa","etawa",70,7,30)
        
    
def home():
    # Sapi.menambahkan_data()
    # Kambing.menambahkan_data()
    print("====== Selamat Datang ======")
    print("|| 1. Peternakan")
    print("|| 2. Menampilkan data")
    # kondisi setelah memilih menu
    pilih_menu = int(input("Masukan.... "))
    if pilih_menu == 1:
        paternakan()
    elif pilih_menu == 2:
        menampilkan_data()
    
def paternakan():
    print("====== SELAMAT DATANG PADA MENU PETERNAKAN ======")
    print("|| 1. Pemberian makan")
    print("|| 2. Pantau kesehatan")
    print("|| 3. Penempatan kandang")
    print("|| 4. Sapi Dan Kambing")
    
    pilihan = int(input("Masukan.... "))
    if pilihan == 1:
        print("==== Pemberian makan =====")
        jenis_hewan = input("Masukan jenis hewan... ")
        Peternakan_hewan.pemberian_makan(jenis_hewan)
        
    elif pilihan == 2:
        print("==== Pantau Kesehatan =====")
        role = input("Masukan role anda ....")
        jenis_hewan = input("Masukan jenis hewan... ")
                
                
        Peternakan_hewan.patau_kesehatan(jenis_hewan,role)
        
    elif pilihan == 3:
        Peternakan_hewan.penempatan_kandang()
        
    elif pilihan == 4:
        print("====== Sapi dan kambing ====== ")
        print("|| 1. Kessehatan")
        print("|| 2. Tambilkan Jumlah produksi")
        masukan = int(input("masukan....."))
        if masukan == 1:
            kesehatan(pilihan)
        
        if masukan == 2:
            tampil_hasil_produksi()
            
def kesehatan(akses):
    print("===== Cek kesehatan hewan =====")
    jenis = input("Masukan jenis hewan... ")
    if jenis == "sapi":
        Sapi.kesehatan(akses)
        
    elif jenis == "kambing":
        Kambing.kesehatan(akses)

def tampil_hasil_produksi():
    print("===== Menampilkan hasil produksi =====")
    jenis = input("Masukan jenis ....")
    if jenis == "sapi":
        print(f"jumlah produksi susu adalah = {Susu_sapi.produksi_susu()} Kg")
        
    elif jenis == "kambing":
        print(f"jumlah produksi daging adalah = {Daging_kambing.produksi_daging()} Kg")
    
def menampilkan_data():
    print("====== MENAMPILKAN DATA ======")
    print("|| 1. Data sapi")
    print("|| 2. Data kambing")
    
    pilihan = int(input("Masukan.... "))
    if pilihan == 1:
        cursor.execute("SELECT * FROM sapi")
        # menampilkan data
        print(cursor.fetchall())
        con.commit()
        
    elif pilihan == 2:
        cursor.execute("SELECT * FROM kambing")
        # menampilkan data
        print(cursor.fetchall())
        con.commit()
        
def Produksi():
    print("|| 1. Susu sapi")
    print("|| 2. Daging kambing")
    pilih_produksi = int(input("Masukan.... "))
    
    if pilih_produksi == 1:
        Susu_sapi.produksi_susu()
    elif pilih_produksi == 2:
        Daging_kambing.produksi_daging() 

run = True
while run:
    print("======= SYSTEM MENAGEMENT PETERNAKAN KAMBING DAN SAPI =======")
    print("|| 1. LOGIN  ")
    print("|| 2. REGISTER  ")
    pilih_user = int(input("Masukan.... "))
    role = input("Masukan role anda....")
    
    if pilih_user == 1:
        Peternakan_hewan.login_akses(role)
        
    elif pilih_user == 2:
        Peternakan_hewan.register(role)
        
    else:
        print("Salah tidak dapatk melakukan login")
