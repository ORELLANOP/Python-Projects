__author__ = 'Cátedra de AED'



total_seg = int(input("Ingrese la cantidad de segundos: "))

segundos = total_seg % 60

total_min = total_seg //60

horas = total_min//60

minutos = total_min%60


print( "Horas:", horas)
print( "Minutos:", minutos)
print( "Segundos:", segundos)


"""
horas = int(input("Ingrese las horas: "))
minutos = int(input("Ingrese los minutos: "))
segundos = int(input("Ingrese los segundos: "))

seg_horas = horas * 3600
seg_minutos = minutos * 60

seg_total = seg_horas + seg_minutos + segundos

print("La cantidad total de segundos es: ", seg_total)


"""
