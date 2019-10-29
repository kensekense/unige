#Ning
#26 October 2019
#Computer Security

import random
import numpy as np

def key_expansion(words):
    '''
    the input should be 4 words (128 bits) of the original input key in a list
    the yield should be the exapanded key (needed for each round of AES encryption) also in a list
    all keys should be bits, but stored as ints in python and converted when necessary
    '''

    #rc_i table given from the assignment is instantiated
    rc_i = (0x00, 0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1B, 0x36)

    #define N as the number of 32 words of the key
    if len(key) == 128:
        N = 4
        R = 11
    elif len(key) == 192:
        N = 6
        R = 13
    elif len(key) == 256:
        N = 8
        R = 15

    #key expansion proper?
    expanded_keys = []
    for i in range(0, R-1): #we want R-1 number of keys

        #define recon_i for word i
        rcon_i = int(format(rc_i[i],"#010b")[2:] + "000000000000000000000000",2)

        #initial 4 keys are just the 4 32 bits of the word in standard 128 key
        if i < N:
            expanded_keys.append(expanded_keys.append(words[i])) #just add as keys

        elif i >= N and i % N == 0 :
            expanded_keys.append(expanded_keys[i-N] ^ SBOX(ROTATION(expanded_keys[i-1])) ^ rcon_i

        elif i>= N and N > 6 and i % N == 4 :
            expanded_keys.append(expanded_keys[i-N] ^ SBOX(expanded_keys[i-1]))

        else:
            expanded_keys.append(expanded_keys[i-N] ^ expanded_keys[i-1])

    return expanded_keys


def SBOX(byte):
    '''
    should take a byte (8 bits) as an integer input,
    as we convert the integer and send back a replacement integer from the sbox
    '''
    #Sbox is given by the assignment, we convert to numpy array called sbox
    Sbox = (
                0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76,
                0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0,
                0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15,
                0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75,
                0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84,
                0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF,
                0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8,
                0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2,
                0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73,
                0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB,
                0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79,
                0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08,
                0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A,
                0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E,
                0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF,
                0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16
    )
    sbox = np.array(Sbox)
    sbox = np.reshape(sbox,(16,16)) #as it is meant to be

    #convert to 8bit binary
    byte = format(byte, '#010b')

    #in format 0b[aaaa][bbbb] meaning starting from index 2
    row = int(byte[2:6],2) #[aaaa]
    col = int(byte[6:11],2) #[bbbb]

    byte_rep = sbox[row][col] #int replacement

    return byte_rep

def ROTATION(byte):
    '''
    takes input byte (8 bits) and performs a one byte left circular shift
    '''
    byte = format(byte, "#010b")[2:] #takes the int and converts to shift
    byte = byte[1:] + byte[:1] #shifts 1 to the left

    return int(byte, 2) #returns as int

def shift_row(mat):
    '''
    takes a matrix input and shifts the rows.
    note that matrices are in row order for python.
    '''
    for i in range(0, len(mat)): #do for each row
        mat[i] = np.roll(mat[i], -i) #does a left shift by how deep in the row you are

    return mat

def inv_shift_row(mat):
    '''
    inverts the shift row
    '''
    for i in range(0, len(mat)): #do for each row
        mat[i] = np.roll(mat[i], i) #does a right shift by how deep in the row you are

    return mat

def mix_column(byte):

    #defining multiplication in field 2^8
    #understanding that multiplication is just a left-shift of one bit and a conditional XOR with 0x1B (00011011) if
    #the leftmost bit is 1 (checked via x & 0x80) because 0x80 is 10000000
    #we also have to keep it in the field, which is why we check with 0xFF
    #taken from aes implementation found on github
    mul_GF28 = lambda x: (((x << 1) ^ 0x1B) & 0xFF) if (x & 0x80) else (x << 1)

    a = byte[0] ^ byte[1] ^ byte[2] ^ byte[3]
    b = byte[0]
    byte[0] ^= a ^ mul_GF28(byte[0] ^ byte[1])
    byte[1] ^= a ^ mul_GF28(byte[1] ^ byte[2])
    byte[2] ^= a ^ mul_GF28(byte[2] ^ byte[3])
    byte[3] ^= a ^ mul_GF28(byte[3] ^ b)

    return byte

def mix_columns(mat):

    for i in range(0, 4):
        mat[i] = mix_column(mat[i])

    return word

def add_round_key(mat, key):
    '''
    XOR round key with word (32 bits)
    '''
    for i in range(0, 4):
        for j in range(0, 4):
            mat[i][j] ^= key[i][j]

    return mat

def encrypt(exp_keys, rounds):
    '''
    do AES encryption by inputting the expanded keys in list format (with each index holding a round key)
    also specify the number of rounds
    '''


if __name__ == "__main__":
