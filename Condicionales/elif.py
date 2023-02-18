ingreso_mensual = 72000
gasto_mensual = 80000

# if anidado y else if (elif)

if ingreso_mensual > 10000:
    if ingreso_mensual - gasto_mensual < 3000:
        print("Estas bien en cualquier parte del mundo")
    elif ingreso_mensual - gasto_mensual > 3000:
        print("Bien pa estas bien")
    else:
        print("Na loco, estas gastando una banda de plata, disminuyele a los tamales")
    
elif ingreso_mensual > 1000:
    print("Estas bien economicamente en latinoamerica")
    
elif ingreso_mensual > 500:
    print("Estas bien economicamente en argentina")
    
elif ingreso_mensual > 200:
    print("Estas bien economicamente en venezuela")
    
else: 
    print("Eres bien pobre")