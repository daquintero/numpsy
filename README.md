# NumpSy

Straight up mix between NumPy, SymPy and Pandas into a value single-declaration extendable framework to simulatenously perform symbolic and numerical operations.

Objectives:
1. Ever think you wanted to simultaneously have numerical and symbolic mathematical tools for an engineering or optimization derivation? Now you can pretty much intuitively derivate simultaneously numerically and symbolically whilst performing unit management automatically.
2. Integrate mathematical analytical derivation Python toolchains into a single handy one that retains and expands each of the constituent packages methods.
3. Have fun!

## Quick Start

Download the [Anaconda distribution first](https://www.anaconda.com/)

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

```py
>>> import numpsy as nsy
```

#### Create a unit and operate with it
```py
>>> farad_unit = nsy.Unit(name="Farad", symbol="F")
>>> farad_unit
<Unit name:"Farad" symbol:"F" symbolic_expression:"">
>>> farad_per_meter = farad_unit / nsy.Unit("meter", "m")
>>> farad_per_meter
<Unit name:"(Farad_by_meter)" symbol:"" symbolic_expression:"F/m">
>>> farad_per_meter.symbolic_expression
F/m
```

#### Create a constant
```py
>>> e_0 = nsy.Constant(
    name="permittivity_vaccum",
    symbol= "\epsilon_0",
    numerical=8.8541878128e-12,
    unit=farad_per_meter)
>>> e_0
<Constant name:"permittivity_vaccum" symbol:"\epsilon_0" symbolic_expression:"None" numerical:"8.8541878128e-12" unit:"<Unit name:"(Farad_by_meter)" symbol:"" symbolic_expression:"F/m">">
>>> e_0.numerical
8.8541878128e-12
```

#### Create a variable
```py
>> capacitor_plate_separation = nsy.Variable(
...     name="capacitor_plate_separation",
...   `  symbol= "d",
...     numerical=None,
...     unit=nsy.u.meter
... )
>>> capacitor_plate_separation
<Variable name:"capacitor_plate_separation" symbol:"d" symbolic_expression:"None" numerical:"None" unit:"<Unit name:"Meter" symbol:"m" symbolic_expression:"">">

>>> car_speed = nsy.Variable(
    name="car_speed",
    symbol= "c",
    numerical=20,
    unit= nsy.Unit("meter", "m") / nsy.Unit("second", "s") )
>>> time_to_arrive = roadtrip_distance / car_speed
>>> time_to_arrive.n
5.0
```


### Is it any good?
I think it's an elegant mathematical representation to simultanously perform symbolic, numerical, and data science operations into a single system.

### Future plans
* Extend unit management and verification.
* Create a full constants list, probably even in Excel or as an importable CSV file into Pandas.

Open to contributions.
