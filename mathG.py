from math import *

G = 6.67408 * 10**-11
KILOTON = 4.184 * 10**12 # J
MEGATON = 4.184 * 10**15 # J

def culcSphereOfInfluence(a, m, M,):
    r = a * ((m) / (M))**(2/5)
    return r

def culcAttractiveForce(m1,m2,r):
    F = G * ((m1*m2)/((r**2)*10**6))
    return F

def culcAcceleration(g, R, r):
    G2 = 6.67408 * 10**-20
    M = (g/1000 * R**2) / G2
    print("1 mass ", M, "kg")
    M = (g * (R * 10**3)**2) / G
    print("2 mass ", M, "kg")
    M = (g/1000 * R**2) / G     # / 10^9 
    print("3 mass ", M, "kg")
    M = (g * R**2) / G      # / 10^6
    print("4 mass ", M, "kg")
    G3 = 0.0001
    M = (g * R**2) / G3     # his / 6,67408 * 10^12
    print("5 mass ", M, "kg")
    a = (G * M) / R
    print("acceleration strange ", a, "m3/s2 km")
    a = (G * M) / R * 10**3
    print("acceleration strange 2 ", a, "m2/s2")
    a = (G * M) / (R * 10**3)**2
    print("acceleration normal ", a, "m/s2")
    G2 = 6.67408 * 10**-20
    a = ((G2  * M) / R**2)
    print("acceleration normal km ", a, "km/s2")
    return a

def culcFirstSpaceSpeed(M,R,h):
    #v1 = ((G * M)/(R + h))**(1/2)
    v1 = ((G * (M/((R + h) * 10**3)))**(1/2))/10**3
    return v1

def culcOrbitSpeed(M,R):
    #v1 = ((G * M)/(R + h))**(1/2)
    v1 = ((G * M) / R * 10**3)**(1/2)
    return v1 / 10**3

def culcKineticEnergyMaaterialPoint(m,v):
    Ek = (m * (v * 10**3)**2)/2   # km/s to m/s
    return Ek

def culcKineticEnergyHardBody(v,p,d):
    Ek = pi / 12 * (p * d**3 * (v * 10**3)**2)
    return Ek

def culcTNTEquivalentKT(Ek):
    Qt = Ek / KILOTON   # J
    return Qt

def culcTNTEquivalentMT(Ek):
    Qt = Ek / MEGATON   # J
    return Qt

def culcCraterRadius(v, pm, pt, g, rm):
    dp = pm / pt
    r = (((((v * 10**3)**2) / g) * dp )**(1/4)) * rm**(3/4)
    return r

print("**** ", round(culcSphereOfInfluence(149598261, 5.9726*10**24, 1.9885*10**30)))

x1 = ((5.9726*10**24) / (1.9885*10**30))**(2)
print("1 = ", x1)

x2 = (x1)**(1/5)
print("2 = ", x2)

x3 = 149598261 * x2
print("3 = ", x3)

x = 57909227 * ((3.33022*10**23) / (1.9885*10**30))**(2/5)
print("\nMercury ", round(x), "km")

x = round(culcSphereOfInfluence(108208930, 	4.8675*10**24, 1.9885*10**30))
print("Venus ", x, "km")

x = 149598261 * ((5.9726*10**24) / (1.9885*10**30))**(2/5)
print("Earth ", round(x), "km")

x = round(culcSphereOfInfluence(2.2794382*10**8 , 	6.4171*10**23, 1.9885*10**30))
print("Mars ", x, "km")

x = round(culcSphereOfInfluence(7.785472*10**8 , 1.8986*10**27, 1.9885*10**30))
print("Jupiter ", x, "km")

x = culcAttractiveForce(1.9885*10**30 , 3.33022*10**23 , 58000000)
print("F ", x, "N")

x = culcAttractiveForce(1000 , 3.33022*10**23 , 140000)
print("F Mercury ", x, "N")

x = culcFirstSpaceSpeed(5.9726*10**24 , 6371 , 0)
print("\nv1 ", x, "km/s")

x = culcFirstSpaceSpeed(5.9726*10**24 , 6371 , 35786)
print("\nv1 ", x, "km/s")

x = culcKineticEnergyMaaterialPoint(6.1 * 10**10 , 12.6)
print("\nEk ", x, "J")
print("\nEk ", culcTNTEquivalentMT(x), "mt")

x = culcKineticEnergyHardBody(12.6, 3000,270)
print("\n2Ek ", x, "J")
print("\nEk ", culcTNTEquivalentMT(x), "mt")

x = culcKineticEnergyHardBody(17, 2600,100)
print("\n3Ek ", x, "J")
print("\n3Ek ", culcTNTEquivalentMT(x), "mt")

x = culcCraterRadius(17, 2600, 5520, 9.8, 100)
print("\nR ", x, "m")

x1 = culcOrbitSpeed(1.9885*10**30, 147098290)
x2 = culcOrbitSpeed(1.9885*10**30, 152098232)
x = (x1+x2)/2
print("\nv ", x, "km/s")

x = culcAcceleration(3.7, 2439, 8382)

x = culcAcceleration(3.7, 243.9, 8382)

x = culcAcceleration(274, 6963, 8382)

x = round(culcSphereOfInfluence(147098290 ,5.9726*10**24, 1.9885*10**30))
print("Earth ", x, "km")
#print("\nEk ", format((x/4184), ".4e"), "kt")
#print("\nEk ", format(culcTNTEquivalent(x), ".4e"), "kt")

#x = (culcSphereOfInfluence(8.5 * 3.0856776*10**19, 1.9885*10**30, 1.9885*10**30 * 4.297*10**6))
#print("SUN ", x, "km")

#x = culcAttractiveForce(1.9885*10**30 * 4.297*10**6 , 3.33022*10**23 , 8.5 * 3.0856776*10**19)
#print("F sun ", x, "N")



