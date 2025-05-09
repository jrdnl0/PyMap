
import numpy as np
from dataclasses import dataclass
import utils as ut


type Pixel = list[int, int, int]



class Header:
    def __init__(self, FILE_NAME : str) -> None:

        self.FILE_NAME = FILE_NAME
        self.FILE_RAW = ut.ReadBytes(self.FILE_NAME, 0, 0, 14)

        self.SIGNATURE = ut.BytesToInteger(self.FILE_RAW[0:2])
        self.FILE_SIZE = ut.BytesToInteger(self.FILE_RAW[2:6])
        self.RESERVED1 = ut.BytesToInteger(self.FILE_RAW[6:8])
        self.RESERVED2 = ut.BytesToInteger(self.FILE_RAW[8:10])
        self.HEAD_SIZE = ut.BytesToInteger(self.FILE_RAW[10:14])

        return None


    def PrintHeader(self) -> None:
        print(f"Header.SIGNATURE : {self.SIGNATURE}")
        print(f"Header.FILE_SIZE : {self.FILE_SIZE}")
        print(f"Header.RESERVED1 = {self.RESERVED1}")
        print(f"Header.RESERVED2 = {self.RESERVED2}")
        print(f"Header.HEAD_SIZE = {self.HEAD_SIZE}")
        return None



class InfoHeader:
    def __init__(self, FILE_NAME : str) -> None:

        self.FILE_NAME = FILE_NAME
        self.FILE_RAW = ut.ReadBytes(self.FILE_NAME, 14, 0, 40)



        self.HEADER_SIZE   = ut.BytesToInteger(self.FILE_RAW[0:4])
        self.IMAGE_WIDTH  = ut.BytesToInteger(self.FILE_RAW[4:8])
        self.IMAGE_HEIGHT = ut.BytesToInteger(self.FILE_RAW[8:12])
        self.IMAGE_PLANE  = ut.BytesToInteger(self.FILE_RAW[12:14])
        self.BITS_PER_PIXEL = ut.BytesToInteger(self.FILE_RAW[14:16])
        self.IMAGE_COMPRESSION = ut.BytesToInteger(self.FILE_RAW[16:20])
        self.IMAGE_SIZE = ut.BytesToInteger(self.FILE_RAW[20:24])
        self.X_RESOLUTION = ut.BytesToInteger(self.FILE_RAW[24:28])
        self.Y_RESOLUTION = ut.BytesToInteger(self.FILE_RAW[28:32])
        self.COLORS_USED  = ut.BytesToInteger(self.FILE_RAW[32:36])
        self.IMPORTANT_COLORS = ut.BytesToInteger(self.FILE_RAW[36:40])


        return None

    def PrintInfoHeader(self) -> None:

        print(f"InfoHeader.HEADER_SIZE = {self.HEADER_SIZE}")
        print(f"InfoHeader.IMAGE_WIDTH = {self.IMAGE_WIDTH}")
        print(f"InfoHeader.IMAGE_HEIGHT = {self.IMAGE_HEIGHT}")
        print(f"InfoHeader.BITS_PER_PIXEL = {self.BITS_PER_PIXEL}")
        print(f"InfoHeader.IMAGE_COMPRESSION = {self.IMAGE_COMPRESSION}")
        print(f"InfoHeader.IMAGE_SIZE = {self.IMAGE_SIZE}")
        print(f"InfoHeader.X_RESOLUTION = {self.X_RESOLUTION}")
        print(f"InfoHeader.Y_RESOLUTION = {self.Y_RESOLUTION}")
        print(f"InfoHeader.COLORS_USED = {self.COLORS_USED}")
        print(f"InfoHeader.IMPORTANT_COLORS = {self.IMPORTANT_COLORS}")

        return None



@dataclass
class Pixel:
    RED : int
    GREEN : int
    BLUE : int




