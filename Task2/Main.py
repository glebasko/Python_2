import numpy as np
import sympy as sp

# 1. Padalinkite intervalą nuo -1.3 iki 2.5 tolygiai į 64 dalis.

array = np.linspace(start=-1.3, stop=2.6, num=64)
print("Task 1\n")
print(array)

# 2. Sugeneruokite masyvą dydžio 3n ir užpildykite jį cikliniu šablonu [1, 2, 3].

n = 5
array = np.tile([1,2,3], n)

print("\nTask 2\n")
print(array)

# 3. Sukurkite masyvą iš pirmųjų 10 nelyginių sveikųjų skaičių.

array = np.arange(start=1, stop=20, step=2)

print("\nTask 3\n")
print(array)

# 4. Sukurkite masyvą dydžio 10 x 10 iš nulių ir "įrėminkite" jį vienetais.

array = np.zeros([10,10], dtype=int)
array = np.pad(array,1,'constant', constant_values=1)

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
array = np.fromfunction(lambda i, j: i + j, (n, n), dtype=int)
print("\nTask 6\n")
print(array)

# 7. Sukurkite atsitiktinį masyvą dydžio 3×5 naudodami np.random.rand(3, 5) funkciją
#    ir suskaičiuokite: sumą, eilučių sumą, stulpelių sumą.

array = np.random.rand(3,5)

print("\nTask 7\n")
print(array)
print(array.sum()) # suma
print('sum(axis=0): ', np.sum(array, axis=0))
print('sum(axis=1): ', np.sum(array, axis=1))
# 8. Sukurkite atsitiktinį masyvą dydžio 5×5 naudodami np.random.rand(5, 5).
#    Surūšiuokite eilutes pagal antrąjį stulpelį. 
#    Tam pamėginkite apjungti masyvo slicing + argsort + indexing metodus.

array = np.random.rand(5,5)

print("\nTask 8\n")
print(array)
array[:,1] = array[np.argsort(array[:,1])][:,1]
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

array = np.random.rand(5,5)

print("\nTask 10\n")
print(array)

print()
print(np.linalg.eigvals(array))

array = np.linalg.eig(array)
print()
print(array)

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

x = sp.Symbol('x')
a = sp.Symbol('a')
print()
print(sp.integrate(x**2 + x + 1, x))
print(sp.integrate(x + a, x, a))