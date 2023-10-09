# Tugas Pertemuan 3 - Kriptografi
```
Dosen Pengampu   : Ahmad Turmudi Zy, S.Kom., M.Kom
Mata Kuliah      : Kriptografi
Nama             : Raihan Tantowi
Nim              : 312110229
Kelas            : TI.21.C.1
```
#### Kode program pada repo di github ini adalah sebuah sistem login sederhana menggunakan enkripsi Vigenère Cipher.
* **Berikut adalah 3 fungsi dalam kode program tersebut :**

1.) Fungsi `encrypt_vigenere(plain_text, key)`: Fungsi ini mengambil teks biasa (plain_text) dan kunci (key) sebagai input dan mengembalikan teks yang telah dienkripsi menggunakan Vigenère Cipher.

2.) Fungsi `decrypt_vigenere(encrypted_text, key)`: Fungsi ini mengambil teks terenkripsi (encrypted_text) dan kunci (key) sebagai input dan mengembalikan teks yang telah didekripsi menggunakan Vigenère Cipher.

3.) Fungsi `login()`: Fungsi ini meminta pengguna memasukkan username dan password. Password yang dimasukkan oleh pengguna dienkripsi menggunakan Vigenère Cipher sebelum dibandingkan dengan password terenkripsi yang telah disimpan. Jika username adalah "raihan" dan password terenkripsi cocok dengan password terenkripsi dari "raihan1234", maka pesan "Selamat Anda Berhasil Login!" akan ditampilkan; jika tidak, pesan "Maaf Login Anda Gagal!" akan ditampilkan.
###

* **Berikut adalah hasil dari program yang telah dibuat :**
#### Jika berhasil login
![Gambar 1](img/ss1.png)

#### Jika tidak berhasil login
![Gambar 2](img/ss2.png)



###
Pada contoh ini, enkripsi dan dekripsi Vigenère dilakukan dengan menggeser karakter-karakter teks menggunakan huruf-huruf kunci yang diulang-ulang. Namun, penting untuk dicatat bahwa penggunaan Vigenère Cipher untuk tujuan keamanan nyata tidak aman karena mudah dipecahkan. Kode ini hanya dimaksudkan untuk tujuan pendidikan dan ilustrasi. Dalam aplikasi nyata, yaitu harus menggunakan metode enkripsi yang lebih kuat dan aman, seperti AES (Advanced Encryption Standard), untuk mengamankan data pengguna.
