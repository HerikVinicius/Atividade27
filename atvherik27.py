frase = str(input('Digite um nome'))
frase = frase.upper().replace(" ","") #tratando ela 
#inverter a palavra e tratar ela 
invertido = frase.upper() [::-1] # inverter a string com [::-1] 
invertido = invertido.replace(" ", "") # removo qulquer espaço que tenha 
frase = frase.upper().replace(" ","") 
invertido = frase.upper() [::-1] 
# .upper() - transforma todos os textos minusculos em maiusculos. 
# [::-1] -> termo para inverter a string
invertido = invertido.replace(" ", "") # .replace() faz com que subistitua o primeiro item pelo segundo, por exemplo nessa linha estou subistituindo qualquer "espaço" por "nada" .replace(" ", "")

#aqui faço o processo de compraração entre as duas Strings 
if frase == invertido:
    print("palíndromo")
else:
    print("nao é um palindromo")