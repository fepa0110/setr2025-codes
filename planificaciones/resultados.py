from Tarea import Tarea
from josephAlgoritmo import *
from calculosStr import *

tareasSTR1 = [Tarea(1, 4, 4), Tarea(2, 5, 5), Tarea(2, 8, 8)]
tareasSTR2 = [Tarea(1, 4, 4), Tarea(2, 6, 6), Tarea(1, 9, 9), Tarea(2, 11, 11)]
tareasSTR3 = [Tarea(1, 4, 4), Tarea(2, 7, 7), Tarea(3, 12, 12), Tarea(2, 15, 15)]
tareasSTR4 = [Tarea(1, 5, 5), Tarea(1, 6, 6), Tarea(1, 8, 8), Tarea(2, 10, 10), Tarea(3, 15, 15)]
tareasSTR5 = [Tarea(1, 8, 8), Tarea(1, 9, 9), Tarea(3, 11, 11), Tarea(2, 14, 14), Tarea(5, 20, 20)]
tareasSTR6 = [Tarea(1, 4, 4), Tarea(1, 7, 7), Tarea(1, 10, 10), Tarea(2, 15, 15), 
            Tarea(3, 18, 18), Tarea(4, 20, 20)]
tareasSTR7 = [Tarea(3, 45, 45), Tarea(4, 50, 50), Tarea(7, 60, 60), Tarea(11, 70, 70), 
            Tarea(5, 85, 85), Tarea(2, 90, 90), Tarea(10, 95, 95)]
tareasSTR8 = [Tarea(28, 125, 125), Tarea(2, 272, 272), Tarea(1175, 6000, 6000), Tarea(9, 12000, 12000), 
            Tarea(1880, 27000, 27000), Tarea(1880, 33000, 33000), Tarea(5000, 100000, 100000)]
tareasSTR9 = [Tarea(500, 2560, 2560), Tarea(5000, 40960, 40960), Tarea(15000, 61440, 61440), 
            Tarea(30000, 983040, 983040), Tarea(50000, 1024000, 1024000), Tarea(1000, 1280000, 1280000)]
tareasSTR10 = [
            Tarea(2, 25, 25),
            Tarea(5, 25, 25),
            Tarea(1, 40, 40),
            Tarea(3, 50, 50),
            Tarea(5, 50, 50),
            Tarea(8, 59, 59),
            Tarea(9, 80, 80),
            Tarea(2, 80, 80),
            Tarea(5, 100, 100),
            Tarea(3, 200, 200),
            Tarea(3, 200, 200),
            Tarea(1, 200, 200),
            Tarea(1, 200, 200),
            Tarea(3, 200, 200),
            Tarea(1, 1000, 1000),
            Tarea(1, 1000, 1000)
            ]

def seleccionar_str():
    seleccion = input("Ingrese el numero de STR: ")

    if(seleccion == "1"): return tareasSTR1
    if(seleccion == "2"): return tareasSTR2
    if(seleccion == "3"): return tareasSTR3
    if(seleccion == "4"): return tareasSTR4
    if(seleccion == "5"): return tareasSTR5
    if(seleccion == "6"): return tareasSTR6
    if(seleccion == "7"): return tareasSTR7
    if(seleccion == "8"): return tareasSTR8
    if(seleccion == "9"): return tareasSTR9
    if(seleccion == "10"): return tareasSTR10

tareas = seleccionar_str()

def mostrar_str(tareas):
    tareas_str = "S({}) = ".format(len(tareas))

    for tarea in tareas:
        tareas_str = tareas_str + str(tarea) + ", "
    print(tareas_str,"\n")

mostrar_str(tareas)
print("H = ",hiperperiodo(tareas))
factor_utilizacion_print(tareas)
print("\nPlanificable por Liu(RM)? {}".format(planificable_liu_rm(tareas)))
print("Planificable por Liu(EDF)? {}".format(planificable_liu_edf(tareas)))
print("Planificable por Bini(RM)? {}\n".format(planificable_bini(tareas)))
joseph(tareas)

print("\nCalculo de ranura libre\n")
ranuraLibrePorJoseph(tareas)

# print(math.lcm(4,5,8))