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

String monthName;

switch(mes){
	case 1: monthName = 'Enero';
			break;
	case 2: monthName = 'Febrero';
			break;
	case 3: monthName = 'Marzo';
			break;
	case 4: monthName = 'Abril';
			break;
	case 5: monthName = 'Mayo';
			break;
	case 6: monthName = 'Junio';
			break;
	case 7: monthName = 'Julio';
			break;
	case 8: monthName = 'Agosto';
			break;
	case 9: monthName = 'Septiembre';
			break;			
	case 10: monhtName = 'Octubre';
			break;
	case 11: monthName = 'Noviembre';
			break;
	case 12: monthName = 'Diciembre';
			break;
	default: monthName = 'Mes Invalido';
			break;
}
print("Bienvenido",name);
print("Usted tiene",2020-anio,"años",7-mes,"meses y",15-dia,"días");
print("Nacio en el mes de",monthName);