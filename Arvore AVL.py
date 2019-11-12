class Node():
    def __init__(self,dado):
        self.dados = dado
        self.pai = None
        self.fLeft = None
        self.fRight = None
        self.cor = 1
    def getDado(self):
        return self.dados

class Avl():
    def __init__(self):
        self.objectNull = Node(0)
        self.objectNull.cor = 0
        self.objectNull.fLeft = None
        self.objectNull.fRight = None
        self.raiz = self.objectNull

    def rotateLeft(self,x):
        y = x.fRight
        x.fRight = y.fLeft
        if y.fLeft != self.objectNull:
            y.fLeft.pai = x

        y.pai = x.pai
        if x.pai == None:
            self.raiz = y
        elif x == x.pai.fLeft:
            x.pai.fLeft = y
        else:
            x.pai.fRight = y
        y.fLeft = x
        x.pai = y

    def rotateRight(self,x):
        y = x.fLeft
        x.fLeft = y.fRight
        if y.fRight != self.objectNull:
            y.fRight.pai = x

        y.pai = x.pai
        if x.pai == None:
            self.raiz = y
        elif x == x.pai.fRight:
            x.pai.fRight = y
        else:
            x.pai.fLeft = y
        y.fRight = x
        x.pai = y
    def __hDelete(self,node,key):
        u = self.__tBusca(node,key)
        if u == self.objectNull:
            print("%s nao presente na arvore"%key)
            return

        y = u
        yPrimal = y.cor
        if u.fLeft == self.objectNull:
            x = u.fRight
            self.__hTrocar(u,u.fRight)
        elif u.fRight == self.objectNull:
            x = u.fLeft
            self.__hTrocar(u,u.fLeft)
        else:
            y = self.inMin(u.fRight)
            yPrimal = y.cor
            x = y.fRight
            if y.pai == u:
                x.pai = y
            else:
                self.__hTrocar(y,y.fRight)
                y.fRight = u.fRight
                y.fRight.pai = y

            self.__hTrocar(u,y)
            y.fLeft = u.fLeft
            y.fLeft.pai = y
            y.cor = u.cor
        if yPrimal == 0:
            self.__deleteFix(x)

    def __deleteFix(self, x):
        while x != self.raiz and x.cor == 0:
            if x == x.pai.fLeft:
                s = x.pai.fRight
                if s.cor == 1:
                    s.cor = 0
                    x.pai.cor = 1
                    self.rotateLeft(x.pai)
                    s = x.pai.fRight

                if s.fLeft.cor == 0 and s.fRight.cor == 0:
                    s.cor = 1
                    x = x.pai
                else:
                    if s.fRight.cor == 0:
                        s.fLeft.cor = 0
                        s.cor = 1
                        self.rotateRight(s)
                        s = x.pai.fRight

                    s.cor = x.pai.cor
                    x.pai.cor = 0
                    s.fRight.cor = 0
                    self.rotateLeft(x.pai)
                    x = self.raiz
            else:
                s = x.pai.fLeft
                if s.cor == 1:
                    s.cor = 0
                    x.pai.cor = 1
                    self.rotateRight(x.pai)
                    s = x.pai.fLeft

                if s.fRight.cor == 0 and s.fRight.cor == 0:
                    s.cor = 1
                    x = x.pai
                else:
                    if s.fLeft.cor == 0:
                        s.fRight.cor = 0
                        s.cor = 1
                        self.rotateLeft(s)
                        s = x.pai.fLeft

                    s.cor = x.pai.cor
                    x.pai.cor = 0
                    s.fLeft.cor = 0
                    self.rotateRight(x.pai)
                    s = self.raiz
        x.cor = 0

    def __hTrocar(self,u,v):
        if u.pai == None:
            self.raiz = v
        elif u == u.pai.fLeft:
            u.pai.fLeft = v
        else:
            u.pai.fRight = v
        v.pai = u.pai
    def inMax(self, node):
        while True:
            if node.fLeft == self.objectNull:
                return node
            node = node.fLeft
    def insertFix(self, node):
        while node.pai.cor == 1:
            if node.pai == node.pai.pai.fRight:
                u = node.pai.pai.fLeft
                if u.cor == 1:
                    u.cor = 0
                    node.pai.cor = 0
                    node.pai.pai.cor = 1
                    node = node.pai.pai
                else:
                    if node == node.pai.fLeft:
                        node = node.pai
                        self.rotateRight(node)
                    node.pai.cor = 0
                    node.pai.pai.cor = 1
                    self.rotateLeft(node.pai.pai)
            else:
                u = node.pai.pai.fRight
                if u.cor == 1:
                    u.cor = 0
                    node.pai.cor = 0
                    node.pai.pai.cor = 1
                    node = node.pai.pai
                else:
                    if node == node.pai.fRight:
                        node = node.pai
                    node.pai.cor = 0
                    node.pai.pai.cor = 1
                    self.rotateRight(node.pai.pai)
            if node == self.raiz:
                break
        self.raiz.cor = 0
    def inMin(self, node):
        while True:
            if node.fRight == self.objectNull:
                return node
            node = node.fRight
    def predecessor(self,x):
        if x.fLeft != self.objectNull:
            return self.inMax(x.fLeft)
        y = x.pai
        while y != self.objectNull and x == y.fLeft:
            x = y
            y = y.pai
        return y
    def sucessor(self, x):
        if x.fRight != self.objectNull:
            return self.inMin(x.fRight)
        y = x.pai
        while y != self.objectNull and x == y.fRight:
            x = y
            y = y.pai
    def tInserir(self,key):
        node = Node(key)
        node.pai = None
        node.dados = key
        node.fLeft = self.objectNull
        node.fRight= self.objectNull
        node.cor = 1

        y = None
        x = self.raiz

        while True:
            if x != self.objectNull:
                y = x
                if node.getDado() < x.getDado():
                    x = x.fLeft
                else:
                    x = x.fRight
            else:
                break

        node.pai = y
        if y == None:
            self.raiz = node
        elif node.getDado() < y.getDado():
            y.fLeft = node
        else:
            y.fRight = node

        if node.pai == None:
            node.cor = 0
            return
        if node.pai.pai == None:
            return
        self.insertFix(node)
        print("dado inserido")
    def tGetRaiz(self):
        return self.raiz
    def tDelete(self,dado):
        self.__hDelete(self.raiz, dado)
    def __tBusca(self,node, x):
        if node == self.objectNull or node.getDado() == x:
            return node
        else:
            if node.getDado() > x:
                return self.__tBusca(node.fLeft,x)
            else:
                return self.__tBusca(node.fRight,x)
    def tSearch(self,x):
        return self.__tBusca(self.raiz,x)

    def tPrint(self):
        return self.__hPrint(self.raiz,1)
    def __hPrint(self,node,filho,s=""):
        if node != self.objectNull:
            if node.pai == None:
                lado = "Raiz"
            elif filho:
                lado = "--Right"
            else:
                lado = "--Left"
            print(s,lado,node.getDado())
            s += "   "
            self.__hPrint(node.fLeft,0,s)
            self.__hPrint(node.fRight,1,s)

class Menu():
    def __init__(self,tela=0):
        self.arvore = Avl()
        self.tela = tela
        self.tela0 = """
        \tArvore AVL
\t1- inserir
\t2- deletar
\t3- visualizar
\t4- sair
"""
        self.tela1 = """\t|- inserir -|
    \t# inserir e ,se preciso, balancear a arvore       #
    \t# é possivel inserir varios valores ao mesmo tempo
    \t  colocando um espaço entre cada valor            # 
    input = """
        self.tela2 = """\t|- deletar -|
    \t # deleta e balanceia a arvore #
    input = """

    def menu_mudar(self,menu_t,b=True):
        if b :
            if menu_t == 0:
                print(self.tela0)
                self.menu_mudar(int(input()))
            elif menu_t == 1:
                print(self.tela1,end= "")
                for x in [int(p) for p in input().split(" ")]:
                    print(x)
                    self.arvore.tInserir(x)
                self.menu_mudar(0)
            elif menu_t == 2:
                print(self.tela2,end= "")
                self.arvore.tDelete(int(input()))
                self.menu_mudar(0)
            elif menu_t == 3:
                self.arvore.tPrint()
                a = input("Pressione ENTER para continuar...")
                self.menu_mudar(0)
            else:
                b = False

p = Menu()
p.menu_mudar(0)