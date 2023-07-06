graf = {'A': ['B','C'],
        'B': ['C','D'],
        'C': ['D'],
        'D': ['C'],
        'E': ['F'],
        'F': ['C']
}
def cari_jalan(graf, awal, akhir, jalur=[]):
    jalur = jalur + [awal]
    if awal == akhir:
        return jalur
    if not awal in graf:
        return[]
    semua_jalur = []
    for titik in graf[awal]:
        if titik not in jalur:
            jalur_jalur = cari_jalan(graf, titik, akhir, jalur)
            for jalur_baru in jalur_jalur:
                semua_jalur.append(jalur_baru)
    return semua_jalur

def counter(data):
    rute = ""
    for y in range(0, len(data)):
        if y < len(data) - 1:
            rute += data[y] + " > "
        else:
            rute += data[y]
    return rute

start = input("Masukan Kota Mulai : ")
Finish = input("Masukan Kota Selesai : ")

data_x = cari_jalan(graf, start, Finish)
print(f"Jumlah Rute : {len(data_x)}")
min = data_x[0]
max = []
for x in data_x:
    if len(x) < len(min):
        min = x
    if len(x) > len(max):
        max = x
print(f"Rute Tercepat : {counter(min)}")
print(f"Rute Terlama : {counter(max)}")
print(f"Daftar Rute Yang Bisa Dilewati : ")

for x in range (0, len(data_x)):
    print(f"RUTE {x+1} : ")
    print(counter(data_x[x]))