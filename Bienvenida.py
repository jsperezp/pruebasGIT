nombre = "Jhonatan"
apellido = "Perez"
edad = 33
name = input("Ingrese su nombre: ")
anioNacimiento = input("Ingrese su año de nacimiento: ")
mesNacimiento = input("Ingrese su mes de nacimiento: ")
diaNacimiento = input("Ingrese su día de nacimiento: ")
salario = input("Ingrese su salario: ")

anio = int(anioNacimiento)
mes = int(mesNacimiento)
dia = int(diaNacimiento)
nroSalarios = int(salario)//877803

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
print("La cantidad de Salarios minimos es:", nroSalarios);
print("\n");
print("Nro", "\t", "Cantidad");

for i in range(1, nroSalarios+1):
	print(i, "\t", 877803 * i)
	