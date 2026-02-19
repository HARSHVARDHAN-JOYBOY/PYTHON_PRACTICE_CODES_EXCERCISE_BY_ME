class laptop:
    model= "LOQ"
    def __init__(self,model,ram,processor):
        self.model=model
        self.ram=ram
        self.processor=processor

    def get_ram(self):
        return self.ram
    def get_info(self):
        print(f"Laptop model is {self.model} Processor is {self.processor} and uses {self.ram} GB Ram")
       
class GamingLaptop(laptop):
    def __init__(self, model, ram, processor,graficcard):
        super().__init__(model, ram, processor)
        self.graficcard=graficcard

    def get_info(self):
        super().get_info()
        print(f"This is gaming laptop and uses {self.graficcard} dedicated Grafic card")

        



l1= GamingLaptop("Legion 5 pro",16,"Ryzen 7 5800H","RTX 3060")
# l1= laptop(16,"Ryzen 7 5800H")           
# print(l1.get_ram())
print(l1.get_info())
# print(dir(l1))