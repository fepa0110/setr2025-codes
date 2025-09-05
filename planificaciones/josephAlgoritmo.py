import math

def joseph(tareas):
    tqPrevio = 0

    sumatoria = 0
        
    for tareaActual in range(0, len(tareas)):
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
                    print("PF = ",tq,"\n")
                    finAlgoritmo = True
                else:
                    tqPrevio = tq
                    
                    q = q+1
                    sumatoria = 0