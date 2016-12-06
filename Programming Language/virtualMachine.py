import sys

cont = 0
cuadruplos = None
mapa = None
dictVirtualDirs = None
stackDeEjecucion = []
funcsMemorySpace = []
tableObjects = []
tablaProcedimientos = None
tablaVariables = None
paramDirsFunc = ""

def virtualMachine(cuads, mapaMemoria, dictVirtual, tablaProc, tablaVars):
    print("==========MAQUINA VIRTUAL==========")
    global cuadruplos, mapa, cont, dictVirtualDirs, tablaProcedimientos, tablaVariables
    dictVirtualDirs = dictVirtual
    cuadruplos = cuads
    mapa = mapaMemoria
    tablaProcedimientos = tablaProc
    tablaVariables = tablaVars
    
    while len(cuadruplos) > cont:
        switch = {
            0 : suma,
            1 : resta,
            2 : multiplicacion,
            3 : division,
            4 : residuo,
            5 : andOperation,
            6 : orOperation,
            7 : lessthan,
            8 : greaterthan,
            9 : equal,
            10 : notequal,
            11 : greaterEqual,
            12 : lessEqual,
            13 : asignacion,
            'leer' : leer,
            'imprimir' :imprimir,
            'imprimirSalto' : imprimirSalto,
            'goto' : goto,
            'gotoF' : gotoF,
            'gosub' : gosub,
            'param' : param,
            'era' : era,
            'retornoValor' : retornoValor,
            'retornoLinea' : retornoLinea,
            'asignRetFuncValue' : asignRetFuncValue,
            'verificaBounds' : verificaBounds,
        }
        switch[cuadruplos[cont][0]]()
        cont = cont + 1
    print ("Funciono")
    print (mapa.hashMM)

#0
def suma():
    global mapa
    fstOperando = str(cuadruplos[cont][1])
    sndOperando = str(cuadruplos[cont][2])

    if fstOperando.endswith("$"):
        fstOperando = mapa.hashMM[int(fstOperando[:len(fstOperando)-1])]
    else:
        fstOperando = int(fstOperando)

    if sndOperando.endswith("$"):
        sndOperando = mapa.hashMM[int(sndOperando[:len(sndOperando)-1])]
    else:
        sndOperando = int(sndOperando)

    mapa.hashMM[cuadruplos[cont][3]] = mapa.hashMM[fstOperando] + mapa.hashMM[sndOperando]

#1
def resta():
    global mapa
    fstOperando = str(cuadruplos[cont][1])
    sndOperando = str(cuadruplos[cont][2])

    if fstOperando.endswith("$"):
        fstOperando = mapa.hashMM[int(fstOperando[:len(fstOperando)-1])]
    else:
        fstOperando = int(fstOperando)

    if sndOperando.endswith("$"):
        sndOperando = mapa.hashMM[int(sndOperando[:len(sndOperando)-1])]
    else:
        sndOperando = int(sndOperando)

    mapa.hashMM[cuadruplos[cont][3]] = mapa.hashMM[fstOperando] - mapa.hashMM[sndOperando]

#2
def multiplicacion():
    global mapa
    fstOperando = str(cuadruplos[cont][1])
    sndOperando = str(cuadruplos[cont][2])

    if fstOperando.endswith("$"):
        fstOperando = mapa.hashMM[int(fstOperando[:len(fstOperando)-1])]
    else:
        fstOperando = int(fstOperando)

    if sndOperando.endswith("$"):
        sndOperando = mapa.hashMM[int(sndOperando[:len(sndOperando)-1])]
    else:
        sndOperando = int(sndOperando)

    mapa.hashMM[cuadruplos[cont][3]] = mapa.hashMM[fstOperando] * mapa.hashMM[sndOperando]

#3
def division():
    global mapa
    fstOperando = str(cuadruplos[cont][1])
    sndOperando = str(cuadruplos[cont][2])

    if fstOperando.endswith("$"):
        fstOperando = mapa.hashMM[int(fstOperando[:len(fstOperando)-1])]
    else:
        fstOperando = int(fstOperando)

    if sndOperando.endswith("$"):
        sndOperando = mapa.hashMM[int(sndOperando[:len(sndOperando)-1])]
    else:
        sndOperando = int(sndOperando)

    mapa.hashMM[cuadruplos[cont][3]] = mapa.hashMM[fstOperando] / mapa.hashMM[sndOperando]


#4
def residuo():
    global mapa
    fstOperando = str(cuadruplos[cont][1])
    sndOperando = str(cuadruplos[cont][2])

    if fstOperando.endswith("$"):
        fstOperando = mapa.hashMM[int(fstOperando[:len(fstOperando)-1])]
    else:
        fstOperando = int(fstOperando)

    if sndOperando.endswith("$"):
        sndOperando = mapa.hashMM[int(sndOperando[:len(sndOperando)-1])]
    else:
        sndOperando = int(sndOperando)

    mapa.hashMM[cuadruplos[cont][3]] = mapa.hashMM[fstOperando] % mapa.hashMM[sndOperando]

#5
def andOperation():
    global mapa
    fstOperando = str(cuadruplos[cont][1])
    sndOperando = str(cuadruplos[cont][2])

    if fstOperando.endswith("$"):
        fstOperando = mapa.hashMM[int(fstOperando[:len(fstOperando)-1])]
    else:
        fstOperando = int(fstOperando)

    if sndOperando.endswith("$"):
        sndOperando = mapa.hashMM[int(sndOperando[:len(sndOperando)-1])]
    else:
        sndOperando = int(sndOperando)

    num1 = mapa.hashMM[fstOperando]
    num2 = mapa.hashMM[sndOperando]

    if num1 and num2:
        mapa.hashMM[cuadruplos[cont][3]] = "verdadero"
    else:
        mapa.hashMM[cuadruplos[cont][3]] = "falso"

#6
def orOperation():
    global mapa
    fstOperando = str(cuadruplos[cont][1])
    sndOperando = str(cuadruplos[cont][2])

    if fstOperando.endswith("$"):
        fstOperando = mapa.hashMM[int(fstOperando[:len(fstOperando)-1])]
    else:
        fstOperando = int(fstOperando)

    if sndOperando.endswith("$"):
        sndOperando = mapa.hashMM[int(sndOperando[:len(sndOperando)-1])]
    else:
        sndOperando = int(sndOperando)

    num1 = mapa.hashMM[fstOperando]
    num2 = mapa.hashMM[sndOperando]

    if num1 or num2:
        mapa.hashMM[cuadruplos[cont][3]] = "verdadero"
    else:
        mapa.hashMM[cuadruplos[cont][3]] = "falso"

#7
def lessthan():
    global mapa
    fstOperando = str(cuadruplos[cont][1])
    sndOperando = str(cuadruplos[cont][2])

    if fstOperando.endswith("$"):
        fstOperando = mapa.hashMM[int(fstOperando[:len(fstOperando)-1])]
    else:
        fstOperando = int(fstOperando)

    if sndOperando.endswith("$"):
        sndOperando = mapa.hashMM[int(sndOperando[:len(sndOperando)-1])]
    else:
        sndOperando = int(sndOperando)

    num1 = mapa.hashMM[fstOperando]
    num2 = mapa.hashMM[sndOperando]

    if num1 < num2:
        mapa.hashMM[cuadruplos[cont][3]] = "verdadero"
    else:
        mapa.hashMM[cuadruplos[cont][3]] = "falso"

#8
def greaterthan():
    global mapa
    fstOperando = str(cuadruplos[cont][1])
    sndOperando = str(cuadruplos[cont][2])

    if fstOperando.endswith("$"):
        fstOperando = mapa.hashMM[int(fstOperando[:len(fstOperando)-1])]
    else:
        fstOperando = int(fstOperando)

    if sndOperando.endswith("$"):
        sndOperando = mapa.hashMM[int(sndOperando[:len(sndOperando)-1])]
    else:
        sndOperando = int(sndOperando)

    num1 = mapa.hashMM[fstOperando]
    num2 = mapa.hashMM[sndOperando]

    if num1 > num2:
        mapa.hashMM[cuadruplos[cont][3]] = "verdadero"
    else:
        mapa.hashMM[cuadruplos[cont][3]] = "falso"

#9
def equal():
    global mapa
    fstOperando = str(cuadruplos[cont][1])
    sndOperando = str(cuadruplos[cont][2])

    if fstOperando.endswith("$"):
        fstOperando = mapa.hashMM[int(fstOperando[:len(fstOperando)-1])]
    else:
        fstOperando = int(fstOperando)

    if sndOperando.endswith("$"):
        sndOperando = mapa.hashMM[int(sndOperando[:len(sndOperando)-1])]
    else:
        sndOperando = int(sndOperando)

    num1 = mapa.hashMM[fstOperando]
    num2 = mapa.hashMM[sndOperando]

    if num1 == num2:
        mapa.hashMM[cuadruplos[cont][3]] = "verdadero"
    else:
        mapa.hashMM[cuadruplos[cont][3]] = "falso"

#10
def notequal():
    global mapa
    fstOperando = str(cuadruplos[cont][1])
    sndOperando = str(cuadruplos[cont][2])

    if fstOperando.endswith("$"):
        fstOperando = mapa.hashMM[int(fstOperando[:len(fstOperando)-1])]
    else:
        fstOperando = int(fstOperando)

    if sndOperando.endswith("$"):
        sndOperando = mapa.hashMM[int(sndOperando[:len(sndOperando)-1])]
    else:
        sndOperando = int(sndOperando)

    num1 = mapa.hashMM[fstOperando]
    num2 = mapa.hashMM[sndOperando]

    if num1 != num2:
        mapa.hashMM[cuadruplos[cont][3]] = "verdadero"
    else:
        mapa.hashMM[cuadruplos[cont][3]] = "falso"

#11
def greaterEqual():
    global mapa
    fstOperando = str(cuadruplos[cont][1])
    sndOperando = str(cuadruplos[cont][2])

    if fstOperando.endswith("$"):
        fstOperando = mapa.hashMM[int(fstOperando[:len(fstOperando)-1])]
    else:
        fstOperando = int(fstOperando)

    if sndOperando.endswith("$"):
        sndOperando = mapa.hashMM[int(sndOperando[:len(sndOperando)-1])]
    else:
        sndOperando = int(sndOperando)

    num1 = mapa.hashMM[fstOperando]
    num2 = mapa.hashMM[sndOperando]

    if num1 >= num2:
        mapa.hashMM[cuadruplos[cont][3]] = "verdadero"
    else:
        mapa.hashMM[cuadruplos[cont][3]] = "falso"

#12
def lessEqual():
    global mapa
    fstOperando = str(cuadruplos[cont][1])
    sndOperando = str(cuadruplos[cont][2])

    if fstOperando.endswith("$"):
        fstOperando = mapa.hashMM[int(fstOperando[:len(fstOperando)-1])]
    else:
        fstOperando = int(fstOperando)

    if sndOperando.endswith("$"):
        sndOperando = mapa.hashMM[int(sndOperando[:len(sndOperando)-1])]
    else:
        sndOperando = int(sndOperando)

    num1 = mapa.hashMM[fstOperando]
    num2 = mapa.hashMM[sndOperando]

    if num1 <= num2:
        mapa.hashMM[cuadruplos[cont][3]] = "verdadero"
    else:
        mapa.hashMM[cuadruplos[cont][3]] = "falso"

#13
def asignacion():
    global mapa
    if cuadruplos[cont][2] == 1:
        mapa.hashMM[mapa.hashMM[cuadruplos[cont][3]]] = mapa.hashMM[cuadruplos[cont][1]]
    else:
        mapa.hashMM[cuadruplos[cont][3]] = mapa.hashMM[cuadruplos[cont][1]]

#14
def leer():
    pass

#15
def imprimir():
    global mapa, tableObjects
    value = str(cuadruplos[cont][3])

    if value.endswith('#'):
        localDict = tableObjects[len(tableObjects)-1]
        value = value[:len(value)-1]
        value = value.split('_')
        value = localDict[value[1]]
    elif value.endswith("$"):
        value = mapa.hashMM[int(value[:len(value)-1])]
    else:
        value = int(value)

    print(mapa.hashMM[value],end="")


def imprimirSalto():
    global mapa, tableObjects
    value = str(cuadruplos[cont][3])

    if value.endswith('#'):
        localDict = tableObjects[len(tableObjects)-1]
        value = value[:len(value)-1]
        value = value.split('_')
        value = localDict[value[1]][0]
    elif value.endswith("$"):
        value = mapa.hashMM[int(value[:len(value)-1])]
    else:
        value = int(value)

    print(mapa.hashMM[value])


#16
def gotoF():
    global cont
    if mapa.hashMM[cuadruplos[cont][1]] == "falso":
        cont = cuadruplos[cont][3]
        cont = cont - 1

#17
def goto():
    global cont
    cont = cuadruplos[cont][3]
    cont  = cont - 1


#19
def gosub():
    global cont, stackDeEjecucion, mapa, tableObjects
    stackDeEjecucion.append(cont)

    if cuadruplos[cont][2] != "":
        for i in tablaVariables:
            if i[0] == cuadruplos[cont][2] and i[1] == cuadruplos[cont][3]:
                tableObjects.append(i[3])
                break

    cont = cuadruplos[cont][1]
    cont = cont - 1
    # estado actual


#20
def param():
    global mapa
    paraNum = cuadruplos[cont][3]
    paraNum = int(paraNum[5:]) - 1
    mapa.hashMM[paramDirsFunc[paraNum]] = mapa.hashMM[cuadruplos[cont][1]]

#21
def era():
    global paramDirsFunc, funcsMemorySpace
    for i in tablaProcedimientos:
        if i[0] == cuadruplos[cont][1] and i[1] == cuadruplos[cont][3]:
            paramDirsFunc = i[5]

    currentScope = cuadruplos[cont][2]
    localDict = {}
    for i in tablaVariables:
        if i[2] == currentScope and i[2] != "programa":
            localDict[i[3]] = mapa.hashMM[i[3]]

    if len(localDict) > 0:
        funcsMemorySpace.append(localDict)

#22
def retornoValor():
    global mapa, cont, stackDeEjecucion, funcsMemorySpace

    afterFuncCuadCont = stackDeEjecucion[len(stackDeEjecucion)-1] + 1
    asignDir = cuadruplos[afterFuncCuadCont][1]
    mapa.hashMM[asignDir] =  mapa.hashMM[cuadruplos[cont][1]]

    if len(funcsMemorySpace) > 0:
        lastState = funcsMemorySpace.pop()
        for key, value in list(lastState.items()):
            mapa.hashMM[key] = value

    cont = stackDeEjecucion.pop()
    # sacar

#23
def retornoLinea():
    global stackDeEjecucion, cont
    cont = stackDeEjecucion.pop()


#24
def asignRetFuncValue():
    pass

def verificaBounds():
    global mapa, cont, cuadruplos
    limSup = cuadruplos[cont][3]
    indice = mapa.hashMM[cuadruplos[cont][1]]
    if indice < 0 or indice >= limSup:
        print("Indice fuera de rango")
        sys.exit()
