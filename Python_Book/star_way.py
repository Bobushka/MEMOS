import time
import math
import tqdm

# Inputs
# acceleration while flight, in G-units (1..100)
G = int(input("Enter acceleration in g-units:\n"))
# distance to destination in thousands km
Unit = input("Enter units (km / au / ly):\n")
Dist = float(input("Enter distance in units:\n"))

if Unit == "km":
    if Dist < 20_000:
        # calc chord instead curve
        Dist = 2*6371*math.sin(Dist/(2*6371))  # 6371 = Earth radius in km
    d_fin = Dist
elif Unit == "au":
    d_fin = Dist * 150_000_000                 # 1 astronomic unit = 150 000 000 km
elif Unit == "ly":
    d_fin = Dist * 150_000_000 * 63_241        # 1 light year = 63 241 astronomic units
else:
    print("Unsupported unit")

print(f'distance = {Dist:.{1}f} {Unit}, acceleration = {G} g')

g = G*10
d_half = d_fin / 2


# time presentation subroutine
def calc_time(t):
    Sec = t - 60*(t//60)
    Min = int(t/60) - 60*(t//3600)
    Hrs = int(t/3600) - 24*(t//(3600*24))
    Day = int(t/3600/24)
    return Sec, Min, Hrs, Day


# prepare values to print
def prep_values(velocity, distance):
    V = v / 1000             # velocity in km/s
    D = d / 1000             # distance in km
    AU = D / 150_000_000     # distance in astronomical units
    LY = AU / 63241          # distance in light years
    return V, D, AU, LY


# Acceleration
# Technical values setup
t, v, d = 0, 0, 0

while d < d_half:            # for distance from start to middle
    v = g * t                # current speed in m/s
    d = v * t/2              # total distance in m
    t += 1

# Thus we finished the half of our trip
V, D, AU, LY = prep_values(v, d)    # resize v & d to big values
Sec, Min, Hrs, Day = calc_time(t)   # time in sec-min-hrs-days
print(f'half way: half_time = {Day:03}::{Hrs:02}:{Min:02}:{Sec:02}, \
v_max = {V:.{2}f} km/s / {V/300000:.{3}f} SoL                              ')


# Deceleration
d = d_half
t0, v0, d0 = t, v, d
# Reset time
t = 0

# deceleration loop
while d < d_fin:             # for distance from middle to end
    v = v0 - g               # current speed in m/s
    d = d0 + (v0+v)/2        # total distance in m
    v0, d0 = v, d            # store the previous step values
    t += 1

V, D, AU, LY = prep_values(v, d)       # resize v & d to big values
Sec, Min, Hrs, Day = calc_time(t0+t)   # time in sec-min-hrs-days
print(f' all way:  all_time = {Day:03}::{Hrs:02}:{Min:02}:{Sec:02}, \
distance = {D:.{0}f} km / {AU:.{3}f} au / {LY:.{3}f} ly', " "*30)

# print(f'v = {v} m/s')  velocity can not be equal to zero at finish line
