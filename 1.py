class Soda: 
    def __init__(self,ingredient='Клубника'):
        if isinstance(ingredient,str):
            self.ingredient=ingredient
        else:
            self.ingredient=None
    def show_my_drink(self):
        if self.ingredient:
            print(f'Газировка и {self.ingredient}')
        else:
            print("Обычная газировка")
#main()
a=int(input('Какая газировка вам нужна'))
soda=Soda(ingredient='Клубника')
soda2=Soda(ingredient=None)
if a==1:
    soda.show_my_drink()
elif a==2:
    soda2.show_my_drink()