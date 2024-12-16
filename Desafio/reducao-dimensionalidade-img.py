# Função para carregar uma imagem (Em formato PPM para simplificar)
# A função split() no PYTHON dive uma string em uma lista de substrings, ou seja, em elementos que compõem a string original.
# O método readline() lê uma linha de um arquivo de texto e a retorna como uma string.

def load_image(caminho):
	with open(caminho, 'rb') as arquivos:
		# Lendo o cabeçalho do arquivo PPM
		tipo = arquivos.readline().strip # P6
		dimensoes = arquivos.readline().strip() # largura e altura
		print("Dimensões lidas:", dimensoes)   
		max_valor = arquivos.readline().strip # 255

		# Separando largura e altura
		largura, altura = map(int, dimensoes.split())

		# Lendo os pixels da imagem
		dados = arquivos.read() #Bytes RGB

	return largura, altura, dados

# Função para converter para tons de cinza
def convert_tons_de_cinza(largura, altura, dados):
	tons_de_cinza = []
	for i in range(0, len(dados), 3):
		r = dados[i]
		g = dados[i+1]
		b = dados[i+2]

		# Fórmula para cinza
		cinza = int(0.2989 * r + 0.5870 * g + 0.1140 * b)
		tons_de_cinza.append(cinza)

	return tons_de_cinza

# Função para binarizar a imagem
def binarizar_imagem(tons_de_cinza, limiar=128):
	binarizada = []
	for cinza in tons_de_cinza:
		if cinza > limiar:
			binarizada.append(255) # Branco
		else:
			binarizada.append(0) # Preto
	return binarizada

# Função para salvar a imagem (em formato PGM paar simplificar)
def salvar_iamgem(caminho, largura, altura, dados):
	with open(caminho, 'wb') as arquivo:
		# Cabeçalho PGM
		arquivo.write(b"P5\n")
		arquivo.write(f"{largura} {altura}\n".encode())
		arquivo.write(b"255\n")

		# Dados da imagem
		arquivo.write(bytearray(dados))

# Programa principal
if __name__ == "__main__":
	# Caminho da imagem PPM(colorido)
	caminho_imagem = "C:/Users/KaioOliveira/Desktop/Pessoal/Curso-ML/Desafio/Lenna__test_image_.ppm"

	# Carregar a imagem
	largura, altura, dados = load_image(caminho_imagem)

	# Converter para tons de cinza
	tons_de_cinza = convert_tons_de_cinza(largura, altura, dados)

	# Salvar a imagem em tons de cinza
	salvar_iamgem("imagem_cinza.pgm", largura, altura, dados)

	# Converter para binarizada 
	imagem_binarizda = binarizar_imagem(tons_de_cinza)

	# Salvar a imagem binarizada
	salvar_iamgem("imagem_binarizda.pgm", largura, altura, imagem_binarizda)

	print("Processo concluído!")