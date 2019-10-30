#following the implementation found on https://github.com/boppreh/aes/blob/master/aes.py
#load the Sbox and Sbox_inv into our python file
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
Sbox_inv = (
            0x52, 0x09, 0x6A, 0xD5, 0x30, 0x36, 0xA5, 0x38, 0xBF, 0x40, 0xA3, 0x9E, 0x81, 0xF3, 0xD7, 0xFB,
            0x7C, 0xE3, 0x39, 0x82, 0x9B, 0x2F, 0xFF, 0x87, 0x34, 0x8E, 0x43, 0x44, 0xC4, 0xDE, 0xE9, 0xCB,
            0x54, 0x7B, 0x94, 0x32, 0xA6, 0xC2, 0x23, 0x3D, 0xEE, 0x4C, 0x95, 0x0B, 0x42, 0xFA, 0xC3, 0x4E,
            0x08, 0x2E, 0xA1, 0x66, 0x28, 0xD9, 0x24, 0xB2, 0x76, 0x5B, 0xA2, 0x49, 0x6D, 0x8B, 0xD1, 0x25,
            0x72, 0xF8, 0xF6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xD4, 0xA4, 0x5C, 0xCC, 0x5D, 0x65, 0xB6, 0x92,
            0x6C, 0x70, 0x48, 0x50, 0xFD, 0xED, 0xB9, 0xDA, 0x5E, 0x15, 0x46, 0x57, 0xA7, 0x8D, 0x9D, 0x84,
            0x90, 0xD8, 0xAB, 0x00, 0x8C, 0xBC, 0xD3, 0x0A, 0xF7, 0xE4, 0x58, 0x05, 0xB8, 0xB3, 0x45, 0x06,
            0xD0, 0x2C, 0x1E, 0x8F, 0xCA, 0x3F, 0x0F, 0x02, 0xC1, 0xAF, 0xBD, 0x03, 0x01, 0x13, 0x8A, 0x6B,
            0x3A, 0x91, 0x11, 0x41, 0x4F, 0x67, 0xDC, 0xEA, 0x97, 0xF2, 0xCF, 0xCE, 0xF0, 0xB4, 0xE6, 0x73,
            0x96, 0xAC, 0x74, 0x22, 0xE7, 0xAD, 0x35, 0x85, 0xE2, 0xF9, 0x37, 0xE8, 0x1C, 0x75, 0xDF, 0x6E,
            0x47, 0xF1, 0x1A, 0x71, 0x1D, 0x29, 0xC5, 0x89, 0x6F, 0xB7, 0x62, 0x0E, 0xAA, 0x18, 0xBE, 0x1B,
            0xFC, 0x56, 0x3E, 0x4B, 0xC6, 0xD2, 0x79, 0x20, 0x9A, 0xDB, 0xC0, 0xFE, 0x78, 0xCD, 0x5A, 0xF4,
            0x1F, 0xDD, 0xA8, 0x33, 0x88, 0x07, 0xC7, 0x31, 0xB1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xEC, 0x5F,
            0x60, 0x51, 0x7F, 0xA9, 0x19, 0xB5, 0x4A, 0x0D, 0x2D, 0xE5, 0x7A, 0x9F, 0x93, 0xC9, 0x9C, 0xEF,
            0xA0, 0xE0, 0x3B, 0x4D, 0xAE, 0x2A, 0xF5, 0xB0, 0xC8, 0xEB, 0xBB, 0x3C, 0x83, 0x53, 0x99, 0x61,
            0x17, 0x2B, 0x04, 0x7E, 0xBA, 0x77, 0xD6, 0x26, 0xE1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0C, 0x7D
            )

rcon_i = (0x00, 0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1B, 0x36)

'''
byte = 8 bits
plaintext is in 128-bits blocks
mat is a 4x4 matrix of bytes
'''

#define the actions performed per round
def sub_bytes(mat):
    for i in range(0, 4):
        for j in range(0, 4):
            mat[i][j] = Sbox[mat[i][j]] #Sbox will return the replacement for each bit of the 4x4 mat

def sub_bytes_inv(mat):
    for i in range(0, 4):
        for j in range(0, 4):
            mat[i][j] = Sbox_inv[mat[i][j]] #Sbox_inv will return the replacement for each bit of the 4x4 mat

def shift_rows(mat):
    #shifting rows in a 4x4 will leave the first row untouched and the last 3 touched
    #done by moving the column values one over (rolling and wrapping around)
    mat[0][1], mat[1][1], mat[2][1], mat[3][1] = mat[1][1], mat[2][1], mat[3][1], mat[0][1]
    mat[0][2], mat[1][2], mat[2][2], mat[3][2] = mat[2][2], mat[3][2], mat[0][2], mat[1][2]
    mat[0][3], mat[1][3], mat[2][3], mat[3][3] = mat[3][3], mat[0][3], mat[1][3], mat[2][3]

def shift_rows_inv(mat):
    #the inverse is just the reverse direction
    mat[0][1], mat[1][1], mat[2][1], mat[3][1] = mat[3][1], mat[0][1], mat[1][1], mat[2][1]
    mat[0][2], mat[1][2], mat[2][2], mat[3][2] = mat[2][2], mat[3][2], mat[0][2], mat[1][2]
    mat[0][3], mat[1][3], mat[2][3], mat[3][3] = mat[1][3], mat[2][3], mat[3][3], mat[0][3]

def add_round_key(mat, key):
    #adding round key is a XOR with the provided key
    for i in range(0, 4):
        for j in range(0, 4):
            mat[i][j] ^= key[i][j]


#defining multiplication in field 2^8
#understanding that multiplication is just a left-shift of one bit and a conditional XOR with 0x1B (00011011) if
#the leftmost bit is 1 (checked via x &ing 0x80) because 0x80 is 10000000 so it's the leftmost bit as 1
#we also have to keep it 8 bits since that's the size we want to work with, which is why with & with 0xFF, since 0xFF is all 8 bits of 1s
mul_GF28 = lambda x: (((x << 1) ^ 0x1B) & 0xFF) if (x & 0x80) else (x << 1)

def mix_column(col):

    a = col[0] ^ col[1] ^ col[2] ^ col[3]
    b = col[0]
    col[0] ^= a ^ mul_GF28(col[0] ^ col[1]) #multiply each column value and add, like matrix multiplication,
    col[1] ^= a ^ mul_GF28(col[1] ^ col[2])
    col[2] ^= a ^ mul_GF28(col[2] ^ col[3])
    col[3] ^= a ^ mul_GF28(col[3] ^ b)


def mix_columns(mat):

    for i in range(0, 4): #for 4x4 matrix
        mix_column(mat[i]) #do for each column

def mix_columns_inv(mat):

    for i in range(0, 4): #for 4x4 matrix
        a = mul_GF28(mul_GF28(mat[i][0] ^ mat[i][2])) #it is essentially a wrap around since we are in a field
        b = mul_GF28(mul_GF28(mat[i][1] ^ mat[i][3]))
        mat[i][0] ^= a #applying it twice and XOR'ing it with the column again
        mat[i][1] ^= b
        mat[i][2] ^= a
        mat[i][3] ^= b

    mix_columns(mat)

def make_mat(text):
    return [list(text[i:i+4]) for i in range(0, len(text), 4)] #returns a list of lists (which makes a matrix 4x4) in col order

def make_128bits(mat):
    return bytes(sum(mat, [])) #returns a list which is the 4x4 matrix flattened

def XOR_bytes(a, b):
    return bytes(i^j for i,j in zip(a,b))

def make_split(text, size):
    return [text[i:i+16] for i in range(0, len(text), size)] #make sizes blocks of 16

#AES Proper
def key_expansion(init_key):

    #make sure the init_key is in the right format
    key_col = make_mat(init_key)

    #since the key is 128 bits, 192 bits, or 256 bits represented by hex, size 16 24, 32
    num_rounds = {16: 10, 24: 12, 32: 14}
    N = num_rounds[len(init_key)]

    #other initializations
    iterations = len(init_key) // 4 #we split the rounds
    i = 1

    while(len(key_col) < (N+1)*4): #while there is still key to go around

        word = list(key_col[-1]) #take the previous sub_key

        if len(key_col) % iterations == 0:
            word.append(word.pop(0)) #circular shift
            word = [Sbox[b] for b in word] #apply sbox
            word[0] ^= rcon_i[i] #XOR with r_con
            i += 1

        elif len(init_key) == 32 and len(key_col) % iterations == 4: #todo when 256-bit key is used
            word = [Sbox[b] for b in word]

        word = XOR_bytes(word, key_col[-iterations])
        key_col.append(word)

    return N, [key_col[4*i:4*(i+1)] for i in range(len(key_col)//4)] #return keys in chunks of 4x4 bytes

def encrypt(plaintext, my_keys, R):
    '''
    plaintext should be 16 bytes long (128 bits)
    '''
    assert len(plaintext) == 16

    plain = make_mat(plaintext) #turn to 4x4

    add_round_key(plain, my_keys[0]) #initial step is an XOR with the first sub_key

    for i in range(1, R): #do the rounds
        sub_bytes(plain)
        shift_rows(plain)
        mix_columns(plain)
        add_round_key(plain, my_keys[i]) #add the round key

    #last round is no mix_cols
    sub_bytes(plain)
    shift_rows(plain)
    add_round_key(plain, my_keys[-1]) #add the last key

    return make_128bits(plain) #return as len 128 bit encrypted

def decrypt(ciphertext, my_keys, R):
    '''
    ciphertext should be 16 bytes long (128 bits)
    '''
    assert len(ciphertext) == 16

    cipher = make_mat(ciphertext) #turn to 4x4

    #do the first stage of decryption, which is the inverse of the last stage of encryption (without mix col)
    add_round_key(cipher, my_keys[-1]) #the last round-key
    shift_rows_inv(cipher)
    sub_bytes_inv(cipher)

    #do the rounds
    for i in range(R-1, 0, -1): #do it in reverse
        add_round_key(cipher, my_keys[i]) #add round key
        mix_columns_inv(cipher) #inverse col mix
        shift_rows_inv(cipher) #inverse shift row
        sub_bytes_inv(cipher) #inverse byte sub

    #add the round key that we init'd with in the encrypt stage
    add_round_key(cipher, my_keys[0]) #the first round-key

    return make_128bits(cipher) #return as len 128 bit decrypted

def CBC_encrypt(plaintext, IV, my_keys, R):
    '''
    XOR with an IV
    '''
    chunks = []
    prev = IV

    for plain_chunks in make_split(plaintext, 16):
        #XOR with IV or previous plaintext
        chunk = encrypt(XOR_bytes(plain_chunks, prev), my_keys, R)
        chunks.append(chunk)
        prev = chunk #set the new prev to be the last added plaintext

    return b''.join(chunks) #return as bits

def CBC_decrypt(ciphertext, IV, my_keys, R):

    chunks = []
    prev = IV

    for cipher_chunk in make_split(ciphertext, 16):
        chunks.append(XOR_bytes(prev, decrypt(cipher_chunk, my_keys, R))) #XOR with the decrypt at each step to undo XOR with each chunk
        prev = cipher_chunk #set the new chunk

    return b''.join(chunks) #return as bits

if __name__ == "__main__":

    #for testing purposes
    initial_key = [0x54, 0x68, 0x61, 0x74, 0x73, 0x20, 0x6D, 0x79, 0x20, 0x4B, 0x75, 0x6E, 0x67, 0x20, 0x46, 0x75]
    plain_text = [0x54, 0x77, 0x6F, 0x20, 0x4F, 0x6E, 0x65, 0x20, 0x4E, 0x69, 0x6E, 0x65, 0x20, 0x54, 0x77, 0x6F]

    #expand keys to encrypt
    N, my_keys = key_expansion(initial_key)

    #test encryption
    encrypted_text = encrypt(plain_text, my_keys, N)

    #test decryption
    decrypted_text = decrypt(encrypted_text, my_keys, N)

    print(encrypted_text)
    print(decrypted_text, "\n") #should output the plain_text

    #test CBC
    cbc_e_text = CBC_encrypt(plain_text, initial_key, my_keys, N) #using initial key as IV value, just for consistency not for security
    cbc_d_text = CBC_decrypt(cbc_e_text, initial_key, my_keys, N)

    print(cbc_e_text)
    print(cbc_d_text) #should be the plain_text
