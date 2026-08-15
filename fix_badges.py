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

    # Find the Lunas tags:
    # <span className="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-bold bg-slate-100 text-slate-800 dark:bg-slate-800/60 dark:text-slate-300">
    #                             <CheckCircle className="w-3.5 h-3.5" /> Lunas
    content = re.sub(
        r'bg-slate-100 text-slate-800 dark:bg-slate-800/60 dark:text-slate-300">\s*<CheckCircle className="w-3.5 h-3.5" /> Lunas',
        r'bg-emerald-50 text-emerald-700 dark:bg-emerald-950/60 dark:text-emerald-300">\n                            <CheckCircle className="w-3.5 h-3.5 text-emerald-600 dark:text-emerald-400" /> Lunas',
        content
    )
    content = re.sub(
        r'bg-slate-100 text-slate-800 dark:bg-slate-800/60 dark:text-slate-300">\s*<Check className="w-3 h-3" /> Lunas',
        r'bg-emerald-50 text-emerald-700 dark:bg-emerald-950/60 dark:text-emerald-300">\n                          <Check className="w-3 h-3 text-emerald-600 dark:text-emerald-400" /> Lunas',
        content
    )
    # CheckCircle2 in Rekap
    content = re.sub(
        r'bg-slate-100 text-slate-800 dark:bg-slate-800/60 dark:text-slate-300">\s*<CheckCircle2 className="w-3 h-3" /> Lunas',
        r'bg-emerald-50 text-emerald-700 dark:bg-emerald-950/60 dark:text-emerald-300">\n                          <CheckCircle2 className="w-3 h-3 text-emerald-600 dark:text-emerald-400" /> Lunas',
        content
    )
    content = re.sub(
        r'bg-slate-100 text-slate-800 dark:bg-slate-800/60 dark:text-slate-300">\s*<CheckCircle2 className="w-3.5 h-3.5" /> Lunas',
        r'bg-emerald-50 text-emerald-700 dark:bg-emerald-950/60 dark:text-emerald-300">\n                            <CheckCircle2 className="w-3.5 h-3.5 text-emerald-600 dark:text-emerald-400" /> Lunas',
        content
    )

    # Belum Lunas tags
    content = re.sub(
        r'bg-slate-100 text-slate-800 dark:bg-slate-800/60 dark:text-slate-300">\s*<XCircle className="w-3.5 h-3.5" /> Belum Lunas',
        r'bg-amber-50 text-amber-700 dark:bg-amber-950/60 dark:text-amber-300">\n                            <XCircle className="w-3.5 h-3.5 text-amber-600 dark:text-amber-400" /> Belum Lunas',
        content
    )
    content = re.sub(
        r'bg-slate-100 text-slate-800 dark:bg-slate-800/60 dark:text-slate-300">\s*<XCircle className="w-3 h-3" /> Belum Lunas',
        r'bg-amber-50 text-amber-700 dark:bg-amber-950/60 dark:text-amber-300">\n                          <XCircle className="w-3 h-3 text-amber-600 dark:text-amber-400" /> Belum Lunas',
        content
    )
    
    # KategoriDetailView Sudah Bayar / Belum Bayar
    content = re.sub(
        r'bg-slate-100 text-slate-800 dark:bg-slate-800/60 dark:text-slate-300">\s*<CheckCircle className="w-3(\.5)? h-3(\.5)?" /> Sudah Bayar',
        r'bg-emerald-50 text-emerald-700 dark:bg-emerald-950/60 dark:text-emerald-300">\n                          <CheckCircle className="w-3\1 h-3\2 text-emerald-600 dark:text-emerald-400" /> Sudah Bayar',
        content
    )
    content = re.sub(
        r'bg-slate-100 text-slate-800 dark:bg-slate-800/60 dark:text-slate-300">\s*<XCircle className="w-3(\.5)? h-3(\.5)?" /> Belum Bayar',
        r'bg-amber-50 text-amber-700 dark:bg-amber-950/60 dark:text-amber-300">\n                          <XCircle className="w-3\1 h-3\2 text-amber-600 dark:text-amber-400" /> Belum Bayar',
        content
    )

    with open(path, 'w') as f:
        f.write(content)

