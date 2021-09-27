# Implementasi Affine Cipher di Python
 
# Algoritma Euclidean yang Diperluas untuk menemukan invers modular
# misalnya: modinv(7, 26) = 15
def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return gcd, x, y
 
def modinv(a, m):
    gcd, x, y = egcd(a, m)
    if gcd != 1:
        return None  # modular inverse does not exist
    else:
        return x % m
 
# fungsi enkripsi sandi affine
# mengembalikan teks sandi
def affine_encrypt(text, key):
    '''
    C = (a*P + b) % 26
    '''
    return ''.join([ chr((( key[0]*(ord(t) - ord('A')) + key[1] ) % 26)
                  + ord('A')) for t in text.upper().replace(' ', '') ])
 
 
# fungsi dekripsi sandi affine
# mengembalikan teks asli
def affine_decrypt(cipher, key):
    '''
    P = (a^-1 * (C - b)) % 26
    '''
    return ''.join([ chr((( modinv(key[0], 26)*(ord(c) - ord('A') - key[1]))
                    % 26) + ord('A')) for c in cipher ])
 
 
# Kode Driver untuk menguji fungsi di atas
def main():
    # mendeklarasikan teks dan kunci
    text = 'ILHAM HIDAYAT SIDIK'
    key = [7, 4]
 
    # memanggil fungsi enkripsi
    affine_encrypted_text = affine_encrypt(text, key)
 
    print('Encrypted Text: {}'.format( affine_encrypted_text ))
 
    # memanggil fungsi dekripsi
    print('Decrypted Text: {}'.format
    ( affine_decrypt(affine_encrypted_text, key) ))
 
 
if __name__ == '__main__':
    main()
