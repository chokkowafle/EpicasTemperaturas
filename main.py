from typing import List

class AnalizadorVentas:
  def __init__(
      self,
      dias:int=7,
      meta_semanal:float=50000.0
      ):
    self.dias=dias
    self.meta_semanal=meta_semanal
    self.ventas:List[float]=[]
  def solicitar_ventas(self):
    print("Ingreso de ventas diarias\n")
    for dia in range(1,self.dias+1):
      while True:
        try:
          entrada=input(f"Ingrese la venta del dia {dia}: $")
          venta=float(entrada)
          if venta <0:
            raise ValueError("La venta no puede ser negativa")
          self.ventas.append(venta)
          break
        except ValueError as e:
          print(f"entrada no valida: {e}")

def main():
  analizador=AnalizadorVentas()
  analizador.solicitar_ventas()
if __name__ == "__main__":
  main()