class Tarea:
    def __init__(self, tiempoEjecucion, periodo, vencimiento):
        self.tiempoEjecucion = tiempoEjecucion
        self.periodo = periodo
        self.vencimiento = vencimiento
    
    def __str__(self):
        return f'Tarea({self.tiempoEjecucion}, {self.periodo}, {self.vencimiento})'