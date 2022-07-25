"""Tá meio bugada saporra ainda...
#Mas podem brincar à vontade.
#Não tem erro, só tem que instalar o textblob e o NaiveBayesClassifier
#Comando: pip install textblob 
#:        pip install NaiveBayesClassifier
Tico, é bem intuitivo, vc consegue ensinar a Jaque a usar o Python, qualquer coisa, eu ensino.

OBS: Acho que preciso treinar o classificador com senteças mais curtas.
"""

from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier

frases = [('Cloroquina tem potencial in vitro para curar covid-19.','pos'),
	 ('Cloroquina causa falência hepática.','neg'),
	 ('Da cloroquina, se fez hidroxicloroquina.','pos'),
	 ('A hidroxicloroquina é uma versão com menos efeitos colaterais.','pos'),
	 ('Viu-se que cloroquina e hidroxicloroquina possuem muitos efeitos deletérios em seres humanos.','neg'),
	 ('Hidroxicloroquina aumenta risco de infarto.','neg'),
	 ('Cloroquina aumenta risco de cegueira.','neg'),
	 ('As pesquisas com cloroquina e hidroxicloroquina foram suspensas para covid-19.','pos'),
	 ('A ONU emitiu um relatório sobre a ineficiência da cloroquina e hidroxicloroquina.','pos'),
	 ('Didier Raoult foi um dos principais nomes em defesa da cloroquina e hidroxicloroquina.','neg'),
	 ('Donald Trump disse que os EUA tinham a cura para o covid-19, quando referiu-se à cloroquina.','neg'),
	 ('Pessoas ficaram com hepatite medicamentosa, por conta da cloroquina/hidroxicloroquina.','neg'),
	 ('As vacinas foram desenvolvidas.','pos'),
	 ('As vacinas demonstraram resultados promissores em testes clínicos, randomizados e duplo-cego.','pos'),
	 ('As vacinas possuem período de memória imunológica relativamente curto ou incerto.','neg'),
	 ('Para o problema das vacinas de memória imunológica curta, pode aumentar o número de doses.','pos'),
	 ('Natália Pasternak foi uma crítica ferrenha da cloroquina e tratamento precoce.','pos'),
	 ('Didier Raoult foi obrigado a se retratar após sua defesa à cloroquina.','pos'),
	 ('Átila Iamarino é defensor ferrenho do uso de máscaras.','pos'),
	 ('O Brasil tem um governo crítico das vacinas','neg'),
	 ('Precisamos acreditar na ciência, assim como Trump, Raoult e o governo brasileiro também precisam','pos'),
	 ('A política do governo brasileiro no enfrentamento à covid-19 foi equivocada','neg'),
	 ('Natália Pasternak e Átila Iamarino estão do lado da ciência e do bom-senso','pos')
	 ]

modelo = NaiveBayesClassifier(frases)
frase = input("\nDigite a string: ") 
print(f"\n\nA resposta é: {modelo.classify(frase)}")
