class Kosmetik(object):
    nama_produk = None

    def __init__(self, nama_produk):
        self.nama_produk = nama_produk

    def aplikasi(self):
        print('{} siap untuk digunakan di wajah atau kulit.'.format(self.nama_produk))

    def deskripsi(self):
        print('{} adalah produk perawatan yang diformulasikan untuk menjaga kesehatan kulit.'.format(self.nama_produk))

    def simpan(self):
        print('{} sebaiknya disimpan di tempat sejuk dan terhindar dari sinar matahari langsung.'.format(self.nama_produk))


class Skincare(Kosmetik):
    nama_produk = None

    def __init__(self, nama_produk):
        self.nama_produk = nama_produk

    def aplikasi(self):
        print('{} diaplikasikan secara merata untuk hasil yang maksimal.'.format(self.nama_produk))

    def gunakan(self):
        print('Gunakan {} setiap hari untuk hasil yang optimal'.format(self.nama_produk))


# Objek pertama
Serum = Skincare('Serum Skin1004')
Serum.deskripsi()
Serum.aplikasi()
Serum.gunakan()
Serum.simpan()

print()

# Objek kedua
Moisturizer = Skincare('Finally Found You! Soy Brigth!')
Moisturizer.deskripsi()
Moisturizer.aplikasi()
Moisturizer.gunakan()
Moisturizer.simpan()
