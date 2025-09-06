import math
from Tarea import *

def joseph(tareas):
    tqPrevio = 0

    sumatoria = 0
    
    print("Tarea actual: 1 --> ",tareas[0])
    print("R1 = C1 = {}\n".format(tareas[0].tiempoEjecucion))

    for tareaActual in range(1, len(tareas)):
        tq = 0
        tqPrevio = 0
        q = 1
        finAlgoritmo = False

        print("Tarea actual: ",tareaActual+1," --> ",tareas[tareaActual])
        print("q = 0 --> ", tq)
        while (not finAlgoritmo):
            for j in range(0, tareaActual):
                sumatoria = sumatoria + (math.ceil(tqPrevio/tareas[j].periodo) * tareas[j].tiempoEjecucion)

            tq = tareas[tareaActual].tiempoEjecucion + sumatoria
            print("q =",q,"--> ", tq)

            if(tq > tareas[tareaActual].vencimiento):
                print("\nSistema no planificable")
                finAlgoritmo = True
            else: 
                if(tq == tqPrevio):
                    print("\nPunto fijo encontrado!")
                    print("R{} = {}\n".format(tareaActual+1,tq))
                    finAlgoritmo = True
                else:
                    tqPrevio = tq
                    
                    q = q+1
                    sumatoria = 0

def ranuraLibrePorJoseph(tareas):
    tareas.append(Tarea(1,1,1))
    tareaActual = len(tareas)-1

    sumatoria = 0
    
    tq = 0
    tqPrevio = 0
    q = 1

    finAlgoritmo = False

    print("Tarea actual: ",tareaActual+1," --> ",tareas[tareaActual])
    print("q = 0 --> ", tq)
    while (not finAlgoritmo):
        for j in range(0, tareaActual):
            sumatoria = sumatoria + (math.ceil(tqPrevio/tareas[j].periodo) * tareas[j].tiempoEjecucion)

        tq = tareas[tareaActual].tiempoEjecucion + sumatoria
        print("q =",q,"--> ", tq)

        if(tq == tqPrevio):
            print("\nRanura libre en [{},{}]\n".format(q-1,q))
            finAlgoritmo = True
        else:
            tqPrevio = tq
            
            q = q+1
            sumatoria = 0