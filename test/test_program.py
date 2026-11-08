from main_hitung import Data
import pytest

def test_isi():
    Data.isi("kubus",70)
    assert len(Data.data_frame) == 0
  