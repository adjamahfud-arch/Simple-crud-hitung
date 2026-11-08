from dataclasses import dataclass, asdict

@dataclass
class Convensi:
    nama_op: str
    hasil_op: int
    waktu: str =""

    def to_dict(self) -> dict:
        return asdict(self)
      
    @classmethod
    def from_dict(cls, data):
        return cls(**data)
      