class QuantityError(Exception):
    def __init__(self,*args,**kwargs):
        self.message = args[0] if args else "Неверное количество товара"
    def __str__(self):
        return f"{self.message}"
        