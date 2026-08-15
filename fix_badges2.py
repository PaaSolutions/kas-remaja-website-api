import os
import re

files_to_check = [
    'src/components/KasView.tsx',
    'src/components/RekapView.tsx',
    'src/components/KategoriDetailView.tsx',
    'src/components/MultiSelectKasModal.tsx',
    'src/components/AnggotaView.tsx'
]

for path in files_to_check:
    if not os.path.exists(path): continue
    with open(path, 'r') as f:
        content = f.read()

    # Generic fix for Sudah Bayar / Lunas (bg-slate-50 or bg-slate-100) -> emerald
    content = re.sub(
        r'bg-slate-[0-9]+ text-slate-[0-9]+ dark:bg-slate-[0-9]+(/[0-9]+)? dark:text-slate-[0-9]+(\s+border\s+border-slate-[0-9]+\s+dark:border-slate-[0-9]+)?">\s*<CheckCircle[2]? className="w-[0-9\.]+ h-[0-9\.]+( text-slate-[0-9]+)?" /> (Sudah Bayar|Lunas)',
        r'bg-emerald-50 text-emerald-700 dark:bg-emerald-950/60 dark:text-emerald-300">\n                          <CheckCircle className="w-3 h-3 text-emerald-600 dark:text-emerald-400" /> \4',
        content
    )

    # Generic fix for Belum Bayar / Belum Lunas
    content = re.sub(
        r'bg-slate-[0-9]+ text-slate-[0-9]+ dark:bg-slate-[0-9]+(/[0-9]+)? dark:text-slate-[0-9]+(\s+border\s+border-slate-[0-9]+\s+dark:border-slate-[0-9]+)?">\s*<XCircle className="w-[0-9\.]+ h-[0-9\.]+( text-slate-[0-9]+)?" /> (Belum Bayar|Belum Lunas)',
        r'bg-amber-50 text-amber-700 dark:bg-amber-950/60 dark:text-amber-300">\n                          <XCircle className="w-3 h-3 text-amber-600 dark:text-amber-400" /> \4',
        content
    )
    
    # Active tab colors in KasView.tsx and KategoriDetailView.tsx
    # e.g., statusFilter === 'lunas' ? 'bg-emerald-500 ...'
    # Actually, I changed them to `bg-emerald-500` before I ran the `clean_colors.sh` script which replaced `bg-emerald-500` with... wait! `clean_colors.sh` did NOT touch `bg-emerald-500`! It only touched `bg-emerald-50`, `bg-emerald-100`. So `bg-emerald-500` might have been replaced by `clean_colors2.sh` which replaced `bg-emerald-500` with `bg-blue-600`! Yes!
    content = content.replace(
        "statusFilter === 'lunas'\n                  ? 'bg-blue-600 text-white shadow-sm'",
        "statusFilter === 'lunas'\n                  ? 'bg-emerald-600 text-white shadow-sm'"
    )
    content = content.replace(
        "statusFilter === 'belum'\n                  ? 'bg-blue-600 text-white shadow-sm'",
        "statusFilter === 'belum'\n                  ? 'bg-amber-500 text-white shadow-sm'"
    )
    content = content.replace(
        "filterTab === 'sudah'\n                  ? 'bg-blue-600 text-white shadow-xs'",
        "filterTab === 'sudah'\n                  ? 'bg-emerald-600 text-white shadow-xs'"
    )
    content = content.replace(
        "filterTab === 'belum'\n                  ? 'bg-blue-600 text-white shadow-xs'",
        "filterTab === 'belum'\n                  ? 'bg-amber-500 text-white shadow-xs'"
    )

    # In KategoriDetailView, 'text-emerald-600' might have been changed to 'text-slate-700'
    content = content.replace("tx.jenis === 'masuk' ? 'text-slate-700 dark:text-slate-400'", "tx.jenis === 'masuk' ? 'text-emerald-600 dark:text-emerald-400'")
    content = content.replace("tx.jenis === 'keluar' ? 'text-slate-700 dark:text-slate-400'", "tx.jenis === 'keluar' ? 'text-rose-600 dark:text-rose-400'")

    with open(path, 'w') as f:
        f.write(content)

