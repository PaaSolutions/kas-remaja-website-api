import re

with open('src/components/KategoriView.tsx', 'r') as f:
    content = f.read()

# Add state
state_code = "  const [selectedDetailKategoriId, setSelectedDetailKategoriId] = useState<string | null>(null);\n  const [kategoriToDelete, setKategoriToDelete] = useState<Kategori | null>(null);"
content = content.replace("  const [selectedDetailKategoriId, setSelectedDetailKategoriId] = useState<string | null>(null);", state_code)

# Replace delete button click handler
old_delete_btn = """                      <button
                        id={`delete-kategori-${kat.id_kategori}-btn`}
                        onClick={() => {
                          if (confirm(`Yakin ingin menghapus kategori "${kat.nama_kategori}"? Seluruh transaksi terkait akan ikut terhapus.`)) {
                            onDeleteKategori(kat.id_kategori);
                          }
                        }}"""
new_delete_btn = """                      <button
                        id={`delete-kategori-${kat.id_kategori}-btn`}
                        onClick={(e) => {
                          e.stopPropagation();
                          setKategoriToDelete(kat);
                        }}"""
content = content.replace(old_delete_btn, new_delete_btn)

# Add Modal
modal_code = """      {/* Delete Confirmation Modal */}
      {kategoriToDelete && (
        <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-slate-900/50 backdrop-blur-sm">
          <div className="bg-white dark:bg-slate-900 w-full max-w-sm rounded-2xl shadow-xl border border-slate-200 dark:border-slate-800 overflow-hidden">
            <div className="p-5">
              <div className="w-10 h-10 rounded-full bg-rose-100 dark:bg-rose-950/50 flex items-center justify-center mb-4 text-rose-600 dark:text-rose-400">
                <Trash2 className="w-5 h-5" />
              </div>
              <h3 className="text-lg font-bold text-slate-900 dark:text-white mb-2">Hapus Kategori?</h3>
              <p className="text-sm text-slate-500 dark:text-slate-400">
                Yakin ingin menghapus kategori <span className="font-semibold text-slate-700 dark:text-slate-300">"{kategoriToDelete.nama_kategori}"</span>?
                Seluruh transaksi terkait akan ikut terhapus dan saldo akan ter-update. Tindakan ini tidak dapat dibatalkan.
              </p>
            </div>
            <div className="flex items-center gap-3 p-4 bg-slate-50 dark:bg-slate-800/50 border-t border-slate-100 dark:border-slate-800">
              <button
                onClick={() => setKategoriToDelete(null)}
                className="flex-1 px-4 py-2 text-sm font-semibold text-slate-600 dark:text-slate-300 hover:bg-slate-200 dark:hover:bg-slate-700 rounded-xl transition-colors cursor-pointer"
              >
                Batal
              </button>
              <button
                onClick={() => {
                  onDeleteKategori(kategoriToDelete.id_kategori);
                  setKategoriToDelete(null);
                }}
                className="flex-1 px-4 py-2 text-sm font-semibold text-white bg-rose-600 hover:bg-rose-700 rounded-xl shadow-sm transition-colors cursor-pointer"
              >
                Ya, Hapus
              </button>
            </div>
          </div>
        </div>
      )}
"""
content = content.replace("    </div>\n  );\n};", modal_code + "    </div>\n  );\n};")

with open('src/components/KategoriView.tsx', 'w') as f:
    f.write(content)

