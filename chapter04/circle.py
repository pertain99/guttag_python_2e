pi = 3.14159264758

def area(radius):
    return pi*(radius**2)

def circumference(radius):
    return 2.0*pi*radius

def sphereSurface(radius):
    return 4.0*area(radius)

def sphereVolume(radius):
    return (4.0/3.0)*pi*(radius**3)