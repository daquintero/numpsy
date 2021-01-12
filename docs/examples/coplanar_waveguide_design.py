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
k_0 = nsy.Variable(name="signal_to_ground_constant",
                   symbol="k_0")

k_0 = k_4 = k_3 = s / (s + 2 * w)



z_0 = 30 * nsy.pi * eliptical_k_0_dash / (nsy.sqrt(e_eff) * eliptical_k_0)
