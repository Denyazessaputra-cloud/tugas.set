# daftar kata spam dan disimapan didalam denyset
kata_spam = {"promo", "diskon", "hadiah", "gratis"}

# tampilan awal
print("=== PROGRAM DETEKSI EMAIL SPAM ===")

# input nama email
nama_email = input("Masukkan nama email: ")

# input pesan dari email
pesan = input("Masukkan isi pesan: ")

# tampilkan email
print("Email dari :", nama_email)
print("Isi pesan  :", pesan)

# cek apakah ada kata yang menggandung spam
if "promo" in pesan.lower():
    print("Terdapat kata spam : promo")

if "diskon" in pesan.lower():
    print("Terdapat kata spam : diskon")

if "hadiah" in pesan.lower():
    print("Terdapat kata spam : hadiah")

if "gratis" in pesan.lower():
    print("Terdapat kata spam : gratis")

if (
    "promo" not in pesan.lower()
    and "diskon" not in pesan.lower()
    and "hadiah" not in pesan.lower()
    and "gratis" not in pesan.lower()
):
    print("Pesan bukan spam")
else:
    print("Pesan termasuk SPAM")

print("=== PROGRAM SELESAI ===")