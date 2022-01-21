class India:
    def capital(self):
        print("New Delhi is the capital of india")

    def language(self):
        print("Hindi and English")

class USA:
    def capital(self):
        print("Washington, D.C")

    def language(self):
        print("English")

ind = India()
usa = USA()
for country in (ind, usa):
    country.capital()
    country.language()
