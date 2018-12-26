opcoes = {
	"vertebrado":{
		"ave":{
			"carnivoro": "aguia",
			"onivoro": "pomba",
		},
		"mamifero":{
			"onivoro": "homem",
			"herbivoro": "vaca",
		}
	},
	"invertebrado":{
		"inseto":{
			"hematofago": "pulga",
			"herbivoro": "lagarta",
		},
		"anelideo":{
			"hematofago": "sanguessuga",
			"onivoro": "minhoca",
		}
	}
}


a = input()
b = input()
c = input()

print(opcoes[a][b][c])