def sisi():
    while True:
       try:
         sisi =input("sisi:").strip()
         if sisi =="":
            print("wajib di isi")
            continue

         if not sisi.isalpha():
            ubah_f =float(sisi)
            return ubah_f
         print("hanya boleh mengunakan huruf")
         
       except ValueError:
           print("hanya boleh mengunakan huruf")
           continue
       except Exception as pc:
           print(f"error:{pc}")

def Lebar():
    while True:
       try:
         Le =input("lebar:").strip()
         if Le =="":
            print("harus di isi!")
            continue
           
         if not Le.isalpha():
            ubah_La =float(Le)
            return ubah_La
         print("tidak boleh huruf!")
            
         
       except ValueError:
           print("tidak boleh huruf!")
           continue
         
       except Exception as xc:
           print(f"error:{xc}")

def panjang():
    while True:
       try:
         long =input("panjang:").strip()
         if long =="":
            print("harus di isi!")
            continue

         if not long.isalpha():
            ubah_long =float(long)
            return ubah_long
         print("harus berupa huruf")
         
       except ValueError:
           print("harus berupa huruf")
           continue
         
       except Exception as ion:
           print(f"error:{ion}")
         
def pilih():
    while True:
       try:
         his_pilih =input("pilihlah pilihan di atas:").strip()
         if his_pilih =="":
            print("pilihan harus di isi!")
            continue

         if not his_pilih.isdigit():
            print("tidak boleh mengunakan karakter lain selain angka")
            continue
         ubah_pilih =int(his_pilih)
         return ubah_pilih
         
       except ValueError:
           print("tidak voleh mengunakan karakter lain selain angka1")
           continue
         
       except Exception as tion:
           print(f"error:{tion}")
      
if __name__ =="__main__":
   pilih()
  