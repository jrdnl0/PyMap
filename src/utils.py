

import numpy as np
import sys
import os

# [CONSTANTS]
READ_BYTES = "rb"
WRITE_BYTES = "wb"
SEEK_SET = 0
SIZEOF_INT = 4
SIZEOF_SHORT = 2
SIZEOF_CHAR = 1
LITTLE_ENDIAN = "little"
BIG_ENDIAN = "big"




# Data Acqusition / File Manipulation Functions
def ReadBytes(FILE_NAME : str, offset : int, whence : int, size : int) -> None:
    FILE_P = open(FILE_NAME, READ_BYTES)
    FILE_P.seek(offset, whence)

    FILE_BYTES = FILE_P.read1(size)

    FILE_P.close()
    return FILE_BYTES


def ReadInteger(FILE) -> int:
    return int.from_bytes(FILE.read1(SIZEOF_INT), byteorder=LITTLE_ENDIAN, signed=False)

def ReadShort(FILE) -> int:
    return int.from_bytes(FILE.read1(SIZEOF_SHORT), byteorder=LITTLE_ENDIAN, signed=False)

def ReadChar(FILE) -> int:
    return int.from_bytes(FILE.read1(SIZEOF_CHAR), byteorder=LITTLE_ENDIAN, signed=False)


def BytesToInteger(B : bytes) -> int:
    """Takes a byte array / bytes-type and returns an integer version of that data (i.e. four bytes read little endian)"""
    return int.from_bytes(B, byteorder=LITTLE_ENDIAN, signed=False)

def BytesToShort(B : bytes) -> int:
    return int.from_bytes(B, byteorder=LITTLE_ENDIAN, signed=False)

def BytesToChar(B : bytes) -> int:
    return int.from_bytes(B, byteorder=LITTLE_ENDIAN, signed=False)


def CalculateStride(width : int, height : int, bits_per_pixel : int) -> int:
    bytes_per_pixel = int(bits_per_pixel / 8)
    alignment = 4
    stride = (((width * int((bytes_per_pixel / 8))) + (alignment - 1)) / alignment) * alignment
    stride = int(stride)
    return stride




# Box-Mueller and Noise Generation Functions

def BoxMueller(stddev : float, size : int = 1) -> np.ndarray:
    """
    Mathematical transformation that takes a uniformly distributed array of randomly generated numbers and turns them into a set of normally-distributed data
    with a standard deviation at the discretion of the user.
    """
    U1 = np.random.uniform(low=0.0, high=1.0, size=size)
    U2 = np.random.uniform(low=0.0, high=1.0, size=size)
    R = np.sqrt(2 * np.log(U1))
    THETA = (2 * np.pi * U2)

    X = np.abs(np.ceil(stddev * R * np.cos(THETA)))
    # Note : Y = np.abs(np.ceil(stddev * R * np.sin(THETA))) but technically we only need one return
    return X
