import math

def hiperperiodo(tareas):
    mcm = tareas[0].periodo

    for indiceTarea in range(1,len(tareas)):
        mcm = math.lcm(mcm,tareas[indiceTarea].periodo)

    return mcm

def factor_utilizacion_print(tareas): 
    fu = 0
    tiempos_utilizacion = ""
    formula_utilizada = "FU = "

    for indiceTarea in range(0, len(tareas)):
        tarea = tareas[indiceTarea]
        tiempos_utilizacion += "|U{} = {}/{}| ".format(indiceTarea+1,tarea.tiempoEjecucion, tarea.periodo)

        formula_utilizada = formula_utilizada + "{}/{}".format(tarea.tiempoEjecucion, tarea.periodo)
        if(not(indiceTarea == len(tareas)-1)):
            formula_utilizada = formula_utilizada + " + "

        fu = fu + tarea.tiempoEjecucion / tarea.periodo

    print(tiempos_utilizacion)
    print(formula_utilizada + " = ",f'{fu:.2f}')

def factor_utilizacion(tareas): 
    fu = 0

    for tarea in tareas:
        fu = fu + tarea.tiempoEjecucion / tarea.periodo

    return fu

def planificable_liu_rm(tareas):
    cantidadTareas = len(tareas)

    return factor_utilizacion(tareas) <= cantidadTareas * (math.exp2(1/cantidadTareas) - 1)

def planificable_liu_edf(tareas):
    return factor_utilizacion(tareas) <= 1

def planificable_bini(tareas):
    resultado = 1

    for tarea in tareas:
        fu = tarea.tiempoEjecucion / tarea.periodo
        resultado = resultado * (fu + 1)
        
        if(resultado > 2): return False
    
    return resultado <= 2