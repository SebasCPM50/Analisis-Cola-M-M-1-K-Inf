# Modelo Matemático del Sistema M/M/1/K/∞  

En este apartado se presenta la formulación teórica del sistema de colas **M/M/1/K/∞**, donde se considera un único servidor, llegadas de tipo Poisson y tiempos de servicio con distribución exponencial.  

---

## Parámetros básicos  
- **λ**: tasa promedio de llegadas.  
- **μ**: tasa promedio de servicio.  
- **ρ = λ/μ**: coeficiente de utilización o intensidad de tráfico.  
- **N<sub>s</sub>**: valor esperado de clientes en todo el sistema.  
- **T<sub>s</sub>**: tiempo promedio de permanencia en el sistema.  
- **N<sub>w</sub>**: número medio de clientes únicamente en la cola.  
- **T<sub>w</sub>**: tiempo medio de espera en la cola.  

---

## Distribución de probabilidades de estado  

Cuando **ρ ≠ 1**:  

\[
P_0 = \frac{1-\rho}{1-\rho^{K+1}}, 
\quad 
P_n = \frac{(1-\rho)\rho^n}{1-\rho^{K+1}}, \quad n=0,1,\dots,K
\]

\[
P_K = \frac{(1-\rho)\rho^K}{1-\rho^{K+1}}
\]

En el caso límite **ρ = 1** (llegadas y servicios con igual tasa):  

\[
P_n = \frac{1}{K+1}, \quad n=0,1,\dots,K
\]

---

## Número esperado de clientes en el sistema (N<sub>s</sub>)  

El promedio de usuarios en cola más el que está en servicio:  

\[
N_s = \frac{\rho \left[1 - (K+1)\rho^K + K\rho^{K+1}\right]}{(1 - \rho)(1 - \rho^{K+1})}
\]

---

## Tiempo promedio en el sistema (T<sub>s</sub>)  

El tiempo medio de permanencia se obtiene a partir de la **Ley de Little**:  

\[
T_s = \frac{N_s}{\lambda (1 - P_K)}
\]

donde \(\lambda (1 - P_K)\) corresponde a la **tasa de llegadas efectivas** (solo los clientes que logran ingresar al sistema).  

---

## Número esperado de clientes en cola (N<sub>w</sub>)  

\[
N_w = N_s - (1 - P_0)
\]

Aquí, \(P_0\) es la probabilidad de que no haya clientes en el sistema:  

\[
P_0 = \frac{1-\rho}{1-\rho^{K+1}}
\]

---

## Tiempo promedio de espera en cola (T<sub>w</sub>)  

Aplicando nuevamente la relación de Little para la cola:  

\[
T_w = \frac{N_w}{\lambda (1 - P_K)}
\]

---

## Comentario final  
- \(P_K\) indica la probabilidad de **bloqueo** (sistema lleno).  
- \(\lambda (1 - P_K)\) representa el **flujo real de llegadas atendidas**, ya que descarta a los clientes rechazados.  
