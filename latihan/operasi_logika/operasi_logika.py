# Soal no 1
print(10*'=','SOAL NO 1',10*'=')
inputUser = int(input('1. A adalah angka yang ingin di input\ndan aturan angka nya adalah: (A > 0 && A < 5) || (A > 8 && A < 11) \n:'))

lebihDari0 = inputUser > 0
kurangDari5 = inputUser < 5

lebihDari8 = inputUser > 8
kurangDari11 = inputUser < 11

print(inputUser, '>' , 0 , '=', lebihDari0)
print(inputUser, '<', 5, '=', kurangDari5)
print(inputUser, '>', 8, '=', lebihDari8)
print(inputUser, '<', 11, '=', kurangDari11)

hasil = (inputUser > 0 and inputUser < 5) or (inputUser > 8 and inputUser < 11)
print('Angka yang kamu masukan:', hasil)

print(10*'=','SOAL NO 2',10*'=')

# Soal no 2
inputUser = int(input('1. A adalah angka yang ingin di input\ndan aturan angka nya adalah: (A < 0 || A > 5) && (A < 8 || A > 11) \n:'))

kurangDari0 = inputUser < 0
lebihDari5 = inputUser > 5
kurangDari8 = inputUser < 8
lebihDari11 = inputUser > 11

print(inputUser, '<' , 0 , '=', kurangDari0)
print(inputUser, '>', 5, '=', lebihDari5)
print(inputUser, '<', 8, '=', kurangDari8)
print(inputUser, '>', 11, '=', lebihDari11)

hasil = (inputUser < 0 or inputUser > 5) and (inputUser < 8 or inputUser > 11)
print('Angka yang kamu masukan:', hasil)