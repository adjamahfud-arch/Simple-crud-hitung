import json
import logging
from Convert import Convensi
from pathlib import Path

logging.basicConfig(
      filename="Simpan.log",
      level=logging.INFO,
      format="%(levelname)s - %(message)s"
)

file =Path("data/riyawat.json")

class Simpan:
    @staticmethod
    def load_file():
        try:
          loading =json.loads(
              file.read_text(encoding="utf-8")
          )
          return [Convensi.from_dict(x) for x in loading]

        except FileNotFoundError:
             logging.error("masih belum ada file")
             return []
        except (json.JSONDecodeError, KeyError) as jy:
             logging.exception("file rusak")
             print(f"file rusak:({jy})")
             return []
        except Exception as tion:
             logging.exception("error!")
             print(f"error:{tion}")
             return []
          
    @staticmethod
    def simpan_j(data):
        try:
          data_s =[u.to_dict() for u in data]
          file.write_text(
              json.dumps(data_s, ensure_ascii=False, indent=4),
              encoding="utf-8"
          )
          return True
          
        except OSError as es:
            logging.exception("error")
            print(f"error:({es})")
            return False
        except Exception as cpt:
            logging.exception("error")
            print(f"error:{cpt}")
            return False
          
    
          
          
          