### Installation

*Import NumpSy*


```python
import numpsy as nsy
```

## Units

#### Declare a Unit


```python
meter = nsy.Unit(name="meter", symbol="m")
meter
```




|                     | Unit                            |
|:--------------------|:--------------------------------|
| name                | meter                           |
| symbol              | \begin{equation}m\end{equation} |
| symbolic_expression | \begin{equation}Ø\end{equation} |



#### Retrieve attributes from this Unit


```python
meter.s
```




$\displaystyle m$




```python
meter.symbol
```




$\displaystyle m$




```python
meter.name
```




    'meter'



#### Operate with this unit


```python
farad_per_meter = nsy.Unit(name="Farad", symbol="F") / meter
farad_per_meter
```




|                     | Unit                                      |
|:--------------------|:------------------------------------------|
| name                | (Farad)_per_(meter)                       |
| symbol              | \begin{equation}Ø\end{equation}           |
| symbolic_expression | \begin{equation}\frac{F}{m}\end{equation} |



#### Append to Unit Library


```python
nsy.Units().data
```




    Hertz     Unit       name name_expression               ...
    Farad     Unit       name name_expression               ...
    meter     Unit       name name_expression               ...
    ohm       Unit     name name_expression                 ...
    ratio     Unit       name name_expression               ...
    second    Unit        name name_expression              ...
    Name: 0, dtype: object




```python
nsy.u
```




    Hertz     Unit       name name_expression               ...
    Farad     Unit       name name_expression               ...
    meter     Unit       name name_expression               ...
    ohm       Unit     name name_expression                 ...
    ratio     Unit       name name_expression               ...
    second    Unit        name name_expression              ...
    Name: 0, dtype: object



## Constant


```python
e_0 = nsy.Constant(
    name="permittivity_vaccum",
    symbol= "\epsilon_0",
    numerical=8.8541878128e-12,
    unit=farad_per_meter
)
e_0
```




|                     | Constant                                                       |
|:--------------------|:---------------------------------------------------------------|
| name                | permittivity_vaccum                                            |
| symbol              | \begin{equation}\epsilon_0\end{equation}                       |
| symbolic_expression | \begin{equation}Ø\end{equation}                                |
| numerical           | 8.8541878128e-12                                               |
| unit                | Symbol: \begin{equation}Ø\end{equation}                        |
|                     | Symbolic Expression: \begin{equation}\frac{F}{m}\end{equation} |




```python
e_0.s
```




$\displaystyle \epsilon_0$




```python
e_0.n
```




    8.8541878128e-12




```python
e_d = nsy.Constant(
    name="dielectric_permittivity",
    symbol= "\epsilon_d",
    numerical=5,
    unit=nsy.u.ratio
)
e_d
```




|                     | Constant                                             |
|:--------------------|:-----------------------------------------------------|
| name                | dielectric_permittivity                              |
| symbol              | \begin{equation}\epsilon_d\end{equation}             |
| symbolic_expression | \begin{equation}Ø\end{equation}                      |
| numerical           | 5                                                    |
| unit                | Symbol: \begin{equation}\end{equation}               |
|                     | Symbolic Expression: \begin{equation}Ø\end{equation} |



#### Constants cannot be mutated


```python
e_d.n = 10
```

    Constant cannot be mutated. You cannot set any attribute value. Instantiate a new variable.


## Variable


```python
capacitor_plate_separation = nsy.Variable(
    name="capacitor_plate_separation",
    symbol= "d",
    numerical=None,
    unit=nsy.u.meter
)
capacitor_plate_separation
```




|                     | Variable                                             |
|:--------------------|:-----------------------------------------------------|
| name                | capacitor_plate_separation                           |
| symbol              | \begin{equation}d\end{equation}                      |
| symbolic_expression | \begin{equation}Ø\end{equation}                      |
| numerical           |                                                      |
| unit                | Symbol: \begin{equation}m\end{equation}              |
|                     | Symbolic Expression: \begin{equation}Ø\end{equation} |




```python
capacitor_plate_separation.s
```




$\displaystyle d$




```python
capacitor_plate_separation.u
```




|                     | Unit                            |
|:--------------------|:--------------------------------|
| name                | meter                           |
| symbol              | \begin{equation}m\end{equation} |
| symbolic_expression | \begin{equation}Ø\end{equation} |



#### Variables can be mutated


```python
capacitor_plate_separation.n = 1e-6
capacitor_plate_separation.n
```




    1e-06




```python
capacitor_plate_separation.numerical = 3e-5
capacitor_plate_separation.numerical
```




    3e-05



#### Operate between Value objects
Constants and Variables are value objects.


```python
capacitance_per_plate_cross_sectional_area = e_d / (e_0 * capacitor_plate_separation)
capacitance_per_plate_cross_sectional_area
```




|                     | Value                                                         |
|:--------------------|:--------------------------------------------------------------|
| name                |                                                               |
| symbol              | \begin{equation}Ø\end{equation}                               |
| symbolic_expression | \begin{equation}\frac{\epsilon_d}{\epsilon_0 d}\end{equation} |
| numerical           | 1.8823484456216984e+16                                        |
| unit                | Symbol: \begin{equation}Ø\end{equation}                       |
|                     | Symbolic Expression: \begin{equation}\frac{}{F}\end{equation} |




```python
capacitance_per_plate_cross_sectional_area.se
```




$\displaystyle \frac{\epsilon_d}{\epsilon_0 d}$




```python
capacitance_per_plate_cross_sectional_area.n
```




    1.8823484456216984e+16



#### Perform Flexible Class Operations


```python
raw_capacitor_cross_sectional_area = (1e-6) ** 2
raw_capacitor_cross_sectional_area
```




    1e-12




```python
device_capacitance = capacitance_per_plate_cross_sectional_area * raw_capacitor_cross_sectional_area
device_capacitance
```




|                     | Value                                                           |
|:--------------------|:----------------------------------------------------------------|
| name                |                                                                 |
| symbol              | \begin{equation}Ø\end{equation}                                 |
| symbolic_expression | \begin{equation}\frac{\epsilon_d Ø}{\epsilon_0 d}\end{equation} |
| numerical           | 18823.484456216982                                              |
| unit                | Symbol: \begin{equation}Ø\end{equation}                         |
|                     | Symbolic Expression: \begin{equation}\frac{Ø}{F}\end{equation}  |




```python
device_capacitance.name
```




    ''




```python
device_capacitance.se
```




$\displaystyle \frac{\epsilon_d Ø}{\epsilon_0 d}$




```python
device_capacitance.symbol = "F"
device_capacitance.symbol
```




$\displaystyle F$




```python
raw_capacitor_cross_sectional_area
```




    1e-12



##### Example Functions


```python
nsy.sqrt(device_capacitance)
```




|                     | Value                                                                 |
|:--------------------|:----------------------------------------------------------------------|
| name                |                                                                       |
| symbol              | \begin{equation}Ø\end{equation}                                       |
| symbolic_expression | \begin{equation}\sqrt{F}\end{equation}                                |
| numerical           | 137.19870428038664                                                    |
| unit                | Symbol: \begin{equation}Ø\end{equation}                               |
|                     | Symbolic Expression: \begin{equation}\sqrt{\frac{Ø}{F}}\end{equation} |




```python
nsy.sinh(device_capacitance)
```

    /Users/daquintero/Documents/numpsy/numpsy/functions.py:53: RuntimeWarning: overflow encountered in sinh
      new.numerical = np.sinh(instance_parameters["numerical"])





|                     | Value                                                                 |
|:--------------------|:----------------------------------------------------------------------|
| name                |                                                                       |
| symbol              | \begin{equation}Ø\end{equation}                                       |
| symbolic_expression | \begin{equation}\sinh{\left(F \right)}\end{equation}                  |
| numerical           | inf                                                                   |
| unit                | Symbol: \begin{equation}Ø\end{equation}                               |
|                     | Symbolic Expression: \begin{equation}\sqrt{\frac{Ø}{F}}\end{equation} |


