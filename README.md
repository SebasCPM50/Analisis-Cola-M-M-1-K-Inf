# Proyecto: Sistema de Colas M/M/1/K/∞

## Introducción  
Este proyecto estudia el comportamiento de un sistema de colas **M/M/1/K/∞**, que se caracteriza por:  
- Llegadas con distribución Poisson (tasa λ).  
- Tiempos de servicio con distribución exponencial (tasa μ).  
- Un único servidor y una cola de capacidad máxima K.  
- Los clientes que llegan cuando el sistema está lleno (n = K) son bloqueados.  

El trabajo combina el modelo matemático (teoría de colas) con la simulación computacional, utilizando **MESA** en Python para comprobar los resultados.  

---

## Objetivos  
- Desarrollar el modelo matemático del sistema M/M/1/K/∞.  
- Calcular métricas de desempeño teóricas:  
  - Número esperado de clientes en el sistema (Ns).  
  - Tiempo promedio en el sistema (Ts).  
  - Número esperado de clientes en cola (Nw).  
  - Tiempo promedio de espera en cola (Tw).  
  - Probabilidad de bloqueo (Pk).  
- Implementar una simulación computacional del sistema con MESA.  
- Comparar resultados teóricos con los obtenidos en la simulación.  

---

## Modelo Matemático  

- **Probabilidad de que el sistema esté vacío (P0):**  
  P0 = (1 - ρ) / (1 - ρ^(K+1))  

- **Probabilidad de que haya n clientes (Pn):**  
  Pn = [(1 - ρ) * ρ^n] / (1 - ρ^(K+1))  

- **Probabilidad de bloqueo (Pk):**  
  Pk = [(1 - ρ) * ρ^K] / (1 - ρ^(K+1))  

- **Número esperado de clientes en el sistema (Ns):**  
  Ns = [ρ * (1 - (K+1)ρ^K + Kρ^(K+1))] / [(1 - ρ)(1 - ρ^(K+1))]  

- **Tiempo promedio en el sistema (Ts):**  
  Ts = Ns / [λ * (1 - Pk)]  

- **Número esperado de clientes en cola (Nw):**  
  Nw = Ns - (1 - P0)  

- **Tiempo promedio en cola (Tw):**  
  Tw = Nw / [λ * (1 - Pk)]  

---

## Simulación con MESA  
La simulación fue desarrollada en Python usando el framework **MESA**.  

- **Clientes**: agentes que llegan al sistema de acuerdo con la tasa λ.  
- **Servidor**: atiende clientes con tasa μ siguiendo la disciplina FIFO.  
- El modelo registra métricas como Ns, Ts, Nw, Tw y la utilización del servidor.  

El objetivo es comprobar que los resultados de la simulación se aproximan a los valores teóricos a medida que aumenta el tiempo de ejecución.  

---

## Resultados  
Se realizaron tres configuraciones distintas:  
1. **Baja carga** (ρ = 0.5).  
2. **Carga media** (ρ ≈ 0.64).  
3. **Alta carga** (ρ ≈ 0.85).  

En todos los casos, los resultados de la simulación coincidieron con los valores teóricos dentro de un margen razonable, confirmando la validez del modelo.  

---

## Conclusiones  
- Los resultados simulados validan los valores teóricos del sistema M/M/1/K/∞.  
- La probabilidad de bloqueo Pk permite estimar la capacidad real del sistema y el rechazo de clientes.  
- El tiempo promedio en el sistema y en la cola aumenta considerablemente cuando la utilización (ρ) se acerca a 1.  
- El framework **MESA** demostró ser una herramienta adecuada para modelar y validar sistemas de colas de manera experimental.  
- La integración de teoría y simulación proporciona una visión más completa y realista del comportamiento del sistema.  
