import os
import re

files_to_check = [
    'src/components/KasView.tsx',
    'src/components/RekapView.tsx',
    'src/components/KategoriDetailView.tsx',
    'src/components/MultiSelectKasModal.tsx',
    'src/components/AnggotaView.tsx'
]

def replace_semantic(content):
    # Lunas / Kas Masuk / Success -> Emerald
    # Pengeluaran / Danger -> Rose
    # Belum Lunas / Warning -> Amber

    # Revert specific patterns I know I broke in my previous script
    # e.g., 'text-slate-700 dark:text-slate-300' where it should be emerald
    # Actually, it's easier to just use regex to target the logic
    
    # In KasView.tsx:
    # <CheckCircle className="w-4 h-4 text-slate-500
    content = content.replace('text-slate-500 ml-auto hidden sm:block', 'text-emerald-500 ml-auto hidden sm:block')
    content = content.replace('<CheckCircle className="w-4 h-4 text-slate-500"', '<CheckCircle className="w-4 h-4 text-emerald-500"')
    content = content.replace('<Clock className="w-4 h-4 text-slate-500 ml-auto hidden sm:block" />', '<Clock className="w-4 h-4 text-amber-500 ml-auto hidden sm:block" />')
    
    # Revert text colors
    content = content.replace('text-slate-600 dark:text-emerald-400', 'text-emerald-600 dark:text-emerald-400')
    content = content.replace("? 'bg-slate-800 text-white shadow-sm'", "? 'bg-emerald-500 text-white shadow-sm'")
    content = content.replace("? 'bg-blue-600 text-white shadow-sm'\n                    : 'text-slate-500 hover:text-slate-700 dark:hover:text-slate-300'", "? 'bg-emerald-500 text-white shadow-sm'\n                    : 'text-slate-500 hover:text-emerald-600 dark:hover:text-emerald-400'")
    content = content.replace("? 'bg-slate-800 text-white shadow-sm'\n                    : 'text-slate-500 hover:text-slate-700 dark:hover:text-slate-300'", "? 'bg-amber-500 text-white shadow-sm'\n                    : 'text-slate-500 hover:text-amber-600 dark:hover:text-amber-400'")

    # Let's just be specific with regex for known strings
    content = re.sub(r'bg-slate-100 text-slate-800 dark:bg-slate-800/60 dark:text-slate-300">\s*<CheckCircle', 'bg-emerald-50 text-emerald-700 dark:bg-emerald-950/60 dark:text-emerald-300">\n                          <CheckCircle className="w-3 h-3 text-emerald-600" />', content)
    
    return content

for path in files_to_check:
    if not os.path.exists(path): continue
    with open(path, 'r') as f:
        content = f.read()
    
    # Simple direct replacements for the badges based on standard strings used before
    
    # Lunas badge
    content = re.sub(
        r'<span className="inline-flex items-center gap-1 px-2(\.5)? py-0\.5 rounded-(full|md) text-\[10px\] font-bold bg-slate-100 text-slate-800 dark:bg-slate-800(/60)? dark:text-slate-300">(\s*)<CheckCircle className="w-3(\.5)? h-3(\.5)?" />',
        r'<span className="inline-flex items-center gap-1 px-2\1 py-0.5 rounded-\2 text-[10px] font-bold bg-emerald-50 text-emerald-700 dark:bg-emerald-950/60 dark:text-emerald-300">\4<CheckCircle className="w-3\5 h-3\6 text-emerald-600" />',
        content
    )
    # Belum badge
    content = re.sub(
        r'<span className="inline-flex items-center gap-1 px-2(\.5)? py-0\.5 rounded-(full|md) text-\[10px\] font-bold bg-slate-100 text-slate-800 dark:bg-slate-800(/60)? dark:text-slate-300">(\s*)<(Clock|XCircle) className="w-3(\.5)? h-3(\.5)?" />',
        r'<span className="inline-flex items-center gap-1 px-2\1 py-0.5 rounded-\2 text-[10px] font-bold bg-amber-50 text-amber-700 dark:bg-amber-950/60 dark:text-amber-300">\4<\5 className="w-3\6 h-3\7 text-amber-600" />',
        content
    )
    
    # Pemasukan text
    content = content.replace("tx.jenis === 'masuk' ? 'text-slate-700 dark:text-slate-300' : 'text-slate-700 dark:text-slate-300'", "tx.jenis === 'masuk' ? 'text-emerald-600 dark:text-emerald-400' : 'text-rose-600 dark:text-rose-400'")

    with open(path, 'w') as f:
        f.write(content)
