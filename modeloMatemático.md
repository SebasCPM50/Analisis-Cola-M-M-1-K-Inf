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

## Comentario final  
- $P_K$ indica la probabilidad de **bloqueo** (sistema lleno).  
- $\lambda (1 - P_K)$ representa el **flujo real de llegadas atendidas**, ya que descarta a los clientes rechazados.  
