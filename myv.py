class Tarea:
    def __init__(self, tiempoEjecucion, periodo, vencimiento):
        self.tiempoEjecucion = tiempoEjecucion
        self.periodo = periodo
        self.vencimiento = vencimiento
    
    def __str__(self):
        return f'Tarea({self.tiempoEjecucion}, {self.periodo}, {self.vencimiento})'


def joseph():
    tarea1 = Tarea(1, 4, 4)
    tarea2 = Tarea(2, 5, 5)
    tarea3 = Tarea(2, 8, 8)

    tareas = [tarea1, tarea2, tarea3]

    for q in range(0, 2):
        print(tareas[q])

joseph()