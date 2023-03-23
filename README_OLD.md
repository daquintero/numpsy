# NumpSy

Straight up mix between NumPy, SymPy, SciPy, and Pandas into a value single-declaration extendable framework to simulatenously perform symbolic and numerical operations.

Objectives:
1. Ever think you wanted to simultaneously perform numerical and symbolic mathematics for an engineering or optimization derivation? Now you can pretty much intuitively derivate simultaneously whilst performing unit management automatically.
2. Integrate mathematical analytical derivation Python toolchains into a single handy one that retains and expands each of the constituent packages methods. Retain intuitive compatibility.
3. Have fun!

### Is it any good?
I think it's an elegant mathematical representation to simultanously perform symbolic, numerical, and data science operations into a single system.

## Quick Start

Download the [Anaconda distribution first](https://www.anaconda.com/).

Pip install:
```bash
$ pip install numpsy
```

Local install for most recent version:
```bash
$ git clone https://github.com/daquintero/numpsy.git
$ cd numpsy
$ python3 setup.py install
```

## Quick Example
See the [10 minutes to NumpSy jupyter notebook](https://github.com/daquintero/numpsy/blob/master/docs/ten_minutes_to_numpsy/10_minutes_to_numpsy.ipynb) for much more.

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
| symbol              | <p align="center"><img alt="\begin{equation}m\end{equation}" src="docs/latex_readme_svgs/527d9987eeea7e57f03edb180944aa61.png" align="middle" width="357.35353664999997pt" height="16.438356pt"/></p> |
| symbolic_expression | <p align="center"><img alt="\begin{equation}Ø\end{equation}" src="docs/latex_readme_svgs/07e36bc9221df21fb42516103f345343.png" align="middle" width="356.5297131pt" height="16.438356pt"/></p> |



#### Retrieve attributes from this Unit


```python
meter.s
```




<img alt="$\displaystyle m$" src="docs/latex_readme_svgs/991606b7eabce3620029b97e1ecd1c31.png" align="middle" width="14.433101099999991pt" height="14.15524440000002pt"/>




```python
meter.symbol
```




<img alt="$\displaystyle m$" src="docs/latex_readme_svgs/991606b7eabce3620029b97e1ecd1c31.png" align="middle" width="14.433101099999991pt" height="14.15524440000002pt"/>




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
| symbol              | <p align="center"><img alt="\begin{equation}Ø\end{equation}" src="docs/latex_readme_svgs/07e36bc9221df21fb42516103f345343.png" align="middle" width="356.5297131pt" height="16.438356pt"/></p>           |
| symbolic_expression | <p align="center"><img alt="\begin{equation}\frac{F}{m}\end{equation}" src="docs/latex_readme_svgs/c9f49e2c2afbf2a26c4fa9f5343f91cd.png" align="middle" width="357.35353664999997pt" height="33.62942055pt"/></p> |



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
| symbol              | <p align="center"><img alt="\begin{equation}\epsilon_0\end{equation}" src="docs/latex_readme_svgs/ad4dfa78b222bfdc9e66a601c0ff1fa7.png" align="middle" width="357.1604223pt" height="16.438356pt"/></p>                       |
| symbolic_expression | <p align="center"><img alt="\begin{equation}Ø\end{equation}" src="docs/latex_readme_svgs/07e36bc9221df21fb42516103f345343.png" align="middle" width="356.5297131pt" height="16.438356pt"/></p>                                |
| numerical           | 8.8541878128e-12                                               |
| unit                | Symbol: <p align="center"><img alt="\begin{equation}Ø\end{equation}" src="docs/latex_readme_svgs/07e36bc9221df21fb42516103f345343.png" align="middle" width="356.5297131pt" height="16.438356pt"/></p>                        |
|                     | Symbolic Expression: <p align="center"><img alt="\begin{equation}\frac{F}{m}\end{equation}" src="docs/latex_readme_svgs/c9f49e2c2afbf2a26c4fa9f5343f91cd.png" align="middle" width="357.35353664999997pt" height="33.62942055pt"/></p> |




```python
e_0.s
```




<img alt="$\displaystyle \epsilon_0$" src="docs/latex_readme_svgs/8f9f4380689f9e8c59e9b9243394de50.png" align="middle" width="13.224938099999992pt" height="14.15524440000002pt"/>




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
| symbol              | <p align="center"><img alt="\begin{equation}\epsilon_d\end{equation}" src="docs/latex_readme_svgs/ff3c0c16a41ac38c3e2a96276f65416f.png" align="middle" width="357.3056784pt" height="16.438356pt"/></p>             |
| symbolic_expression | <p align="center"><img alt="\begin{equation}Ø\end{equation}" src="docs/latex_readme_svgs/07e36bc9221df21fb42516103f345343.png" align="middle" width="356.5297131pt" height="16.438356pt"/></p>                      |
| numerical           | 5                                                    |
| unit                | Symbol: <p align="center"><img alt="\begin{equation}\end{equation}" src="docs/latex_readme_svgs/e0b0f8e64d3d3c1d20e400710d0c4c41.png" align="middle" width="21.004643549999997pt" height="16.438356pt"/></p>               |
|                     | Symbolic Expression: <p align="center"><img alt="\begin{equation}Ø\end{equation}" src="docs/latex_readme_svgs/07e36bc9221df21fb42516103f345343.png" align="middle" width="356.5297131pt" height="16.438356pt"/></p> |



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
| symbol              | <p align="center"><img alt="\begin{equation}d\end{equation}" src="docs/latex_readme_svgs/0763f4bd58e4e7c340249488c269f6b2.png" align="middle" width="354.41496915pt" height="16.438356pt"/></p>                      |
| symbolic_expression | <p align="center"><img alt="\begin{equation}Ø\end{equation}" src="docs/latex_readme_svgs/07e36bc9221df21fb42516103f345343.png" align="middle" width="356.5297131pt" height="16.438356pt"/></p>                      |
| numerical           |                                                      |
| unit                | Symbol: <p align="center"><img alt="\begin{equation}m\end{equation}" src="docs/latex_readme_svgs/527d9987eeea7e57f03edb180944aa61.png" align="middle" width="357.35353664999997pt" height="16.438356pt"/></p>              |
|                     | Symbolic Expression: <p align="center"><img alt="\begin{equation}Ø\end{equation}" src="docs/latex_readme_svgs/07e36bc9221df21fb42516103f345343.png" align="middle" width="356.5297131pt" height="16.438356pt"/></p> |




```python
capacitor_plate_separation.s
```




<img alt="$\displaystyle d$" src="docs/latex_readme_svgs/4db18991b0ea9ff6ae234a6b44f4c33d.png" align="middle" width="8.55596444999999pt" height="22.831056599999986pt"/>




```python
capacitor_plate_separation.u
```




|                     | Unit                            |
|:--------------------|:--------------------------------|
| name                | meter                           |
| symbol              | <p align="center"><img alt="\begin{equation}m\end{equation}" src="docs/latex_readme_svgs/527d9987eeea7e57f03edb180944aa61.png" align="middle" width="357.35353664999997pt" height="16.438356pt"/></p> |
| symbolic_expression | <p align="center"><img alt="\begin{equation}Ø\end{equation}" src="docs/latex_readme_svgs/07e36bc9221df21fb42516103f345343.png" align="middle" width="356.5297131pt" height="16.438356pt"/></p> |



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
| symbol              | <p align="center"><img alt="\begin{equation}Ø\end{equation}" src="docs/latex_readme_svgs/07e36bc9221df21fb42516103f345343.png" align="middle" width="356.5297131pt" height="16.438356pt"/></p>                               |
| symbolic_expression | <p align="center"><img alt="\begin{equation}\frac{\epsilon_d}{\epsilon_0 d}\end{equation}" src="docs/latex_readme_svgs/40facce99d32bb0b8461bb5c240faaf8.png" align="middle" width="361.4383938pt" height="31.939908pt"/></p> |
| numerical           | 1.8823484456216984e+16                                        |
| unit                | Symbol: <p align="center"><img alt="\begin{equation}Ø\end{equation}" src="docs/latex_readme_svgs/07e36bc9221df21fb42516103f345343.png" align="middle" width="356.5297131pt" height="16.438356pt"/></p>                       |
|                     | Symbolic Expression: <p align="center"><img alt="\begin{equation}\frac{}{F}\end{equation}" src="docs/latex_readme_svgs/402400a45934b32960ffdb2768ee6cbf.png" align="middle" width="356.5639506pt" height="23.604652499999997pt"/></p> |




```python
capacitance_per_plate_cross_sectional_area.se
```




<img alt="$\displaystyle \frac{\epsilon_d}{\epsilon_0 d}$" src="docs/latex_readme_svgs/3b5a0ea48104bf18f1e9d21678c8f47d.png" align="middle" width="22.602815399999997pt" height="36.3965877pt"/>




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
| symbol              | <p align="center"><img alt="\begin{equation}Ø\end{equation}" src="docs/latex_readme_svgs/07e36bc9221df21fb42516103f345343.png" align="middle" width="356.5297131pt" height="16.438356pt"/></p>                                 |
| symbolic_expression | <p align="center"><img alt="\begin{equation}\frac{\epsilon_d Ø}{\epsilon_0 d}\end{equation}" src="docs/latex_readme_svgs/dad110002c83361e975cb3d3bb56b501.png" align="middle" width="363.6983922pt" height="36.894244199999996pt"/></p> |
| numerical           | 18823.484456216982                                              |
| unit                | Symbol: <p align="center"><img alt="\begin{equation}Ø\end{equation}" src="docs/latex_readme_svgs/07e36bc9221df21fb42516103f345343.png" align="middle" width="356.5297131pt" height="16.438356pt"/></p>                         |
|                     | Symbolic Expression: <p align="center"><img alt="\begin{equation}\frac{Ø}{F}\end{equation}" src="docs/latex_readme_svgs/d68142045363ae526a2af7e213720bbf.png" align="middle" width="356.5639506pt" height="34.42851555pt"/></p>  |




```python
device_capacitance.name
```




    ''




```python
device_capacitance.se
```




<img alt="$\displaystyle \frac{\epsilon_d Ø}{\epsilon_0 d}$" src="docs/latex_readme_svgs/5dbd605233a76725ccf89e2d69434815.png" align="middle" width="27.12282045pt" height="46.30526009999998pt"/>




```python
device_capacitance.symbol = "F"
device_capacitance.symbol
```




<img alt="$\displaystyle F$" src="docs/latex_readme_svgs/fdd7fc3481f50c7725212c5c1aae26f9.png" align="middle" width="12.85392569999999pt" height="22.465723500000017pt"/>




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
| symbol              | <p align="center"><img alt="\begin{equation}Ø\end{equation}" src="docs/latex_readme_svgs/07e36bc9221df21fb42516103f345343.png" align="middle" width="356.5297131pt" height="16.438356pt"/></p>                                       |
| symbolic_expression | <p align="center"><img alt="\begin{equation}\sqrt{F}\end{equation}" src="docs/latex_readme_svgs/247c82731ced3e2bf916ff89a21707eb.png" align="middle" width="363.41327385pt" height="19.487407499999996pt"/></p>                                |
| numerical           | 137.19870428038664                                                    |
| unit                | Symbol: <p align="center"><img alt="\begin{equation}Ø\end{equation}" src="docs/latex_readme_svgs/07e36bc9221df21fb42516103f345343.png" align="middle" width="356.5297131pt" height="16.438356pt"/></p>                               |
|                     | Symbolic Expression: <p align="center"><img alt="\begin{equation}\sqrt{\frac{Ø}{F}}\end{equation}" src="docs/latex_readme_svgs/35eabbee1c39b85838aa31462abebb1e.png" align="middle" width="366.75572669999997pt" height="39.452455349999994pt"/></p> |




```python
nsy.sinh(device_capacitance)
```





|                     | Value                                                                 |
|:--------------------|:----------------------------------------------------------------------|
| name                |                                                                       |
| symbol              | <p align="center"><img alt="\begin{equation}Ø\end{equation}" src="docs/latex_readme_svgs/07e36bc9221df21fb42516103f345343.png" align="middle" width="356.5297131pt" height="16.438356pt"/></p>                                       |
| symbolic_expression | <p align="center"><img alt="\begin{equation}\sinh{\left(F \right)}\end{equation}" src="docs/latex_readme_svgs/b81ce41e775ff0ebf8f4e88329b48ac4.png" align="middle" width="378.9840615pt" height="16.438356pt"/></p>                  |
| numerical           | inf                                                                   |
| unit                | Symbol: <p align="center"><img alt="\begin{equation}Ø\end{equation}" src="docs/latex_readme_svgs/07e36bc9221df21fb42516103f345343.png" align="middle" width="356.5297131pt" height="16.438356pt"/></p>                               |
|                     | Symbolic Expression: <p align="center"><img alt="\begin{equation}\sqrt{\frac{Ø}{F}}\end{equation}" src="docs/latex_readme_svgs/35eabbee1c39b85838aa31462abebb1e.png" align="middle" width="366.75572669999997pt" height="39.452455349999994pt"/></p> |




### Future plans
* Extend unit management and verification.
* Create a full constants list, probably even in Excel or as an importable CSV file into Pandas.

Open to contributions.
