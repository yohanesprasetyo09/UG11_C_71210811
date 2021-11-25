#UG11_C_71210811_SOAL1
def nilai(glorius) :
    
    print (" Nilai Tertinggi adalah: ", max (glorius)) 
    print (" Nilai Terendah adalah : ", min (glorius))
    
    rumus = sum(glorius) / len(glorius)
    
    print("Rata-ratanya adalah: ", '{:5.2f}' .format(rumus))
    
    return sorted(glorius)

daftar_nilai1 = [10,40,30,53,50]
daftar_nilai2 = [99,78,89,85,46]
daftar_nilai3 = [57,90,76,85,78]
print(nilai(daftar_nilai1))
