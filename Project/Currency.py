class Currency:

    def __init__(self, currency_code = "USD", toEuroRate = "0.9488", fromEuroRate = "1.0541"):  # I'm using US Dollar as defualt attributes
        self._currency = currency_code
        self._toEuro = float(toEuroRate)
        self._fromEuro = float(fromEuroRate)

    def convert(self, amount):
        if self._currency == "EUR": # No need to convert if true
            return amount
        else:
            amount = amount * self._toEuro  # converts amount to Euro
            return amount
