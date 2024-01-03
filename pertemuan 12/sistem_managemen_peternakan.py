
import datetime
from tabulate import tabulate

class perusahaan():
    def __init__(self,lokasi,nama_perusahaan):
        self.lokasi = lokasi
        self.nama_perusahaan = nama_perusahaan
    # def akses_privat(self):
    #     return self.__
    
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
            Susu_sapi.berat += penambahan_berat
            print(f"Berhasil memberi pakan pada {datetime.datetime.now()}")
        elif jenis_hewan == "kambing":
            Daging_kambing.berat += penambahan_berat
            print(f"Berhasil memberi pakan pada {datetime.datetime.now()}")
        else:
            print("gagal memberikan pakan jenis hewan salah")
            
    def patau_kesehatan(self,jenis):
        if jenis == 'sapi':
            data_gejala_solusi = {
                "berat" : [["Sapi kurus kurang lapisan lemak"],["Identifikasi penyebabnya, seperti parasit, masalah pencernaan, atau penyakit.","Sesuaikan pakan dan nutrisi dengan bantuan seorang ahli nutrisi ternak.","Berikan perawatan medis yang sesuai, jika diperlukan."]],
                "perubahan_makan": [["masalah perubahan makan"],[    "Berikan akses ke air bersih.","Sesuaikan pakan dan konsistensi diet.","Konsultasikan dengan seorang dokter hewan untuk diagnosis lebih lanjut dan perawatan."]],
                "perubahan_perilaku_makan": [["perilaku sapi berubah"],[    "Pisahkan sapi yang sakit untuk mencegah penyebaran infeksi.","Berikan perawatan antibiotik sesuai petunjuk dokter hewan.","Pastikan ventilasi yang baik di kandang sapi."]],
                "kondisi_lemas": [["sapi kondisi lemas"],[    "Lakukan pemeriksaan kesehatan menyeluruh untuk mengidentifikasi penyebabnya.","Berikan nutrisi yang baik, pastikan pakan dan air cukup.","Jika perlu, berikan vitamin atau suplemen energi."]],
                "perubahan_kondisi_kulit": [["masalah kondisi kulit"],[    "Identifikasi penyebab penyakit kulit (misalnya, parasit, infeksi jamur).","Berikan perawatan antiparasit atau antijamur sesuai petunjuk dokter hewan.","Pemantauan kebersihan kandang dan lingkungan."]],
                "perubahan_kotoran": [["masalah dalam kotoran"],["Isolasi sapi yang sakit, periksa dan obati penyebab diare, dan berikan nutrisi yang tepat."]],
                "perubahan_urin": [["masalah dalam perubahan urin"],["Segera konsultasikan dengan dokter hewan untuk diagnosis dan perawatan yang sesuai."]],
                "perubahan_produksi_susu": [["perngurangan jumlah dan kualitas produksi susu"],["Periksa dan atasi masalah di pemerahan susu, perbaiki masalah gizi, dan periksa kesehatan sapi secara menyeluruh.","Identifikasi penyebab penurunan produksi, seperti penyakit atau masalah manajemen, dan berikan perawatan yang sesuai."]]
            }
            # data gejala berisi key dictionary
            data_gejala = []
            for value_gejala in data_gejala_solusi.keys():
                data_gejala.append(value_gejala)
                
            data_hasil_gejala = []
            # kondisi gejala kurus
            berat_badan = input(f"Apakah sapi tersebut mengalami penurunan berat badan yang signifikan? ")
            # kondisi gejala penolakan majan
            perubahan_makan_minum = input(f"Apakah ada perubahan pada makan atau minum sapi?")
            #kondisi geala lambatnya proses makan,pengunyahan terganggu
            perubahan_prilaku_makan = input(f"Apakah ada perubahan dalam perilaku makan sapi?") 
            #kondisi sapi lemas
            konsisi_lemas = input(f"Apakah sapi tersebut tampak lemas atau tidak bersemangat?")
            # kondisi perubahan pada kulit
            perubahan_kondisi_kulit = input(f"Apakah ada perubahan pada kulit atau bulu sapi?")
            # kondisi perubahan warna bau dan konsistensi pada kotoran sapi
            perubahan_kotoran = input(f" Apakah terdapat perubahan pada warna, bau, atau konsistensi kotoran sapi?")
            # kondisi perubahan warna bau urin 
            perubahan_warna_bau_urin = input(f"Apakah terdapat perubahan pada warna atau bau urin sapi?")
            # kondisi perubahan padd hasil produksi susu
            perubahan_produksi_susu = input(f"Apakah ada perubahan pada hasil produksi susu (jika sapi adalah sapi perahan)?")
            for value in [berat_badan,perubahan_makan_minum,perubahan_prilaku_makan,konsisi_lemas,perubahan_kondisi_kulit,perubahan_kotoran,perubahan_warna_bau_urin,perubahan_produksi_susu]:
                data_hasil_gejala.append(value)
            # datafinal
            data_final = []
            
            for value in range(0,len(data_gejala)):
                if data_hasil_gejala[value] == "ya":
                    data_final.append(data_gejala_solusi[data_gejala[value]])
                
                else:
                    pass
            if len(data_final) != 0:
                # menampilkan data
                print(tabulate(data_final,headers=["Gejala","penanganan"],tablefmt="grid"))
            else:
                print("Sapi dalam kondisi prima tidak ada gejala")
            
            return data_final
            
        elif jenis == 'kambing':
            data_gejala_solusi = {
                "berat" : [["kambing kurus kurang lapisan lemak"],["Identifikasi penyebabnya, seperti parasit, masalah pencernaan, atau penyakit.","Sesuaikan pakan dan nutrisi dengan bantuan seorang ahli nutrisi ternak.","Berikan perawatan medis yang sesuai, jika diperlukan."]],
                "perubahan_makan": [["masalah perubahan makan"],[    "Berikan akses ke air bersih.","Sesuaikan pakan dan konsistensi diet.","Konsultasikan dengan seorang dokter hewan untuk diagnosis lebih lanjut dan perawatan."]],
                "perubahan_perilaku_makan": [["perilaku kambing berubah"],[    "Pisahkan kambing yang sakit untuk mencegah penyebaran infeksi.","Berikan perawatan antibiotik sesuai petunjuk dokter hewan.","Pastikan ventilasi yang baik di kandang kambing."]],
                "kondisi_lemas": [["kambing kondisi lemas"],[    "Lakukan pemeriksaan kesehatan menyeluruh untuk mengidentifikasi penyebabnya.","Berikan nutrisi yang baik, pastikan pakan dan air cukup.","Jika perlu, berikan vitamin atau suplemen energi."]],
                "perubahan_kondisi_kulit": [["masalah kondisi kulit"],[    "Identifikasi penyebab penyakit kulit (misalnya, parasit, infeksi jamur).","Berikan perawatan antiparasit atau antijamur sesuai petunjuk dokter hewan.","Pemantauan kebersihan kandang dan lingkungan."]],
                "perubahan_kotoran": [["masalah dalam kotoran"],["Isolasi kambing yang sakit, periksa dan obati penyebab diare, dan berikan nutrisi yang tepat."]],
                "perubahan_urin": [["masalah dalam perubahan urin"],["Segera konsultasikan dengan dokter hewan untuk diagnosis dan perawatan yang sesuai."]],
                "perubahan_produksi_daging": [["perngurangan jumlah dan kualitas produksi daging"],["Periksa dan atasi masalah di kualitas daging, perbaiki masalah gizi, dan periksa kesehatan kambing secara menyeluruh.","Identifikasi penyebab penurunan produksi, seperti penyakit atau masalah manajemen, dan berikan perawatan yang sesuai."]]
            }
            # data gejala berisi key dictionary
            data_gejala = []
            for value_gejala in data_gejala_solusi.keys():
                data_gejala.append(value_gejala)
            # hasil dari gejala
            data_hasil_gejala = []
            # kondisi gejala kurus
            berat_badan = input(f"Apakah kambing tersebut mengalami penurunan berat badan yang signifikan? ")
            # kondisi gejala penolakan majan
            perubahan_makan_minum = input(f"Apakah ada perubahan pada makan atau minum kambing?")
            #kondisi geala lambatnya proses makan,pengunyahan terganggu
            perubahan_prilaku_makan = input(f"Apakah ada perubahan dalam perilaku makan kambing?") 
            #kondisi kambing lemas
            konsisi_lemas = input(f"Apakah kambing tersebut tampak lemas atau tidak bersemangat?")
            # kondisi perubahan pada kulit
            perubahan_kondisi_kulit = input(f"Apakah ada perubahan pada kulit atau bulu kambing?")
            # kondisi perubahan warna bau dan konsistensi pada kotoran kambing
            perubahan_kotoran = input(f" Apakah terdapat perubahan pada warna, bau, atau konsistensi kotoran kambing?")
            # kondisi perubahan warna bau urin 
            perubahan_warna_bau_urin = input(f"Apakah terdapat perubahan pada warna atau bau urin kambing?")
            # kondisi perubahan padd hasil produksi susu
            perubahan_produksi_susu = input(f"Apakah ada perubahan pada hasil produksi daging (jika kambing adalah kambing perahan)?")
            for value in [berat_badan,perubahan_makan_minum,perubahan_prilaku_makan,konsisi_lemas,perubahan_kondisi_kulit,perubahan_kotoran,perubahan_warna_bau_urin,perubahan_produksi_susu]:
                data_hasil_gejala.append(value)
            # data final yang sudah siap di tambpilkan
            data_final = []
            
            
            for value in range(0,len(data_gejala)):
                if data_hasil_gejala[value] == "ya":
                    data_final.append(data_gejala_solusi[data_gejala[value]])
                
                else:
                    pass
            if len(data_final) != 0:
                # menampilkan data
                print(tabulate(data_final,headers=["Gejala","penanganan"],tablefmt="grid"))
            else:
                print("Sapi dalam kondisi prima tidak ada gejala")

            return data_final
    
    def penempatan_kandang(self):
        if Susu_sapi.umur > 2: # 2 bulan usia sapi
            Susu_sapi.kandang = 'kandang sapi dewasa'
            print("berhasil melakukan penempatan")
        else:
            Susu_sapi.kandang = 'kandang sapi anakan'
            print("berhasil melakukan penempatan")
                        
class sapi(peternakan_hewan):
    def __init__(self,lokasi,nama_perusahaan,jenis,kandang,ras,berat,umur):
        super().__init__(lokasi,nama_perusahaan,jenis,kandang)
        self.ras = ras
        self.berat = berat
        self.umur = umur
    
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
    def __init__(self,lokasi,nama_perusahaan,jenis,kandang,ras,berat,umur):
        super().__init__(lokasi,nama_perusahaan,jenis,kandang)
        self.ras = ras
        self.berat = berat
        self.umur = umur
    
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
Peternakan_hewan = peternakan_hewan("CIkarang barat","PT agung bayu","sapi","Dewasa")
Sapi = sapi("CIkarang barat","PT agung bayu","sapi","Dewasa","Limousin",6,600) # waktu dalam bulan berat dalam kuwintal
Kambing = kambing("CIkarang barat","PT agung bayu","kambing","Dewasa","etawa",70,40) # waktu dalam bulan berat dalam kuwintal
Susu_sapi = sapi_susu("CIkarang barat","PT agung bayu","sapi","Dewasa","Limosin",6,6,10)
Daging_kambing = kambing_daging("CIkarang barat","PT agung bayu","kambing","Dewasa","etawa",70,7,30)

id_akun = 123
pass_akun = "agung"

def login():
    id = int(input("Masukan id anda   :"))
    password = input("Masukan password anda :")
    if id == id_akun and password == pass_akun:
        home()        
    
def home():
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
        jenis_hewan = input("Masukan jenis hewan... ")
        Peternakan_hewan.patau_kesehatan(jenis_hewan)
        
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
        data_sapi = []
        header = ["jenis","kandang","ras","berat","umur","jumlah produksi"]
        for value in [Susu_sapi.jenis,Susu_sapi.kandang,Susu_sapi.ras,Susu_sapi.berat,Susu_sapi.umur]:
            data_sapi.append(value)
        # menampilkan data
        print(data_sapi)
        # print(tabulate(data_sapi,header,tablefmt="Grid"))
        
    elif pilihan == 2:
        data_kambing = []
        header = ["jenis","kandang","ras","berat","umur"]
        for value in [Daging_kambing.jenis,Daging_kambing.kandang,Daging_kambing.ras,Daging_kambing.berat,Daging_kambing.umur]:
            data_kambing.append(value)
        # menampilkan data
        print(data_kambing)
        
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
    pilih_login = int(input("Masukan.... "))
    if pilih_login == 1:
        login()
    else:
        print("Salah tidak dapatk melakukan login")