from mesa import Agent, Model
from mesa.time import RandomActivation
import numpy as np

class Cliente(Agent):
    def __init__(self, unique_id, model, llegada):
        super().__init__(unique_id, model)
        self.llegada = llegada
        self.inicio_servicio = None
        self.salida = None

    def step(self):
        pass

class Servidor(Agent):
    def __init__(self, unique_id, model, mu):
        super().__init__(unique_id, model)
        self.mu = mu
        self.ocupado = False
        self.cliente_actual = None
        self.tiempo_restante = 0

    def step(self):
        if self.ocupado:
            self.tiempo_restante -= 1
            if self.tiempo_restante <= 0:
                self.cliente_actual.salida = self.model.schedule.steps
                self.model.completados.append(self.cliente_actual)
                self.cliente_actual = None
                self.ocupado = False

        if not self.ocupado and len(self.model.cola) > 0:
            cliente = self.model.cola.pop(0)
            cliente.inicio_servicio = self.model.schedule.steps
            self.cliente_actual = cliente
            self.ocupado = True
            self.tiempo_restante = np.random.exponential(1/self.mu)

class SistemaColas(Model):
    def __init__(self, lambd, mu, tiempo_max):
        self.lambd = lambd
        self.mu = mu
        self.schedule = RandomActivation(self)
        self.servidor = Servidor(0, self, mu)
        self.schedule.add(self.servidor)
        self.cola = []
        self.completados = []
        self.tiempo_max = tiempo_max
        self.id_cliente = 1

    def step(self):
        if np.random.rand() < self.lambd:
            cliente = Cliente(self.id_cliente, self, self.schedule.steps)
            self.schedule.add(cliente)
            self.cola.append(cliente)
            self.id_cliente += 1
        self.schedule.step()

    def correr(self):
        for _ in range(self.tiempo_max):
            self.step()

        n_s = np.mean([c.salida - c.llegada for c in self.completados])
        n_w = np.mean([c.inicio_servicio - c.llegada for c in self.completados])
        t_s = np.mean([c.salida - c.llegada for c in self.completados])
        t_w = np.mean([c.inicio_servicio - c.llegada for c in self.completados])
        rho = sum([1 for c in self.completados if c.inicio_servicio]) / self.tiempo_max

        return {
            "N_s": n_s,
            "N_w": n_w,
            "T_s": t_s,
            "T_w": t_w,
            "Rho": rho
        }

# Ejemplo de ejecución
modelo = SistemaColas(lambd=0.5, mu=1, tiempo_max=10000)
resultados = modelo.correr()
print(resultados)
