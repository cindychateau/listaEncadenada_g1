class Nodo:
    def __init__(self, nombre, id):
        self.nombre = nombre
        self.id = id
        self.next = None #Aún no pertenece a ninguna lista, por lo tanto NO sé cuál vaya ser en un futuro su nodo siguiente