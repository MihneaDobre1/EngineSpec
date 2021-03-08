import math

d = float(input("Diametru:"))

s = float(input("Cursa:"))
i = int(input("Numar cilindri:"))
Pe = int(input("Putere in kW:"))
rpm = int(input("Turatie: "))
Vt = (math.pi * math.pow(d,2))/4 * s *  0.000001 * i
Pl = Pe/Vt
Ps = (4 * math.pow(10,4) * Pe) / (i* math.pi * math.pow(d,2))
PeMPa = (30 * 4 * Pe) / (0.1*Vt*i*rpm)
wp = s*rpm/30* math.pow(10,-3)

print("Cilindree totala: "+str(Vt))
print("Puterea litrica: "+str(Pl))
print("Puterea specifica: "+str(Ps))
print("Puterea efectiva in MPa: "+str(PeMPa))
print("Viteza pistonului: "+str(wp))


