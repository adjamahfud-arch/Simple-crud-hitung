from datetime import datetime
import module.validasi as mv
from pathlib import Path
import sys

file_cd =Path(
     "/storage/emulated/0/proyek_hitung/service"
)
sys.path.insert(0, str(file_cd))
from service.Convert import Convensi
from service.service_2 import Simpan

format_w ="%H-%M %d %m %Y %A"

class Hitung:
   @staticmethod
   def l_kubus(s: int) -> int:
       try:
         pangkat =s ** 2
         hitung =6 * pangkat
         bulatkan =round(hitung)
         return bulatkan
       except ValueError:
           print("erorr nilai tidak sesuai")
       except Exception as Ep:
           print(f"error {Ep}")

   @staticmethod
   def l_segi_panjang(p: int, l: int) -> int:
       try:
         hitung1 =p * l 
         bulat =round(hitung1)
         return bulat
       except ValueError:
           print("error nilai tidak sesuai")
       except Exception as pl:
           print(f"error{pl}")
        
class Data:
   def __init__(self) -> None:
       self.data_frame =Simpan.load_file()

   def tambah(self, data_t):
       self.data_frame.append(data_t)

   def isi(self,op_name: str, hasil: int, waktu: str) -> None:
       creat_opp =Convensi(op_name,hasil,waktu)
       self.tambah(creat_opp)
       status =Simpan.simpan_j(self.data_frame)
       if status:
          print("data berhasil di simpan")

class Time:
   @staticmethod
   def waktu_now():
       waktu =datetime.now().strftime(format_w)
       return waktu
     
class Condisi:
   @staticmethod
   def condisi(pilih_: str):
       f_data =Data()
       try:
         if pilih_ ==1:
            nama_opr ="kubus"
            hs =mv.sisi()
            hasil =Hitung.l_kubus(hs)
            now_time =Time.waktu_now()
            f_data.isi(nama_opr,hasil,now_time)
            print(hasil)
            return True
         if pilih_ ==2:
            nama_ops ="segi panjang"
            pj =mv.panjang()
            lb =mv.Lebar()
            now_time =Time.waktu_now()
            hasilkan =Hitung.l_segi_panjang(pj,lb)
            f_data.isi(nama_ops,hasilkan,now_time)
            print(hasilkan)
            return True
         if pilih_ ==3:
             print("keluar dari program")
             return False
         else:
            print("pilihan tidak valid")
            return True
       except Exception as ex:
            print(f"error:{ex}")
   @staticmethod
   def muncul(skor: int) -> bool:
       try:
         if skor == 0:
            return False
         return True
       except Exception as cp:
           print(f"error:{cp}")

def ui():
   print("selamat datang  di program penggitung luas bangun")
   print("1.kubus")
   print("2.segi panjang")


if __name__ =="__main__":
  name_cls =Condisi()
  kesem = 0
  while True:
      try:
        stat =name_cls.muncul(kesem)
        if not stat:
           ui()
        pilihan =mv.pilih()
        status =name_cls.condisi(pilihan)
        if not status:
           break
        kesem += 1
      except Exception as el:
           print(f"error:{el}")
        
        
  
   
   

                 