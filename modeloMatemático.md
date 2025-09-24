# Modelo Matemático del Sistema M/M/1/K/∞  

En este apartado se presenta la formulación teórica del sistema de colas **M/M/1/K/∞**, donde se considera un único servidor, llegadas de tipo Poisson y tiempos de servicio con distribución exponencial.  

---

## Parámetros básicos  
- **λ**: tasa promedio de llegadas.  
- **μ**: tasa promedio de servicio.  
- **ρ = λ/μ**: coeficiente de utilización o intensidad de tráfico.  
- **Nₛ**: valor esperado de clientes en todo el sistema.  
- **Tₛ**: tiempo promedio de permanencia en el sistema.  
- **N𝑤**: número medio de clientes únicamente en la cola.  
- **T𝑤**: tiempo medio de espera en la cola.  

---

## Distribución de probabilidades de estado  

Cuando **ρ ≠ 1**:  

$$
P_0 = \frac{1-\rho}{1-\rho^{K+1}}
$$

$$
P_n = \frac{(1-\rho)\rho^n}{1-\rho^{K+1}}, \quad n=0,1,\dots,K
$$

$$
P_K = \frac{(1-\rho)\rho^K}{1-\rho^{K+1}}
$$

En el caso límite **ρ = 1** (llegadas y servicios con igual tasa):  

$$
P_n = \frac{1}{K+1}, \quad n=0,1,\dots,K
$$

---

## Número esperado de clientes en el sistema (Nₛ)  

$$
N_s = \frac{\rho \left[1 - (K+1)\rho^K + K\rho^{K+1}\right]}{(1 - \rho)(1 - \rho^{K+1})}
$$

---

## Tiempo promedio en el sistema (Tₛ)  

$$
T_s = \frac{N_s}{\lambda (1 - P_K)}
$$  

donde $\lambda (1 - P_K)$ corresponde a la **tasa de llegadas efectivas** (solo los clientes que logran ingresar al sistema).  

---

## Número esperado de clientes en cola (N𝑤)  

$$
N_w = N_s - (1 - P_0)
$$  

y  

$$
P_0 = \frac{1-\rho}{1-\rho^{K+1}}
$$  

---

## Tiempo promedio de espera en cola (T𝑤)  

$$
T_w = \frac{N_w}{\lambda (1 - P_K)}
$$  

---

## Notas adicionales  
- $P_K$ indica la probabilidad de **bloqueo** (sistema lleno).  
- $\lambda (1 - P_K)$ representa el **flujo real de llegadas atendidas**, ya que descarta a los clientes rechazados.
---


---

## Resultados esperados teóricos

A continuación se muestran los valores teóricos esperados para tres configuraciones diferentes del sistema M/M/1/K/∞, usando la versión sin bloqueo (K → ∞), ya que se compara contra NetLogo que no tiene límite de capacidad.

---

### Simulación 1: Baja carga (ρ = 0.5)

- **λ = 0.5**
- **μ = 1.0**
- **ρ = λ / μ = 0.5**

$$
\begin{align*}
N_s &= \frac{\rho}{1 - \rho} = \frac{0.5}{1 - 0.5} = 1.0 \\
T_s &= \frac{1}{\mu - \lambda} = \frac{1}{1 - 0.5} = 2.0 \\
N_w &= \frac{\rho^2}{1 - \rho} = \frac{0.25}{0.5} = 0.5 \\
T_w &= \frac{\rho}{\mu - \lambda} = \frac{0.5}{0.5} = 1.0
\end{align*}
$$

---

### Simulación 2: Carga media (ρ ≈ 0.639)

- **λ = 0.90**
- **μ ≈ 1.408** (porque tiempo de servicio es 0.71 ticks)
- **ρ ≈ 0.639**

$$
\begin{align*}
N_s &\approx \frac{0.639}{1 - 0.639} \approx 1.768 \\
T_s &\approx \frac{1}{1.408 - 0.90} \approx 1.967 \\
N_w &\approx \frac{0.639^2}{1 - 0.639} \approx 1.131 \\
T_w &\approx \frac{0.639}{1.408 - 0.90} \approx 1.257
\end{align*}
$$

---

### Simulación 3: Alta carga (ρ ≈ 0.855)

- **λ = 0.95**
- **μ ≈ 1.111** (porque tiempo de servicio es 0.90 ticks)
- **ρ ≈ 0.855**

$$
\begin{align*}
N_s &\approx \frac{0.855}{1 - 0.855} \approx 5.896 \\
T_s &\approx \frac{1}{1.111 - 0.95} \approx 6.211 \\
N_w &\approx \frac{0.855^2}{1 - 0.855} \approx 5.054 \\
T_w &\approx \frac{0.855}{1.111 - 0.95} \approx 5.264
\end{align*}
$$

---

Estos valores teóricos permiten validar los resultados obtenidos mediante la simulación en NetLogo. Las diferencias menores entre teoría y práctica se deben a la variabilidad inherente a los modelos estocásticos y al tiempo finito de simulación.
