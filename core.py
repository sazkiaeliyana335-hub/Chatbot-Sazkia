# -- coding: utf-8 --
from fuzzywuzzy import fuzz

def get_bot_reply(text: str) -> str:
    text = text.lower().strip()

    keywords = {
        "jam": ["jam", "buka", "operasional", "open", "tutup"],
        "alamat": ["alamat", "lokasi", "tempat", "dimana", "di mana"],
        "order": ["order", "pesan", "cetak", "print", "booking"],
        "produk": ["produk", "layanan", "jasa", "apa saja"]
    }

    def match(key):
        return any(fuzz.partial_ratio(text, k) > 75 for k in keywords[key])

    if match("jam"):
        return (
            "🕘 *Jam Operasional*\n"
            "Senin – Sabtu\n"
            "08.00 – 20.00 WIB"
        )

    elif match("alamat"):
        return (
            "📍 *Alamat Toko*\n"
            "Sazkia Printing\n"
            "Jl. Melati desa Kramat"
        )

    elif match("order"):
        return (
            "📝 *Cara Order*\n"
            "1️⃣ Kirim desain\n"
            "2️⃣ Pilih ukuran & bahan\n"
            "3️⃣ Konfirmasi harga\n"
            "4️⃣ Produksi"
        )

    elif match("produk"):
        return (
            "🖨️ *Produk & Layanan*\n"
            "• Banner\n"
            "• Brosur\n"
            "• Undangan\n"
            "• Stiker\n"
            "• Cetak Foto"
        )

    else:
        return (
            "😊 Maaf, saya belum paham.\n\n"
            "Silakan tanya tentang:\n"
            "• Jam operasional\n"
            "• Alamat toko\n"
            "• Cara order\n"
            "• Produk yang tersedia"
        )
