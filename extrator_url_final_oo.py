import re


class ExtratorURL:
	def __init__(self, url):
		self.url = self.sanitiza_url(url)
		self.validar_url()

	def sanitiza_url(self, url):
		if type(url) == str:
			return url.strip()
		else:
			return ""

	def validar_url(self):
		if not self.url:
			raise ValueError("A URL está vazia")

		padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
		match = padrao_url.match(self.url)

		if not match:
			raise ValueError ("URL Inválida")

	def get_url_base(self):
		indice_interrogacao = self.url.find('?')
		url_base = self.url[:indice_interrogacao]
		return url_base

	def get_url_parametros(self):
		indice_interrogacao = self.url.find('?')
		url_parametros = self.url[indice_interrogacao+1:]
		return url_parametros

	def get_valor_parametro(self, parametro_busca):
		indice_parametro_busca = self.get_url_parametros().find(parametro_busca)
		indice_valor = indice_parametro_busca + len(parametro_busca) + 1
		indice_e_comercial = self.get_url_parametros().find('&', indice_valor)

		if indice_e_comercial == -1:
			valor = self.get_url_parametros()[indice_valor:]
		else:
			valor = self.get_url_parametros()[indice_valor:indice_e_comercial]
		return valor

	# Desafio	
	def conversao(self, moeda_origem, moeda_destino, quantidade):
		if moeda_origem == 'real' and moeda_destino == 'dolar'and quantidade > 0:
			return quantidade / VALOR_DOLAR
		elif moeda_origem == 'dolar' and moeda_destino == 'real' and quantidade > 0:
			return quantidade * VALOR_DOLAR
		else:
			raise ValueError("Parâmetros Inválidos")
	
	def __len__(self): # retorna o tamanho da url como tamanho do objeto em len(extrator_url)
		return len(self.url)

	def __str__(self): # define como o objeto sera "printado" em print(extrator_url)
		return "URL: " + self.url + "\n" + "Parametros: " + self.get_url_parametros() + "\n" + "Base: " + self.get_url_base()

	def __eq__(self, other): # faz com que o __eq__ não compare os endereços de memória (False) mas sim o conteudo da url dos objetos (True)
		return self.url == other.url


url = "bytebank.com/cambio?quantidade=100&moedaOrigem=dolar&moedaDestino=real"
extrator_url = ExtratorURL(url)

VALOR_DOLAR = 5.20  # 1 dólar = 5.20 reais
moeda_origem = extrator_url.get_valor_parametro("moedaOrigem")
moeda_destino = extrator_url.get_valor_parametro("moedaDestino")
quantidade = extrator_url.get_valor_parametro("quantidade")

conversao = extrator_url.conversao(moeda_origem, moeda_destino, float(quantidade))

print("Quantidade: {:.2f} ({})\nConversão: {:.2f} ({})".format(float(quantidade), moeda_origem, conversao, moeda_destino))

