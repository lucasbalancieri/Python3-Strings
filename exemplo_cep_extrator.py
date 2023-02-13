import re 		# Regular Expressions (RegEx)

endereco = "Rua das Flores 72, Apartamento 1002, Laranjeiras, Rio de Janeiro, RJ, 23440120"

# CEP 5 digitos, hifen (opcional), 3 digitos ex: #####-##
# o ? indica que o conjunto [-] é opcional (pode aparecer nenhuma, ou uma vez)


# padrao = re.compile("[0123456789][0123456789][0123456789][0123456789][0123456789][-]?[0123456789][0123456789][0123456789]")
# padrao = re.compile("[0123456789]{5}[-]?[0123456789]{3}")
# padrao = re.compile("[0-9]{5}[-]?[0-9]{3}")
padrao = re.compile("[0-9]{5}[-]{0,1}[0-9]{3}")


busca = padrao.search(endereco)

if busca:
	cep = busca.group()
	print(cep)