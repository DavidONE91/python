# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 19:24:14 2019

@author: CEC
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 12:13:57 2019

@author: CEC
"""
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 12:13:57 2019

@author: CEC
"""

info1=input("Ingrese su Nombre: ")
info2=input("Ingrese su Apellido: ")
info3=input("Ingrese su Ciudad natal: ")
info4=input("Ingrese su Edad: ")
info4=int(info4)
if info4<=25:
    print("Usted es demasiado joven")
elif info4>25 and info4<=40:
    print("Usted es joven")
else:
    print("Usted ya no es joven")
space=" "
print("Bienvenido"+space+info1+space+info2+space+"al curso de Python ofertado en su ciudad natal:"+space+info3+space+", donde encontrará gente de su edad:"+space+info4+space+"años, así como de otras edades.Sea bienvenido!")