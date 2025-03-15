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

# Bibliography

Access to site of fuzzy: 

> [Fuzzy site](https://scikit-fuzzy.readthedocs.io/en/latest/)