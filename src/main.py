"""

BAIC BITMAP LIBRARY FOR PYTHON
(BBLFP)

Author : Jacob Daniel

"""

# Imports
import sys
import numpy as np
from dataclasses import dataclass


# Defintions
BLACK_BUCK_IMG = "blackbuck.bmp"
BLACK_SQUARE_IMG = "BlackSquare(97x97).bmp"
ORANGE_SQUARE_IMG = "OrangeSquare(97x97).bmp"


# Basic Utility Functions


def ReadBytes(FILE_NAME: str, offset: int, whence: int, size: int) -> bytes:
    FILE = open(FILE_NAME, "rb")
    FILE.seek(offset, whence)

    FILE_BYTES = FILE.read1(size)

    FILE.close()
    return FILE_BYTES


def ReadInteger(FILE) -> int:
    return int.from_bytes(FILE.read1(4), byteorder="little", signed=False)


def ReadShort(FILE) -> int:
    return int.from_bytes(FILE.read1(2), byteorder="little", signed=False)


def ByteToInteger(B: bytes) -> int:
    return int.from_bytes(B, byteorder="little", signed=False)


def BoxMuellerMethod(stddev: float, size: int) -> np.ndarray:
    """Returns a randomly distributed set of numbers in the scope of [0, 1]"""
    U1 = np.random.uniform(low=0.0, high=1.0, size=size)
    U2 = np.random.uniform(low=0.0, high=1.0, size=size)

    R = np.sqrt(-2 * np.log(U1))
    THETA = 2 * np.pi * U2

    X = stddev * np.abs(np.ceil(R * np.cos(THETA)))
    return X


# Basic Image Header Classes
@dataclass
class BMP_HEADER:
    SIGNATURE: int
    FILE_SIZE: int
    RESERVED1: int
    RESERVED2: int
    DATA_OFFSET: int
    LINKED_FILE: str

    def INIT_HEADER(self) -> None:
        pFILE = open(self.LINKED_FILE, "rb")
        self.SIGNATURE = ReadShort(pFILE)
        self.FILE_SIZE = ReadInteger(pFILE)
        self.RESERVED1 = ReadShort(pFILE)
        self.RESERVED2 = ReadShort(pFILE)
        self.DATA_OFFSET = ReadInteger(pFILE)

        pFILE.close()
        return None

    def PrintBitmapHeader(self) -> None:
        print(f"Signature : {self.SIGNATURE}")
        print(f"File Size : {self.FILE_SIZE}")
        print(f"Reserved 1: {self.RESERVED1}")
        print(f"Reserved 2 : {self.RESERVED2}")
        print(f"Header Size : {self.DATA_OFFSET}")
        return None


@dataclass
class BMP_INFO:
    HEADER_SIZE: int
    IMAGE_WIDTH: int
    IMAGE_HEIGHT: int
    IMAGE_PLANES: int
    BITS_PER_PIXEL: int
    IMG_COMPRESSION: int
    IMAGE_SIZE: int
    X_RESOLUTION: int
    Y_RESOLUTION: int
    COLORS_USED: int
    IMP_COLORS: int
    LINKED_FILE: str

    def INIT_INFO(self) -> None:
        pFILE = open(self.LINKED_FILE, "rb")
        pFILE.seek(14, 0)

        self.HEADER_SIZE = ReadInteger(pFILE)
        self.IMAGE_WIDTH = ReadInteger(pFILE)
        self.IMAGE_HEIGHT = ReadInteger(pFILE)
        self.IMAGE_PLANES = ReadShort(pFILE)
        self.BITS_PER_PIXEL = ReadShort(pFILE)
        self.IMG_COMPRESSION = ReadInteger(pFILE)
        self.IMAGE_SIZE = ReadInteger(pFILE)
        self.X_RESOLUTION = ReadInteger(pFILE)
        self.Y_RESOLUTION = ReadInteger(pFILE)
        self.COLORS_USED = ReadInteger(pFILE)
        self.IMP_COLORS = ReadInteger(pFILE)

        pFILE.close()
        return None

    def PrintInfoHeader(self) -> None:
        print(f"Header Size : {self.HEADER_SIZE}")
        print(f"Image Width : {self.IMAGE_WIDTH}")
        print(f"Image Height : {self.IMAGE_HEIGHT}")
        print(f"Image Planes : {self.IMAGE_PLANES}")
        print(f"Bits Per Pixel : {self.BITS_PER_PIXEL}")
        print(f"Image Compression : {self.IMG_COMPRESSION}")
        print(f"Image Size : {self.IMAGE_SIZE}")
        print(f"X Resolution : {self.X_RESOLUTION}")
        print(f"Y Resolution : {self.Y_RESOLUTION}")
        print(f"Colors Used : {self.COLORS_USED}")
        print(f"Important Colors : {self.IMP_COLORS}")

        return None


def CreateInfoHeader(file_name: str) -> BMP_INFO:
    NEW_INFO_HEADER = BMP_INFO
    NEW_INFO_HEADER.LINKED_FILE = file_name
    NEW_INFO_HEADER.INIT_INFO(NEW_INFO_HEADER)
    return NEW_INFO_HEADER


def CreateHeader(file_name: str) -> BMP_HEADER:
    NEW_HEADER = BMP_HEADER
    NEW_HEADER.LINKED_FILE = file_name
    NEW_HEADER.INIT_HEADER(NEW_HEADER)
    return NEW_HEADER


@dataclass
class Pixel:
    RED: int
    GREEN: int
    BLUE: int

    def PrintPixel(self) -> None:
        print(f"{self.RED}.{self.GREEN}.{self.BLUE}")
        return None


class BitmapImage:
    def __init__(self, file_name: str) -> None:
        self.linked_file = file_name
        self.IMAGE_HEADER = CreateHeader(self.linked_file)
        self.IMAGE_INFO = CreateInfoHeader(self.linked_file)
        self.PixelMatrix = None
        self.ReadPixels()
        return None

    def PrintInfoHeader(self) -> None:
        self.IMAGE_INFO.PrintInfoHeader(self.IMAGE_INFO)
        return None

    def PrintHeader(self) -> None:
        self.IMAGE_HEADER.PrintBitmapHeader(self.IMAGE_HEADER)
        return None

    def ReadPixels(self) -> None:
        self.PixelMatrix = np.array([int(B) for B in ReadBytes(self.linked_file, 54, 0, self.IMAGE_INFO.IMAGE_SIZE)][::-1])
        np.array_split(self.PixelMatrix, 3)
        return None

