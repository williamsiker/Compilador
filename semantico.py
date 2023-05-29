txt = " "
cont = 0


def incrementar_cot():
    global cont
    cont += 1
    return "%d" % cont


class Nodo():
    pass


class Null(Nodo):
    def __init__(self):
        self.type = 'void'

    def imprimir(self, ident):
        print(ident + "nodo nulo")

    def traducir(self):
        global txt
        id = incrementar_cot()
        txt += id + "[label= " + "nodo_nulo" + "]" + "\n\t"

        return id


class block(Nodo):
    def __init__(self, son1, name):
        self.son1 = son1
        self.name = name

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementar_cot()

        son1 = self.son1.traducir()
        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + "->" + son1 + "\n\t"

        return "digraph G {\n\t" + txt + "}"


class statement_list1(Nodo):
    def __init__(self, son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def imprimir(self, ident):
        self.son1.imprimir(" "+ ident)
        self.son2.imprimir(" " + ident)
        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementar_cot()
        son1 = self.son1.traducir()
        son2 = self.son2.traducir()
        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + "->" + son1 + "\n\t"
        txt += id + "->" + son2 + "\n\t"

        return id

class statement_list2(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" "+ident)
        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementar_cot()
        son1 = self.son1.traducir()
        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + "->" + son1 + "\n\t"

        return id


class statement(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementar_cot()

        son1 = self.son1.traducir()
        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + "->" + son1 + "\n\t"

        return id


class crearventana(Nodo):
    def __init__(self, son1, son2, son3, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        self.son2.imprimir(" " + ident)
        self.son3.imprimir(" " + ident)
        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementar_cot()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()
        son3 = self.son3.traducir()
        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + "->" + son1 + "\n\t"
        txt += id + "->" + son2 + "\n\t"
        txt += id + "->" + son3 + "\n\t"

        return id


class crearframe(Nodo):
    def __init__(self, son1, son2, son3, son4, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        self.son2.imprimir(" " + ident)
        self.son3.imprimir(" " + ident)
        self.son4.imprimir(" " + ident)
        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementar_cot()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()
        son3 = self.son3.traducir()
        son4 = self.son4.traducir()
        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + "->" + son1 + "\n\t"
        txt += id + "->" + son2 + "\n\t"
        txt += id + "->" + son3 + "\n\t"
        txt += id + "->" + son4 + "\n\t"

        return id


class crearboton(Nodo):
    def __init__(self, son1, son2, son3, son4, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        self.son2.imprimir(" " + ident)
        self.son3.imprimir(" " + ident)
        self.son4.imprimir(" " + ident)
        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementar_cot()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()
        son3 = self.son3.traducir()
        son4 = self.son4.traducir()
        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + "->" + son1 + "\n\t"
        txt += id + "->" + son2 + "\n\t"
        txt += id + "->" + son3 + "\n\t"
        txt += id + "->" + son4 + "\n\t"

        return id


class crearetiqueta(Nodo):
    def __init__(self, son1, son2, son3, son4, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        self.son2.imprimir(" " + ident)
        self.son3.imprimir(" " + ident)
        self.son4.imprimir(" " + ident)
        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementar_cot()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()
        son3 = self.son3.traducir()
        son4 = self.son4.traducir()
        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + "->" + son1 + "\n\t"
        txt += id + "->" + son2 + "\n\t"
        txt += id + "->" + son3 + "\n\t"
        txt += id + "->" + son4 + "\n\t"

        return id


class iniciar(Nodo):
    def __init__(self, son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        self.son2.imprimir(" " + ident)
        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementar_cot()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()
        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + "->" + son1 + "\n\t"
        txt += id + "->" + son2 + "\n\t"

        return id


class argument_list1(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementar_cot()
        son1 = self.son1.traducir()
        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + "->" + son1 + "\n\t"

        return id

class argument_list2(Nodo):
    def __init__(self, son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        self.son2.imprimir(" " + ident)
        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementar_cot()
        son1 = self.son1.traducir()
        son2 = self.son2.traducir()
        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + "->" + son1 + "\n\t"
        txt += id + "->" + son2 + "\n\t"

        return id


class argument1(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementar_cot()
        son1 = self.son1.traducir()
        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + "->" + son1 + "\n\t"

        return id

class argument2(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementar_cot()
        son1 = self.son1.traducir()
        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + "->" + son1 + "\n\t"

        return id


class error(Nodo):
    def __init__(self, name):
        self.name = name

    def traducir(self):
        global txt
        id = incrementar_cot()

        return id


class Id(Nodo):
    def __init__(self, name):
        self.name = name

    def imprimir(self, ident):
        print(ident + "ID: " + self.name)

    def traducir(self):
        global txt
        id = incrementar_cot()
        txt += id + "[label= " + self.name + "]" + "\n\t"

        return id


class Assign(Nodo):
    def __init__(self, name):
        self.name = name

    def imprimir(self, ident):
        print(ident + "Assign: " + self.name)

    def traducir(self):
        global txt
        id = incrementar_cot()

        txt += id + "[label= \"" + self.name + "\"]" + "\n\t"

        return id


class Ventana(Nodo):
    def __init__(self, name):
        self.name = name

    def imprimir(self, ident):
        print(ident + "Func: " + self.name)

    def traducir(self):
        global txt
        id = incrementar_cot()

        txt += id + "[label= \"" + self.name + "\"]" + "\n\t"

        return id