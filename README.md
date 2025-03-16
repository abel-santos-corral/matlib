# matlib

Matlib and fuzzy for difuse systems

# Configuration of VS Code

To configure VS Code and having a dev environment, follow the steps:

## Create virtual environment

First, please go to project folder and execute:

``` 
python -m venv venv
```

## Activate virtual environment

It will depend upon the operating system (OS).

__Linux__

```
source venv/bin/activate
```

__Windows (Power shell)__

```
venv\Scripts\Activate.ps1
```

__Windows (Command prompt)__

```
venv\Scripts\activate
```

## Install dependencies

Install dependencies with

```
pip install -r requirements.txt
```

# Installation

To install packages:
```
pip install numpy matplotlib scikit-fuzzy scipy
```

To execute prograns to get the graphs:
``` 
python3 matlib_vara.py
python3 matlib_varb.py
python3 matlib_varc.py
python3 matlib_out.py
```

To execute query to get where is intersecting a value. Example for VarA:
```
python3 query_vara.py
```

To execute program to see graph for w of Yager family:
```
python3 w_yager.py
```

More information on w value in next section. 

# Yager Membership Function  

In the **Yager family**, the parameter `w` is a **control parameter** that adjusts the smoothness of the membership function.  
The higher the value of `w`, the smoother and less abrupt the transition of membership values.  

The general Yager function is defined as:  

$$
\mu_A(x) = 1 - \left( \max(0, 1 - \frac{|x - c|}{a}) \right)^w
$$  

Where:  
- `c` is the center of the fuzzy set.  
- `a` is the width of the fuzzy set.  
- `w` controls the smoothness of the curve.  

---

## 📌 Criteria for choosing `w`  

1. **Desired level of fuzziness:**  
   - A **small value of `w`** (e.g., `w ≈ 1` or `w ≈ 2`) produces a **smooth transition**, useful when uncertainty is high.  
   - A **large value of `w`** (e.g., `w > 5`) creates a more **abrupt curve**, useful when stricter classification is desired.  

2. **System sensitivity:**  
   - If the system requires a **more gradual decision-making process** (e.g., temperature control systems, pattern recognition), **a low `w` is preferred**.  
   - If the application requires **sharp and well-defined changes** (e.g., industrial process control with strict boundaries), **a high `w` is used**.  

3. **Experiments and empirical validation:**  
   - Various values of `w` can be tested and **compared with real data** to find the most suitable value.  
   - `w` can be adjusted according to system performance metrics (accuracy, stability, etc.).  

4. **Practical applications:**  
   - **Fuzzy control systems:** If used to adjust a continuous variable, a low `w` (`~2-3`) allows better adaptation.  
   - **Fuzzy decision-making:** If the system needs to classify options, a higher `w` (`~5-10`) helps to better define the boundaries between sets.  
   - **Image processing and computer vision:** To detect edges or segmentation, `w` can be adjusted depending on the required level of detail.  

---

## 📊 Practical Example: Temperature Adjustment in a Climate Control System  

- If the **temperature change must be gradual**, use `w = 2`.  
- If the **system needs to react quickly**, use `w = 8` or higher.  

**Graphically**, small values of `w` produce smooth transitions, while larger values make the function more like a threshold function.  

🔍 Ejemplo de particiones difusas para la variable **Temperatura**

Supongamos que tenemos tres conjuntos difusos:

    - Frío (μ1)
    - Tibio (μ2)
    - Caliente (μ3)

### Universo de Discurso (D):
Rango de temperaturas entre 0°C y 40°C.

### Funciones de pertenencia:
- **Frío (μ1):**  
    - Trapezoidal con soporte completo en [0, 15] y declive suave hasta 20.  
    - \( \mu_1(x) = 1 \) si \( x \leq 15 \)  
    - \( \mu_1(x) = \frac{20 - x}{5} \) si \( 15 < x \leq 20 \)  
    - \( \mu_1(x) = 0 \) si \( x > 20 \)  

- **Tibio (μ2):**  
    - Triangular con centro en 25 y soporte de [15, 35].  
    - \( \mu_2(x) = \frac{x - 15}{10} \) si \( 15 < x \leq 25 \)  
    - \( \mu_2(x) = \frac{35 - x}{10} \) si \( 25 < x \leq 35 \)  
    - \( \mu_2(x) = 0 \) si \( x \leq 15 \) o \( x \geq 35 \)  

- **Caliente (μ3):**  
    - Trapezoidal con soporte completo en [30, 40] y declive suave desde 25.  
    - \( \mu_3(x) = 0 \) si \( x < 25 \)  
    - \( \mu_3(x) = \frac{x - 25}{5} \) si \( 25 \leq x \leq 30 \)  
    - \( \mu_3(x) = 1 \) si \( x > 30 \)  

---

🔑 **Propiedad de Partición Difusa:**  

En cada punto \( x \in D \), la suma de pertenencias de **Frío**, **Tibio** y **Caliente** debe ser 1:  
\[
\mu_1(x) + \mu_2(x) + \mu_3(x) = 1
\]

## Cálculo del número de tuplas de entrada

Para calcular el número de tuplas de entrada posibles, simplemente multiplicamos la cantidad de términos en cada variable de entrada:

- La variable `VarA` tiene **3 términos**: `terA1`, `terA2`, `terA3`.
- La variable `VarB` tiene **4 términos**: `terB1`, `terB2`, `terB3`, `terB4`.

Entonces, el número total de combinaciones o tuplas posibles es:

Número de tuplas = 3 × 4 = 12


Por lo tanto, existen **12 tuplas posibles** para las variables de entrada.

## ¿Cuántas reglas necesito?

En un sistema de inferencia difusa basado en reglas, normalmente se define **una regla por cada tupla de entrada posible**. Esto significa que necesitas **12 reglas**, una para cada combinación de términos de `VarA` y `VarB`.

### Ejemplo de reglas
- Si `VarA` es `terA1` y `VarB` es `terB1`, entonces `VarOut` es `VarOut1`.
- Si `VarA` es `terA1` y `VarB` es `terB2`, entonces `VarOut` es `VarOut2`.
- ...
- Si `VarA` es `terA3` y `VarB` es `terB4`, entonces `VarOut` es `VarOut3`.


### 🔍 Cómo calcular el corte de una función de pertenencia triangular

Cuando cortas la función de pertenencia a un nivel máximo de 0.67, básicamente estás intersectando la curva con una línea horizontal en \( y = 0.67 \). Para calcular los puntos \( x \) correspondientes, necesitas:

1. **Definir la función de pertenencia original (triangular).**
2. **Resolver la intersección de esa función con el nivel \( 0.67 \).**

---

### 📌 Cálculo manual:

La función de pertenencia triangular \( \text{VarOut2} \) está definida como:

- \( 0 \) para \( x \leq 0 \) o \( x \geq 10 \)
- \( \frac{x}{5} \) para \( 0 \leq x \leq 5 \)
- \( \frac{10 - x}{5} \) para \( 5 \leq x \leq 10 \)

Queremos saber dónde esta función es igual a \( 0.67 \).

Para \( 0 \leq x \leq 5 \):
\[
\frac{x}{5} = 0.67 \implies x = 0.67 \times 5 = 3.35
\]

Para \( 5 \leq x \leq 10 \):
\[
\frac{10 - x}{5} = 0.67 \implies 10 - x = 0.67 \times 5 \implies x = 10 - 3.35 = 6.65
\]

---

### 📌 Resultado:

El corte ocurre entre los puntos \( x = 3.35 \) y \( x = 6.65 \).


# Bibliography

Access to site of fuzzy: 

> [Fuzzy site](https://scikit-fuzzy.readthedocs.io/en/latest/)