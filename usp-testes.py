segundos_str = input ("Por favor, entre com o numero de segundos que deseja converter: ")
total_segs = int(segundos_str)

horas = total_segs // 3600
dias = horas // 24
meses = dias // 30
anos = meses // 12
segs_restantes = total_segs % 3600
minutos = segs_restantes // 60
segs_restantes_final = segs_restantes % 60  

print (anos , "ano", meses , "meses" , dias , "dias" , horas ,"horas" , minutos , "minutos e" , segs_restantes_final , " segundos")

