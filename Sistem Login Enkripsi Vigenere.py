# Fungsi untuk mengenkripsi teks menggunakan Vigenère Cipher
def encrypt_vigenere(plain_text, key):
    encrypted_text = ""
    key_repeated = key * (len(plain_text) // len(key)) + key[:len(plain_text) % len(key)]
    for i in range(len(plain_text)):
        char = plain_text[i]
        if char.isalpha():
            shift = ord(key_repeated[i].upper()) - 65
            if char.islower():
                encrypted_text += chr((ord(char) - 97 + shift) % 26 + 97)
            elif char.isupper():
                encrypted_text += chr((ord(char) - 65 + shift) % 26 + 65)
        else:
            encrypted_text += char
    return encrypted_text

# Fungsi untuk mendekripsi teks menggunakan Vigenère Cipher
def decrypt_vigenere(encrypted_text, key):
    decrypted_text = ""
    key_repeated = key * (len(encrypted_text) // len(key)) + key[:len(encrypted_text) % len(key)]
    for i in range(len(encrypted_text)):
        char = encrypted_text[i]
        if char.isalpha():
            shift = ord(key_repeated[i].upper()) - 65
            if char.islower():
                decrypted_text += chr((ord(char) - 97 - shift) % 26 + 97)
            elif char.isupper():
                decrypted_text += chr((ord(char) - 65 - shift) % 26 + 65)
        else:
            decrypted_text += char
    return decrypted_text

# Fungsi untuk proses login
def login():
    username = input("Masukkan username Anda: ")
    password = input("Masukkan password Anda: ")
    
    # Enkripsi password sebelum disimpan
    encrypted_password = encrypt_vigenere(password, "kunci")
    
    # Proses login dengan membandingkan dengan password terenkripsi yang sudah disimpan
    if username == "raihan" and encrypted_password == encrypt_vigenere("raihan1234", "kunci"):
        print("")
        print("============================")
        print("Selamat Anda Berhasil Login!")
        print("============================")
    else:
        print("")
        print("======================")
        print("Maaf Login Anda Gagal!")
        print("======================")

# Contoh penggunaan
login()
