import numpy as np

# 1. Padalinkite intervalą nuo -1.3 iki 2.5 tolygiai į 64 dalis.

array = np.linspace(start=-1.3, stop=2.6, num=64)
print("Task 1\n")
print(array)

# 2. Sugeneruokite masyvą dydžio 3n ir užpildykite jį cikliniu šablonu [1, 2, 3].

n = 5
array = np.array([1,2,3]*n)

print("\nTask 2\n")
print(array)

# 3. Sukurkite masyvą iš pirmųjų 10 nelyginių sveikųjų skaičių.

array = np.arange(start=1, stop=20, step=2)

print("\nTask 3\n")
print(array)

# 4. Sukurkite masyvą dydžio 10 x 10 iš nulių ir "įrėminkite" jį vienetais.

array = np.zeros([10,10], dtype=int)
array[0] = 1
array[9] = 1
array[:,0] = 1
array[:,9] = 1

print("\nTask 4\n")
print(array)


# 5. Sukurkite masyvą dydžio 8 x 8, kur 1 ir 0 išdėlioti šachmatine tvarka (panaudokite slicing+striding metodą).

array = np.zeros((8,8), dtype=int)
array[1::2,::2] = 1
array[::2,1::2] = 1

print("\nTask 5\n")
print(array)

# 6. Sukurkite masyvą dydžio n×n , kurio (i,j)-oji pozicija lygi i+j

n = 6
array = np.zeros((n,n), dtype=int)

i = 0
while i < n:
    y = 0
    while y < n:
        array[i,y] = i+y
        y+=1
    i+=1
    
print("\nTask 6\n")
print(array)

# 7. Sukurkite atsitiktinį masyvą dydžio 3×5 naudodami np.random.rand(3, 5) funkciją
#    ir suskaičiuokite: sumą, eilučių sumą, stulpelių sumą.

array = np.random.rand(3,5)

print("\nTask 7\n")
print(array)
print(array.sum()) # suma
print(array.shape) # stulpelių bei eilučių suma

# 8. Sukurkite atsitiktinį masyvą dydžio 5×5 naudodami np.random.rand(5, 5).
#    Surūšiuokite eilutes pagal antrąjį stulpelį. 
#    Tam pamėginkite apjungti masyvo slicing + argsort + indexing metodus.

array = np.random.rand(5,5)

print("\nTask 8\n")
print(array)
array[:,1] = [(array[i,1]) for i in np.argsort(array[:,1])]

print()
print(array)

# 9. Atvirkštinę matricą

array = np.random.rand(5,5)

print("\nTask 9\n")
print(array)

array = np.linalg.inv(array) # atvirkštinė

print()
print(array)

# 10. Apskaičiuokite matricos tikrines reikšmes ir tikrinį vektorių

# 11. Pasirinktos funkcijos išvestinę

array = np.random.rand(5,5)

print("\nTask 11\n")
print(array)

array = np.gradient(array) # išvestinė

print()
print(array)

# 12. Pasirinktos funkcijos apibrėžtinį ir neapibrėžtinį integralus

array = np.random.rand(5,5)

print("\nTask 12\n")
print(array)

print()
print(np.trapz(array)) # integralas