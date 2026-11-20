# 🧮 Kalkulator Sederhana Berbasis Python

Program kalkulator sederhana berbasis terminal yang dibuat menggunakan Python. Program ini bisa melakukan 4 operasi matematika dasar: penjumlahan, pengurangan, perkalian, dan pembagian — lengkap dengan penanganan error agar tidak crash saat input salah.

---

## ✨ Fitur

| No | Fitur | Deskripsi |
|----|-------|-----------|
| 1 | ➕ Penjumlahan | Menjumlahkan dua angka |
| 2 | ➖ Pengurangan | Mengurangkan dua angka |
| 3 | ✖️ Perkalian | Mengalikan dua angka |
| 4 | ➗ Pembagian | Membagi dua angka (dengan proteksi bagi nol) |
| 5 | 🚪 Keluar | Keluar dari program |

---

## 🗂️ Struktur Program

```
kalkulator-berbasis-python-/
│
├── kalkulator.py    # File utama program kalkulator
└── README.md        # Dokumentasi proyek ini
```

---

## ⚙️ Cara Kerja Program

Program berjalan menggunakan **loop menu utama** (`app_menu()`). Setiap kali program dijalankan, muncul menu pilihan. Pengguna memasukkan nomor pilihan, lalu program menjalankan fungsi yang sesuai.

### Alur Program:

```
Jalankan kalkulator.py
        ↓
  Tampil Menu Utama
  1. Penjumlahan
  2. Pengurangan
  3. Perkalian
  4. Pembagian
  5. Keluar
        ↓
  User input pilihan
        ↓
  ┌─────────────────────────────────────────┐
  │  Pilih 1 → app_penjumlahan()            │
  │  Pilih 2 → app_pengurangan()            │
  │  Pilih 3 → app_perkalian()              │
  │  Pilih 4 → app_pembagian()              │
  │  Pilih 5 → Keluar / break               │
  └─────────────────────────────────────────┘
        ↓
  Input 2 angka → Hitung → Tampilkan hasil
        ↓
  Tekan Enter → Kembali ke Menu Utama
```

### Fungsi-fungsi dalam program:

- **`app_menu()`** — Fungsi utama yang menampilkan menu dan mengarahkan ke fungsi lain berdasarkan pilihan user. Menggunakan `while True` agar menu terus muncul sampai user memilih keluar.

- **`app_penjumlahan()`** — Meminta 2 angka dari user, lalu menjumlahkannya.

- **`app_pengurangan()`** — Meminta 2 angka dari user, lalu mengurangkannya.

- **`app_perkalian()`** — Meminta 2 angka dari user, lalu mengalikannya.

- **`app_pembagian()`** — Meminta 2 angka dari user, lalu membaginya. Dilindungi dari error bagi nol (`ZeroDivisionError`).

---

## 🛡️ Penanganan Error

Program ini sudah dilengkapi error handling sehingga tidak akan crash jika user salah input.

| Error | Penyebab | Pesan yang muncul |
|-------|----------|-------------------|
| `ValueError` | Input bukan angka (misal huruf atau simbol) | `"Eror: Masukan angka yang valid"` |
| `ZeroDivisionError` | Angka kedua diisi 0 saat pembagian | `"Eror: Tidak bisa membagi dengan nol"` |

---

## 🖥️ Cara Menjalankan Program

### Prasyarat

Pastikan **Python** sudah terinstall di komputermu.

**Cek apakah Python sudah ada:**
```bash
python --version
```
atau
```bash
python3 --version
```

Jika belum ada, download Python di: **https://www.python.org/downloads/**
> Pilih versi terbaru, centang **"Add Python to PATH"** saat instalasi (Windows).

---

### Langkah Menjalankan

**1. Clone atau download repo ini:**
```bash
git clone https://github.com/username/kalkulator-berbasis-python-.git
cd kalkulator-berbasis-python-
```

**2. Jalankan programnya:**
```bash
python kalkulator.py
```
atau (Linux/Mac):
```bash
python3 kalkulator.py
```

**3. Ikuti instruksi di layar — masukkan pilihan menu, lalu masukkan angka-angka yang diminta.**

---

## 📸 Contoh Tampilan Program

```
*** Program Kalkulator sedrhana for all ***
1. Penjumlahan
2. pengurangan
3. Perkalian
4. Pembagian
5. keluar
*** Program Kalkulator Sederhana ***
Pilihan: 1

*** Program Penjumlahan ***
angka1: 10
angka2: 5
hasil penjumlahan 15
*** Program penjumlahan selesai ***
Enter untuk lanjut
```

---

## 🔧 Kebutuhan Sistem

- Python **3.x** (tidak perlu install library tambahan apapun)
- Terminal / Command Prompt / PowerShell
- Tidak butuh koneksi internet

---

## 👨‍💻 Dibuat Oleh

Dibuat sebagai proyek belajar Python dasar — cocok untuk pemula yang ingin memahami:
- Fungsi (`def`)
- Input / Output
- Kondisi `if-elif-else`
- Perulangan `while`
- Penanganan error `try-except`

---

> ⭐ Kalau project ini bermanfaat, jangan lupa kasih bintang di GitHub ya!
