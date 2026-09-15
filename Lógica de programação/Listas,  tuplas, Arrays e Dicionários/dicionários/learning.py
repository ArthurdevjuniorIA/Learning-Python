meu_email = "tutu@gmail.com"
contatos = { "Tutu": "meuemail@gmail.com",
            "Roberto": "emaildoroberto@gmail.com",
            "Pedro" : "emaildopedro@gmail.com",
            "Adalberto" : True,
            "tutu": "oiemail@gmail.com",
            "Tutu": meu_email
}
for item, valor in enumerate(contatos):
    print(valor)
print(contatos["Tutu"])
contatos["Roberto"] = "tuevacilao@gmail.com"
contatos.pop("Pedro")
for key in contatos.keys():
    if key == "Tutu":
        print("Tutu está na lista")