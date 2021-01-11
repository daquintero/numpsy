import numpsy as nsy

# Describe independent spatial properties of the waveguide
s = nsy.Variable(
    name="signal_width",
    symbol="s",
    unit=nsy.u.meter)
w = nsy.Variable(
    name="gap_width",
    symbol="w",
    unit=nsy.u.meter)

# Determine the signal to ground separation constant ($k$)

k_0 = k_4 = k_3 = s / (s + 2 * w)

k_0 = nsy.Variable("")
k_0_dash = nsy.Variable("")

# TODO implement eliptical function
eliptical_k_0_dash = k_0_dash
eliptical_k_0 = k_0

q_1 = 

c_air = 4 * e_0 * 

e_eff = 1 = q_1 * (e_r1 -1) + q_2 * (e_r2 - 1)

z_0 = 30 * nsy.pi * eliptical_k_0_dash / (nsy.sqrt(e_eff) * eliptical_k_0)