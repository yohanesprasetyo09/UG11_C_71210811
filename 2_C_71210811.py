#UG11_C_71210811_SOAL2
def check_data_type (a1, a2) :
    a1 = a1.__class__.__name__
    a2 = a2.lower()

    if a1 == a2:
        print("Jawaban Anda benar")
        return True


    print("Jawaban Anda salah, seharusnya adalah: ", a1)
    return False

print(check_data_type(True,"Bool"))
print(check_data_type(True,"bool"))
print(check_data_type({},"TUPLE"))
print(check_data_type({},"DIct"))
print(check_data_type([],""))
