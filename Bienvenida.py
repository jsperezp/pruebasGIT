nombre = "Jhonatan"
apellido = "Perez"
edad = 33
name = input("Ingrese su nombre: ")
anioNacimiento = input("Ingrese su año de nacimiento: ")
mesNacimiento = input("Ingrese su mes de nacimiento: ")
diaNacimiento = input("Ingrese su día de nacimiento: ")

anio = int(anioNacimiento)
mes = int(mesNacimiento)
dia = int(diaNacimiento)

monthName = '';

def nombreMes(i):
	switcher = {
		1: 'Enero',
		2: 'Febrero',
		3: 'Marzo',				
		4: 'Abril',				
		5: 'Mayo',			
		6: 'Junio',				
		7: 'Julio',				
		8: 'Agosto',				
		9: 'Septiembre',						
		10: 'Octubre',			
		11: 'Noviembre',				
		12: 'Diciembre',			
	}
	return switcher.get(i, "Invalido");	
	
print("Bienvenido",name);
print("Usted tiene",2020-anio,"años",7-mes,"meses y",15-dia,"días");
print("Nacio en el mes de:",nombreMes(mes));