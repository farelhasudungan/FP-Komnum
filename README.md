# Laporan Tugas Program Komnum

Kami dari kelompok A19 yang beranggotakan:
|    NRP     |      Name      |
| :--------: | :------------: |
| 5025241016 | Farrel Hasudungan Immanuel Limbong |
| 5025241025 | Tobias Orlando Purba |
| 5025241085 | Mario Napitupulu |
| 5025241096 | Willy Marcelius |
| 5025241122 | Rennard Filbert Tanjaya |

Berikut penjelasan dari kode program komnum untuk soal nomor 2:

### Soal
![image](https://github.com/user-attachments/assets/5862bb2d-1db0-497e-8f07-9e41525344c4)

### Penjelasan kode
```py
import numpy as np
from sympy import *
```
- `import numpy as np`  mengimpor library NumPy dan memberi alias np, NumPy adalah library populer untuk komputasi numerik dan array/matriks di Python
- `from sympy import *` mengimpor semua fungsi dan kelas dari library SymPy, yaitu library untuk komputasi simbolik, seperti symbols(), solve(), diff(), integrate(), dsb

```py
def error_true(y_real, x_n):
    return abs((y_real - x_n) / y_real)
```
- Fungsi ini menghitung galat relatif terhadap nilai sebenarnya (true error)
- `y_real` merupakan nilai akar yang sebenarnya
- `x_n` merupakan hasil aproksimasi akar dari metode numerik
- `abs()` merupakan fungsi bawaan Python untuk nilai mutlak

```py
def error_aprox(x_n, x0):
    return abs((x_n - x0) / x_n) if x_n != 0 else float('inf')
```
- Menghitung error aproksimasi antara iterasi sekarang (x_n) dan sebelumnya (x0)
- Jika x_n == 0, untuk menghindari pembagian dengan nol, maka fungsi akan mengembalikan float('inf') (tak hingga)

```py
def f(x):
    return x**3 + x**2 - 34*x - 56 
```
- Ini adalah fungsi yang ingin dicari akar-nya (nilai 𝑥 yang membuat 𝑓(𝑥)=0

```py
def bisection(xl, xu, x_true, max_iter=3, tol=1e-5):
```
- `xl` merupakan batas bawah interval
- `xu` merupakan batas atas interval
- `x_true` merupakan nilai akar sebenarnya (untuk menghitung error terhadap nilai asli)
- `max_iter` merupakan jumlah maksimum iterasi (dalam kasus ini maksimum iterasi = 3)
- `tol` merupakan toleransi (batas bawah error aproksimasi untuk menghentikan iterasi)

```py
print(f"{'Iter':<5}{'XL':<10}{'XU':<10}{'XR':<10}{'f(XR)':<12}{'ε_t (%)':<10}{'ε_a (%)':<10}")
print("-" * 65)
```
- Mencetak judul kolom hasil iterasi
- `Iter` merupakan nomor iterasi
- `XL, XU` merupakan batas bawah dan atas
- `XR` merupakan titik tengah (nilai estimasi akar)
- `f(XR)` merupakan nilai fungsi di XR
- `ε_t (%)` merupakan error true terhadap akar sebenarnya
- `ε_a (%)` merupakan error aproksimasi antar iterasi
- `:<5, :<10` adalah formatting string untuk membuat rata kiri dan lebar kolom

```py
xr_old = None
for i in range(1, max_iter+1):
```
- `xr_old` digunakan untuk menyimpan nilai sebelumnya dari xr, agar bisa menghitung error aproksimasi antar iterasi
- `for i in range(1, max_iter+1)` menjalankan iterasi mulai dari 1 sampai max_iter

```py
xr = (xl + xu) / 2
f_xr = f(xr)
```
- `xr` merupakan nilai tengah antara xl dan xu, yaitu tebakan akar saat ini
- `f_xr` merupakan nilai fungsi di titik tengah

```py
et = abs((x_true - xr) / x_true) * 100
```
- Menghitung error true terhadap nilai sebenarnya dalam persen

```py
ea = abs((xr - xr_old) / xr) * 100 if xr_old is not None else None
```
- Menghitung error aproksimasi antar iterasi jika sudah ada nilai xr_old dari iterasi sebelumnya

```py
ea_str = f"{ea:.2f}" if ea is not None else "-"
print(f"{i:<5}{xl:<10.2f}{xu:<10.2f}{xr:<10.2f}{f_xr:<12.2f}{et:<10.2f}{ea_str:<10}")
```
- Cetak semua nilai hasil iterasi dengan format dua angka desimal
- Jika `ea` belum tersedia (iterasi pertama), tampilkan `-`

```py
if ea is not None and ea < tol:
    break
```
- Jika error aproksimasi sudah lebih kecil dari toleransi, hentikan iterasi (konvergen)

```py
if f(xl) * f_xr < 0:
    xu = xr
else:
    xl = xr
```
- Cek tanda dari hasil kali `f(xl) * f(xr)`:
  - Jika negatif, akar ada di antara `xl` dan `xr` → geser `xu` ke `xr`
  - Jika positif atau nol, akar ada di antara `xr` dan `xu` → geser `xl` ke `xr`

```py
xr_old = xr
```
- Simpan nilai `xr` sekarang untuk digunakan pada iterasi berikutnya sebagai `xr_old`

```py
bisection(xl = -2, xu = 3, x_true=2)
```
- Jalankan fungsi bisection dengan:
  - Batas bawah: `-2`
  - Batas atas: `3`
  - Nilai akar sebenarnya: `2`
