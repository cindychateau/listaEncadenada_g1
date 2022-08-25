from Nodo import Nodo
class ListaEncadenada:
    def __init__(self):
        self.head = None #Porque cuando declaro por primera vez mi lista AÚN no tiene ningún nodo, la inicializamos vacía

    #HEAD -> Juana
    #Juana -> Next: Pedro
    #Pedro -> Next: Pablo
    #Pablo -> Next: Elena
    #Elena -> Next: None
    
    #insertaNodo(Juan) ---- aux = es el nodo en el que nos encontramos en ese momento

    #aux = Juana
    #Juana.next = Pedro

    #aux = Pedro
    #Pedro.next = Pablo

    #aux = Pablo
    #Pablo.next = Elena

    #aux = Elena
    #Elena.next = None
    #Elena.next = Juan

    def insertaNodo(self, nuevoNodo):
        if self.head == None: #Mi lista está vacía
            self.head = nuevoNodo #El primer elemento lista es el nodo recibo
        else:
            aux = self.head #el primer nodo a comparar es el head (o el primero de mi lista)
            while aux.next != None: #Siempre y cuando el next de mi nodo NO sea None
                aux = aux.next #aux ahora es el siguiente nodo
            aux.next = nuevoNodo

    
    #Función que me imprima TODA la lista
    #HEAD -> Juana
    #Juana -> Next: Pedro
    #Pedro -> Next: Pablo
    #Pablo -> Next: Elena
    #Elena -> Next: None

    #aux = Juana
    #PRINT Juana

    #aux = Juana.next = Pedro
    #PRINT Pedro

    #aux = Pedro.next = Pablo
    #PRINT Pablo

    #aux = Pablo.next = Elena
    #PRINT Elena

    #aux = Elena.next = None
    def imprimeLista(self):
        aux = self.head #Me toma el primer elemento de la lista
        while aux != None:
            print(aux.nombre)
            aux = aux.next

    #Función que elimine un nodo en base a su ID
    def eliminaNodo(self, id): 
        #Revisar si la lista está vacía
        if self.head == None:
            print("La lista está vacía, no podemos eliminar nodos")
        else:
            aux = self.head
            if aux.id == id:
                #1.- el nuevo head va a ser el next (el que le sigue) de mi head actual
                self.head = aux.next
                aux.next = None #Del nodo que estoy eliminando, el NEXT debe ser None porque lo estamos sacando de la lista
            else:
                #HEAD -> Juana
                #Juana 1 -> Next: Pedro
                #Pedro 2 -> Next: Pablo
                #Pablo 3 -> Next: Elena
                #Elena 4 -> Next: None
                #id = 3
                #aux = Juana
                #prevAux = Juana

                #prevAux = Juana
                #aux = Juana.next = Pedro

                #prevAux = Pedro
                #aux = Pedro.next = Pablo
                #Pedro.next = Elena
                #Pablo.next = None
                prevAux = aux #Comenzamos diciendo que previo es el head
                while aux.next != None:
                    prevAux = aux
                    aux = aux.next
                    #1.- Comparamos si el nodo aux coincide con el ID que tratamos de eliminar
                    if aux.id == id:
                        #2.- El nodo previo, su NEXT va a ser ahora el NEXT del nodo a eliminar
                        prevAux.next = aux.next
                        #3.- El nodo que estoy eliminando, su NEXT debe ser None
                        aux.next = None