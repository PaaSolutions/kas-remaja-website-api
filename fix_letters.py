import re

with open('ANDROID_PROMPT.md', 'r') as f:
    content = f.read()

content = content.replace("### D. Kelola Anggota", "### C. Kelola Anggota")
content = content.replace("### F. Transaksi Kas Utama", "### E. Transaksi Kas Utama")

with open('ANDROID_PROMPT.md', 'w') as f:
    f.write(content)
