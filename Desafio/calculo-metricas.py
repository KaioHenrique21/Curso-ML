# Função para calcular Sensibilidade (Recall)
def calcular_sensibilidade(VP, FN):
	if(VP + FN) == 0:
		return 0 # evitar divisão por 0
	return VP / (VP + FN)

# Função para calcular Especifidade
def calcular_especificidade(VN, FP):
	if(FP + VN) == 0:
		return 0 # evitar divisão por 0
	return VN / (FP + VN)

# Função para calcular Acuracia
def calcular_acuracia(VP, VN, N):
	return (VP + VN) / N

# Função para calcular Precisão
def calcular_precisao(VP, FP):
	if(VP + FP) == 0:
		return 0 # evitar divisão por 0
	return VP / (VP + FP)

# Função para calcular F-Score
def calcular_fscore(precisao, sensibilidade):
	if(precisao + sensibilidade) == 0:
		return 0 # evitar divisão por 0
	return 2 * (precisao * sensibilidade) / (precisao + sensibilidade)

# Função para calcular matriz de confusão

def main():
	# Matriz de confusão arbitrária
	matriz_confusao = {
		"VP": 50, # verdadeiros Positivos
		"VN": 40, # verdadeiros Negativo
		"FP": 10, # Falsos Positivos
		"FN": 5   # Falsos Negativo
	}

	# Total de elementos (N)
	N = sum(matriz_confusao.values())

	# Calculando as métricas
	sensibilidade = calcular_sensibilidade(matriz_confusao["VP"], matriz_confusao["FN"])
	especificidade = calcular_especificidade(matriz_confusao["VN"], matriz_confusao["FP"])
	acuracia = calcular_acuracia(matriz_confusao["VP"], matriz_confusao["VN"], N)
	precisao = calcular_precisao(matriz_confusao["VP"], matriz_confusao["FP"])
	fscore = calcular_fscore(precisao, sensibilidade)

	# Exibição dos resultados
	print(f"Sensibilidade: {sensibilidade:.2f}")
	print(f"Especificidade: {especificidade:.2f}")
	print(f"Acuracia: {acuracia:.2f}")
	print(f"Precisão: {precisao:.2f}")
	print(f"F-Score: {fscore:.2f}")

# Execução do programa
if __name__ == "__main__":
	main()
