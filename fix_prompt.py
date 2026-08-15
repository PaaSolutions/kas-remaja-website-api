import re

with open('ANDROID_PROMPT.md', 'r') as f:
    content = f.read()

# Add Login to Section 1
login_section = """### A. Autentikasi (Login)
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

"""
content = content.replace("### A. Dashboard & Statistik", login_section + "### B. Dashboard & Statistik")
content = content.replace("### B. Kelola", "### C. Kelola")
content = content.replace("### C. Kelola", "### D. Kelola")
content = content.replace("### D. Transaksi", "### E. Transaksi")
content = content.replace("### E. Transaksi", "### F. Transaksi")

# Add Rekap feature and Login to Section 2
feature_updates = """1. **Autentikasi (Login):**
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
"""

content = re.sub(r'1\. \*\*Dashboard & Summary:\*\*(.*)4\. \*\*Tab Anggota:\*\*([^\n]*\n[^\n]*)', feature_updates, content, flags=re.DOTALL)

with open('ANDROID_PROMPT.md', 'w') as f:
    f.write(content)
