#UG11_C_71210811_SOAL3
def ambil_dan_sisipkan(A1, A2=1, A3=2):

    kalimat = list(A1)
    
    return print(A1 + kalimat[A2 - 1] + kalimat[A3 - 1])


x = input ( " Masukan Kalimat :  ")

y = input ( " Masukan Index 1 :  ")

z = input ( " Masukan Index 2 :  ")

ambil_dan_sisipkan(x, int(y), int(z))