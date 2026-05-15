meme_dict = {
    "BISCOITAR": "fazer algo apenas para chamar a atenção",
    "HATER": "pessoa que está constantemente criticando os outros",
    "VDD": "abreviação de verdade",
    "VLW": "abreviação de valeu",
    "TANKO": "aguentar ou segurar algo",
    "CRINGE": "Algo vergonhoso ou constrangedor",
    "STALKEAR": "Investigar a vida de alguém online"
}

word = input("Digite uma palavra moderna que você não entende: ")

word = word.upper()

if word in meme_dict.keys():
    print(meme_dict[word])

else:
    print("A palavra não foi encontrada")
