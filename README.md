# NumpSy

Straight up mix between NumPy, SymPy and Pandas into a value single-declaration extendable framework to simulatenously perform symbolic and numerical operations.

Objectives:
1. Aid mathematical system derivation, understanding, analysis and scientific functionality. 


## Quick Start

Local install after downloading the Anaconda distribution or equivalent:
```bash
>>> git clone https://github.com/daquintero/numpsy.git
>>> cd numpsy
>>> python3 setup.py install
```

## Quick Example
```py
import numpsy as nsy

# Create a unit and operate with it
>>> farad_unit = nsy.Unit(name="Farad", symbol="F")
>>> farad_unit
<Unit name:"Farad" symbol:"F" symbolic_expression:"">
>>> farad_per_meter = farad_unit / nsy.Unit("meter", "m")
>>> farad_per_meter
<Unit name:"(Farad_by_meter)" symbol:"" symbolic_expression:"F/m">
>>> farad_per_meter.se
F/m

# Create a constant
>>> e_0 = nsy.Constant(
    name="permittivity_vaccum",
    symbol= "\epsilon_0",
    number=8.8541878128e-12,
    unit=farad_per_meter)
>>> e_0
<Constant name:"permittivity_vaccum" symbol:"\epsilon_0" symbolic_expression:"None" number:"8.8541878128e-12" unit:"<Unit name:"(Farad_by_meter)" symbol:"" symbolic_expression:"F/m">">
>>> e_0.n
8.8541878128e-12

# Operate between Value objects
>>> roadtrip_distance = nsy.Variable(
     name="roadtrip_distance",
     symbol= "r",
     number=100,
     unit=nsy.Unit("meter", "m"))
>>> car_speed = nsy.Variable(
    name="car_speed",
    symbol= "c",
    number=20,
    unit= nsy.Unit("meter", "m") / nsy.Unit("second", "s") )
>>> time_to_arrive = roadtrip_distance / car_speed
>>> time_to_arrive.n
5.0

```
More advanced examples in `docs/examples/coplanar_waveguide_design.ipynb`.


### Is it any good?
I think it's an elegant mathematical representation to simultanously perform symbolic, numerical, and data science operations into a single system.

### Future plans
* Extend unit management and verification.
* Create a full constants list, probably even in Excel or as an importable CSV file into Pandas.

Open to contributions.
