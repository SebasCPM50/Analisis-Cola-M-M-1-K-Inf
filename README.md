# Simulación de un Sistema de Colas M/M/1 con MESA

## Introducción  
Este proyecto implementa un sistema de colas **M/M/1** utilizando el framework **MESA** en Python.  
El objetivo es comprobar los resultados teóricos de la teoría de colas con los obtenidos mediante simulación computacional.  

---

## Objetivos  
- Implementar un modelo de simulación discreta basado en agentes.  
- Calcular métricas de desempeño del sistema:  
  - Número promedio de clientes en el sistema (Nₛ).  
  - Tiempo promedio en el sistema (Tₛ).  
  - Número promedio de clientes en cola (N𝑤).  
  - Tiempo promedio en cola (T𝑤).  
  - Utilización del servidor (ρ).  
- Comparar los resultados de simulación con los valores teóricos.  

---

## Implementación  
El modelo fue desarrollado en Python con **MESA**.  

Se definen:  
- **Clientes**: usuarios que llegan al sistema siguiendo una distribución de Poisson (tasa λ).  
- **Servidor**: atiende clientes uno por uno, con tiempos de servicio exponenciales (tasa μ) y cola FIFO.  

La simulación registra métricas de desempeño y permite comparar teoría y práctica.  

---

## Resultados esperados  
Según la teoría de colas:  
- Los valores de Nₛ, Tₛ, N𝑤 y T𝑤 dependen de la intensidad de tráfico ρ = λ / μ.  
- Al aumentar el tiempo de simulación, los resultados se aproximan a los valores teóricos.  

---

## Conclusiones  
- Los resultados obtenidos con MESA validan los valores teóricos de un sistema M/M/1.  
- La diferencia entre simulación y teoría se debe a la naturaleza estocástica del modelo y al tiempo finito de simulación.  
- El framework **MESA** es una herramienta eficaz para modelar y validar sistemas de colas de manera experimental.  
