class Human:

    default_name = 'No name'
    default_age = 0

    def __init__(self, name=default_name, age=default_age):
        self.name = name
        self.age = age
        self.__money = 0
        self.__house = None

    def info(self):
        print(f"Buyer's name is {self.name}")
        print(f"Buyer's age is {self.age}")
        print(f"Amount of money: {self.__money}")
        print(f"House: {self.__house}")

    @staticmethod
    def default_info():
        print(f"Default name: {Human.default_name}")
        print(f"Default age: {Human.default_age}")

    def _make_deal(self, house, price):
        self.__money -= price
        self.__house = house

    def earn_money(self, salary):
        self.__money += salary

    def buy_house(self, house, discount):
        price = house.final_price(discount)
        if self.__money >= price:
            self._make_deal(house, price)
            print("Purchase successfully completed!")
        else:
            print("Not enough money for this house...")


class House:

    def __init__(self, area, price):
        self._area = area
        self._price = price

    def final_price(self, discount):
        final_price = self._price * (100 - discount) / 100
        return final_price


class SmallHouse(House):

    default_area = 40

    def __init__(self, price):
        super().__init__(SmallHouse.default_area, price)


Human.default_info()
Julia = Human("Julia", 20)
Julia.info()
small_house = SmallHouse(5000)
Julia.buy_house(small_house, 3)
Julia.earn_money(10000)
Julia.buy_house(small_house, 3)
Julia.info()
