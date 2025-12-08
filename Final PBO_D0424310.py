# Final Pemrograman Berorientasi Objek
#(Tema cewek tentang penjualan kosmetik)

# Nama : Waffiq Adkhilniy MR
# Nim : D0424310
# Kelas : Sistem Informasi  A 2024


# Class Product (Encapsulation)

class Product:
    def __init__(self, name, price):
        self.__name = name          # enkapsulasi (private)
        self.__price = price

    # Getter & Setter
    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price

    def show_info(self):
        print(f"Nama Produk : {self.__name}")
        print(f"Harga       : Rp{self.__price}")
        

# Class Cosmetic (Inheritance)

class Cosmetic(Product):
    def __init__(self, name, price, category):
        super().__init__(name, price)  # ambil dari parent class
        self.category = category

    def show_info(self):
        super().show_info()
        print(f"Kategori    : {self.category}")


# Class Lipstick (Polymorphism)

class Lipstick(Cosmetic):
    def __init__(self, name, price, category, color):
        super().__init__(name, price, category)
        self.color = color

    def show_info(self):
        print("--- Detail Lipstick ---")
        super().show_info()
        print(f"Warna       : {self.color}")


# Class Foundation (Polymorphism)

class Foundation(Cosmetic):
    def __init__(self, name, price, category, shade):
        super().__init__(name, price, category)
        self.shade = shade

    def show_info(self):
        print("--- Detail Foundation ---")
        super().show_info()
        print(f"Shade       : {self.shade}")


# Object & Polymorphism (Main Program)

l1 = Lipstick("Matte Velvet", 75000, "Lip Product", "Red Rose")
f1 = Foundation("Soft Matte", 120000, "Face Product", "Natural Beige")

products = [l1, f1]

for p in products:
    p.show_info()
    print()

