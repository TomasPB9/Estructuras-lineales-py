from array import ArrayType

#Los métodos que escribimos con doble guion bajo, son precisamente para 
#poder utilizar cosas como:

									#	menu[1]
									#	len(menu)
									#	print(menu)

class Array:
    def __init__(self, capacity, fill_value=None):
        self.items = list()
        for i in range(capacity):
            self.items.append(fill_value)
    
    def __len__(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)

    def __iter__(self):
        return iter(self.items)

    def __getitem__(self, index):
        return self.items[index]

    def __setitem__(self, index, new_item):
        self.items[index] = new_item

menu = Array(5)
print(len(menu))
print()

# ------------------------------- METODOS BUILT-IN EN PYTHON ----------------------------


for i in range(len(menu)):
    menu[i]= i+1

print(menu[0])
print()


for option in menu:
    print(menu[option-1])

# ------------------------------- METODOS CREADOS DEL ARRAY ----------------------------

print()
print("Clases creadas de array")
print(menu.__len__())

print()
print(menu.__str__())

print()
print(menu.__iter__())

print()
print(menu.__getitem__(2))

print()
print(menu.__setitem__(2,100))

print()
print(menu.__getitem__(2))

