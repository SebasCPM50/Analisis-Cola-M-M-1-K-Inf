# Proyecto: Sistema de Colas M/M/1/K/∞

## Introducción  
Este proyecto estudia el comportamiento de un sistema de colas **M/M/1/K/∞**, que se caracteriza por:  
- Llegadas con distribución Poisson (tasa **λ**).  
- Tiempos de servicio con distribución exponencial (tasa **μ**).  
- Un único servidor y una cola de capacidad máxima **K**.  
- Los clientes que llegan cuando el sistema está lleno (**n = K**) son bloqueados.  

El trabajo combina el modelo matemático (teoría de colas) con la simulación computacional, utilizando **MESA** en Python para comprobar los resultados.  

---

## Objetivos  
- Desarrollar el modelo matemático del sistema M/M/1/K/∞.  
- Calcular métricas de desempeño teóricas:  
  - Número esperado de clientes en el sistema (**Nₛ**).  
  - Tiempo promedio en el sistema (**Tₛ**).  
  - Número esperado de clientes en cola (**N𝑤**).  
  - Tiempo promedio de espera en cola (**T𝑤**).  
  - Probabilidad de bloqueo (**Pₖ**).  
- Implementar una simulación computacional del sistema con MESA.  
- Comparar resultados teóricos con los obtenidos en la simulación.  

---

## Modelo Matemático  

**Probabilidad de que el sistema esté vacío (P₀):**

$$
P_0 = \frac{1 - \rho}{1 - \rho^{K+1}}
$$

**Probabilidad de que haya n clientes (Pₙ):**

$$
P_n = \frac{(1 - \rho)\rho^n}{1 - \rho^{K+1}}, \quad n=0,1,\dots,K
$$

**Probabilidad de bloqueo (Pₖ):**

$$
P_K = \frac{(1 - \rho)\rho^K}{1 - \rho^{K+1}}
$$

**Número esperado de clientes en el sistema (Nₛ):**

$$
N_s = \frac{\rho \left[1 - (K+1)\rho^K + K\rho^{K+1}\right]}{(1 - \rho)(1 - \rho^{K+1})}
$$

**Tiempo promedio en el sistema (Tₛ):**

$$
T_s = \frac{N_s}{\lambda (1 - P_K)}
$$

**Número esperado de clientes en cola (N𝑤):**

$$
N_w = N_s - (1 - P_0)
$$

**Tiempo promedio en cola (T𝑤):**

$$
T_w = \frac{N_w}{\lambda (1 - P_K)}
$$

---

## Simulación con MESA  
La simulación fue desarrollada en Python usando el framework **MESA**.  

- **Clientes**: agentes que llegan al sistema de acuerdo con la tasa **λ**.  
- **Servidor**: atiende clientes con tasa **μ** siguiendo la disciplina FIFO.  
- El modelo registra métricas como **Nₛ, Tₛ, N𝑤, T𝑤** y la utilización del servidor.  

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
- La probabilidad de bloqueo **Pₖ** permite estimar la capacidad real del sistema y el rechazo de clientes.  
- El tiempo promedio en el sistema y en la cola aumenta considerablemente cuando la utilización (**ρ**) se acerca a 1.  
- El framework **MESA** demostró ser una herramienta adecuada para modelar y validar sistemas de colas de manera experimental.  
- La integración de teoría y simulación proporciona una visión más completa y realista del comportamiento del sistema.  
