from collections import Counter


def _ambil_angka(data, batas):
    terakhir = data[-batas:]
    hasil = []
    for item in terakhir:
        nilai = item[1] if isinstance(item, (list, tuple)) else item
        hasil.append(str(nilai).strip().zfill(4))
    return hasil


def analisis_lanjutan(data, batas=50):
    angka_list = _ambil_angka(data, batas)
    if not angka_list:
        return "Belum ada data untuk dianalisis."

    frek = Counter(d for angka in angka_list for d in angka)

    genap = sum(v for d, v in frek.items() if int(d) % 2 == 0)
    ganjil = sum(frek.values()) - genap
    kecil = sum(v for d, v in frek.items() if int(d) <= 4)
    besar = sum(frek.values()) - kecil

    nama_pola = {
        1: "4 angka sama",
        2: "2 angka unik",
        3: "3 angka unik",
        4: "4 angka unik",
    }
    pola = Counter(nama_pola[len(set(a))] for a in angka_list)

    baris = [f"ANALISIS {len(angka_list)} DATA TERAKHIR", "", "FREKUENSI DIGIT"]
    baris += [f"{d} = {frek[d]} kali" for d in "0123456789"]
    baris += [
        "",
        f"GANJIL : {ganjil}",
        f"GENAP  : {genap}",
        "",
        f"KECIL (0-4) : {kecil}",
        f"BESAR (5-9) : {besar}",
        "",
        "KLASIFIKASI POLA",
    ]
    baris += [f"{n}: {j}" for n, j in pola.most_common()]
    baris += [
        "",
        "CATATAN:",
        "Ini statistik historis. Frekuensi tidak menjamin hasil berikutnya.",
    ]
    return "\n".join(baris)


def bandingkan_periode(data, periode=(10, 20, 30, 50)):
    garis = "=" * 25
    return "\n".join(
        f"\n{garis}\n{analisis_lanjutan(data, p)}" for p in periode
  )
