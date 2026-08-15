# 📱 Android App Prompt: Kas Remaja RT 04

Gunakan dokumen ini sebagai instruksi (prompt) utama jika Anda ingin men-generate atau membangun aplikasi Android (Native Kotlin dengan Jetpack Compose) yang terhubung ke Backend Kas Remaja RT 04.

---

## 1. 🌐 Struktur API & Endpoint
**Base URL:** `https://[MASUKKAN_URL_BACKEND_ANDA]/api`
*(Seluruh request menggunakan HTTP GET/POST/PUT/DELETE dengan tipe konten `application/json`)*

### A. Autentikasi (Login)
- **Endpoint:** `POST /api/login`
- **Payload:**
```json
{
  "username": "admin",
  "password": "password123"
}
```
- **Response JSON:**
```json
{
  "success": true,
  "message": "Login berhasil",
  "token": "token_string_here",
  "admin": {
    "username": "admin",
    "nama_lengkap": "Administrator",
    "role": "bendahara"
  }
}
```

### B. Dashboard & Statistik
- **Endpoint:** `GET /api/dashboard`
- **Response JSON:**
```json
{
  "success": true,
  "data": {
    "total_kas": 1500000,
    "pengeluaran_kas": 250000,
    "total_iuran_lain": 800000,
    "pengeluaran_lain": 100000,
    "total_anggota": 45,
    "anggota_aktif": 40
  }
}
```

### C. Kelola Anggota
- **Endpoint:** `GET /api/anggota`
- **Endpoint:** `POST /api/anggota` (Create), `PUT /api/anggota` (Update), `DELETE /api/anggota?id={id_anggota}`
- **Response JSON (GET):**
```json
{
  "success": true,
  "data": [
    {
      "id_anggota": "ANG-12345",
      "nama": "Budi Santoso",
      "status": "Aktif",
      "no_telepon": "08123456789",
      "alamat": "Blok A No 12",
      "tanggal_bergabung": "2024-01-10T10:00:00.000Z"
    }
  ]
}
```

### D. Kelola Kategori (Pos Keuangan)
- **Endpoint:** `GET /api/kategori`
- **Endpoint:** `POST /api/kategori`, `PUT /api/kategori`, `DELETE /api/kategori?id={id_kategori}`
- **Response JSON (GET):**
```json
{
  "success": true,
  "data": [
    {
      "id_kategori": "KAT-KAS-UTAMA",
      "nama_kategori": "Kas Utama RT 04",
      "is_kas_utama": true,
      "deskripsi": "Iuran bulanan wajib",
      "target_nominal": 20000
    }
  ]
}
```
*(Catatan Backend: DELETE pada kategori Kas Utama akan ditolak (400 Bad Request). Menghapus kategori lain akan memicu Cascade Delete pada transaksi yang berelasi).*

### E. Transaksi Kas Utama
- **Endpoint:** `GET /api/transaksi-kas` (Mendukung query `?periode_bulan=YYYY-MM`)
- **Endpoint:** `POST /api/transaksi-kas` (Simpan transaksi)
- **Payload (POST) / Response (GET):**
```json
{
  "id_transaksi": "TRX-KAS-123",
  "id_anggota": "ANG-12345",
  "periode_bulan": "2024-08",
  "tanggal": "2024-08-15T08:00:00.000Z",
  "jumlah": 20000,
  "jenis": "masuk",
  "keterangan": "Lunas Agustus"
}
```

### F. Transaksi Iuran Lain / Pengeluaran
- **Endpoint:** `GET /api/transaksi-lain`
- **Endpoint:** `POST /api/transaksi-lain`
- **Payload (POST):**
```json
{
  "id_kategori": "KAT-123",
  "id_anggota": "ANG-123", 
  "tanggal": "2024-08-15T09:00:00.000Z",
  "jumlah": 50000,
  "jenis": "keluar",
  "keterangan": "Beli Perlengkapan Rapat"
}
```

---

## 2. 🚀 Detail Fitur Utama (Requirements)
Aplikasi Android harus memiliki fitur berikut:

1. **Autentikasi (Login):**
   - Layar login sederhana dengan field Username dan Password.
   - Menyimpan *state* otentikasi (Token/Info Admin) di `DataStore` atau `SharedPreferences`.
   - Mengarahkan ke Dashboard jika berhasil.

2. **Dashboard & Summary:** 
   - Card Hero banner menampilkan Total Akumulasi Saldo Bersih.
   - 4 Card Indikator (Kas Masuk, Iuran Lain, Pengeluaran Kas, Pengeluaran Lain).
   - Daftar 12 Transaksi Terakhir (gabungan Kas dan Lainnya).

3. **Tab Kas Utama:** 
   - Filter transaksi berdasarkan bulan.
   - Status anggota yang sudah lunas (badge hijau) dan belum (badge amber).

4. **Tab Kategori / Iuran Lain:**
   - Menampilkan Grid kategori.
   - Modal peringatan (Konfirmasi) sebelum menghapus kategori, dengan peringatan "*Cascade Delete*".

5. **Tab Anggota:**
   - CRUD data warga/remaja. Bisa dihubungi via intent WhatsApp jika `no_telepon` tersedia.

6. **Tab Rekapitulasi (Laporan):**
   - **Mode Laporan Pembayaran Kas:** Menampilkan rekapitulasi siapa saja yang sudah lunas dan belum lunas berdasarkan bulan (agregasi client-side dari data Kas dan Anggota).
   - **Mode Buku Kas (Arus Kas):** Menampilkan daftar pemasukan dan pengeluaran secara kronologis.
   - (Opsional) Fitur salin teks (Copy to Clipboard) atau Bagikan ke WhatsApp berisi format laporan text.


---

## 3. 🎨 Detail Desain (RT04 Color System & UI/UX)

Gunakan **Jetpack Compose Material 3** dengan panduan identitas visual berikut:

### Colors (Light Theme)
- **Primary (Brand):** `Color(0xFF155EEF)` (Royal Blue)
- **Primary Dark:** `Color(0xFF1239B8)` (Deep Blue - untuk Gradient/Hero)
- **Accent/Highlight:** `Color(0xFF22D3EE)` (Cyan)
- **Background:** `Color(0xFFF8FAFC)` (Slate 50)
- **Surface (Card):** `Color(0xFFFFFFFF)` (White)

### Semantic Colors
- **Success (Lunas/Masuk):** `Color(0xFF10B981)` (Emerald)
- **Warning (Belum Lunas):** `Color(0xFFF59E0B)` (Amber)
- **Danger (Keluar/Hapus):** `Color(0xFFE11D48)` (Rose)

### Layout & Shape Rules
1. **Corner Radius:**
   - Tombol Standard & Chip: `10dp` (Small) hingga `999dp` (Pill)
   - Kartu Indikator / Kategori: `14dp` hingga `20dp` (Medium - Large)
   - Dashboard Hero Card: `28dp` (Extra Large)
2. **Dashboard Hero Styling:**
   - Wajib menggunakan `Brush.linearGradient` diagonal dari `0xFF155EEF` -> `0xFF1239B8` -> `0xFF312E81`.
   - Berikan efek shadow atau glow (Elevation yang diwarnai biru jika memungkinkan).
3. **Tipografi & Spacing:**
   - Hindari text warna abu-abu pada background warna (Gunakan White/Off-white untuk kontras).
   - Gunakan padding yang lega (minimal `16dp` padding container utama).
   - Terapkan gaya modern, hindari border tebal dan drop-shadow kaku (gunakan shadow tipis dan lembut).
4. **State Handling:**
   - Selalu tampilkan animasi loading (Shimmer atau CircularProgressIndicator) saat *fetching* dari endpoint.
   - Jangan tampilkan "Mock Data" jika API gagal, tampilkan Snackbar "Koneksi Bermasalah".
