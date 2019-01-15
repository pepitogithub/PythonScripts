def sincomparar(valoringresado,valoracomprar):
	return True

class validador:
	#Clase estatica para realizar validaciones.
	#ejemplos de invocacion:
	# ingresar(int, validador.menor, 3)
	# ingresar(float, validador.mayor, 5)
	# ingresar(complex, validador.entre, 0,3+1j)
	# ingresar(complex, validador.noentre, 0,3+1j)
	# ingresar(str, validador.igual, "asd","3","9","pedro")
	# ingresar(str, validador.distinto, "asd","3","9","pedro")
	respuestasSI = ["S","SI","Y","YES","1",""]
	respuestasNO = ["N","NO","0"]
	
	@staticmethod
	def ingresar(tipo,funcioncomparadora=sincomparar,*valoresacomparar):
	# Funcion para ingresar valores con tipos correctos que cumplan con las condiciones especificadas por funcioncomparadora y valoresacomparar.
		error = True
		while (error):
			error = False
			valoringresado = raw_input("> ")
			
			try:
				valoringresado = tipo(valoringresado)
				
			except (ValueError):
				error = True
			
			else:
				error = not(funcioncomparadora(valoringresado,valoresacomparar))
			
		return valoringresado
	
	@staticmethod
	def ingresarBoolean(tipo,funcioncomparadora=sincomparar,*valoresacomparar):
	# Esta funcion responde si o no a la pregunta: el valor ingresado, del tipo especificado, cumple con las validaciones especificadas?
		error = True
		while (error):
			error = False
			valoringresado = raw_input("> ")
			
			try:
				valoringresado = tipo(valoringresado)
				
			except (ValueError):
				error = True
			
			else:
				return funcioncomparadora(valoringresado,valoresacomparar)
	
	@staticmethod
	def ingresarSINO():
		# Esta funcion es para cuando preguntas si deseea continuar, si responde un si(ver arriba como decir que si) devuelve true, si dice responde un no, devuelve false, si escribio fruta pregunta de nuevo.
		si = False
		no = False
		error = True
		while(error):
			valoringresado = raw_input("> ").upper()
			dijosi = validador.igual(valoringresado, validador.respuestasSI)
			dijono = validador.igual(valoringresado, validador.respuestasNO)
			if(dijosi):
				ret = True
				error = False
				
			if (dijono):
				ret = False		
				error = False
				
		return ret
		
	@staticmethod
	def menor(valoringresado,valoracomprar):
		if(valoringresado < valoracomprar[0]):
			return True
		else:
			return False
	
	@staticmethod
	def menorigual(valoringresado,valoracomprar):
		if(valoringresado <= valoracomprar[0]):
			return True
		else:
			return False
	
	@staticmethod
	def mayor(valoringresado,valoracomprar):
		if(valoringresado > valoracomprar[0]):
			return True
		else:
			return False
			
	@staticmethod
	def mayorigual(valoringresado,valoracomprar):
		if(valoringresado >= valoracomprar[0]):
			return True
		else:
			return False
	
	@staticmethod
	def entre(valoringresado,valoresacomparar):
		if(valoringresado >= valoresacomparar[0] and valoringresado <= valoresacomparar[1]):
			return True
		else:
			return False
			
	@staticmethod
	def noentre(valoringresado,valoresacomparar):
		if(valoringresado < valoresacomparar[0] and valoringresado > valoresacomparar[1]):
			return True
		else:
			return False
			
	@staticmethod
	def igual(valoringresado,valoresacomparar):
		if (type(valoresacomparar[0]) is list):
			valoresc = valoresacomparar[0]
		else:
			valoresc = valoresacomparar
			
		if(valoringresado in valoresc):
			return True
		else:
			return False
			
	@staticmethod
	def distinto(valoringresado,valoresacomparar):
		if (type(valoresacomparar[0]) is list):
			valoresc = valoresacomparar[0]
		else:
			valoresc = valoresacomparar
			
		if(valoringresado not in valoresacomparar):
			return True
		else:
			return False