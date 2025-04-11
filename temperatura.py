def obtener_temperaturas():
    """Introduzca las temperaturas de los últimos 7 dias."""
    temperaturas = []
    for dia in range(1, 8):
        while True:
            try:
                temp = float(input(f"Ingrese la temperatura del día {dia}: "))
                temperaturas.append(temp)
                break
            except ValueError:
                print("Por favor, ingrese un número válido.")
    return temperaturas

def calcular_promedio(temps):
    """Calcula el promedio de temperaturas."""
    return sum(temps) / len(temps)

def encontrar_max_min(temps):
    """Encuentra temperaturas maximas y minimas con sus dias."""
    max_temp = temps[0]
    min_temp = temps[0]
    dias_max = [0]
    dias_min = [0]
    
    for i, temp in enumerate(temps[1:], start=1):
        if temp > max_temp:
            max_temp = temp  
            dias_max = [i]
        elif temp == max_temp:
            dias_max.append(i)
            
        if temp < min_temp:
            min_temp = temp  
            dias_min = [i]
        elif temp == min_temp:
            dias_min.append(i)
            
    return (max_temp, dias_max), (min_temp, dias_min)

def mostrar_alertas(temps):
    """Muestra alertas por temperaturas extremas."""
    alertas = []
    for i, temp in enumerate(temps):
        if temp > 40:
            alertas.append(f"Alerta! Día {i+1}: {temp}°C (Supera los 40°C)")
        elif temp < 0:
            alertas.append(f"Alerta! Día {i+1}: {temp}°C (Bajo cero)")
    
    # Movido fuera del bucle for
    if alertas:
        print("\n".join(alertas))
    else:
        print("No se registraron temperaturas extremas")
            
def formatear_dias(dias):
    """Formatea índices de lista (base 0) a días legibles (base 1)"""
    dias_numeros = [str(d+1) for d in dias]
    if len(dias_numeros) == 0:
        return "ningún día"
    elif len(dias_numeros) == 1:
        return f"día {dias_numeros[0]}"
    else:
        return f"días {', '.join(dias_numeros)}"

def main():
    print("\n" + "="*50)
    print("Bienvenido! Vamos a registrar las temperaturas de los últimos 7 días.")
    print("="*50 + "\n")
    
    temperaturas = obtener_temperaturas()
    promedio = calcular_promedio(temperaturas)
    (max_temp, dias_max), (min_temp, dias_min) = encontrar_max_min(temperaturas)
    
    print("\n" + "-"*50)
    print("RESULTADOS".center(50))
    print("-"*50)
    mostrar_alertas(temperaturas)
    print(f"\nPromedio semanal: {promedio:.2f}°C")
    print(f"Temperatura máxima: {max_temp}°C (días {formatear_dias(dias_max)})")
    print(f"Temperatura mínima: {min_temp}°C (días {formatear_dias(dias_min)})")
    print("="*50 + "\n")
    
    print("Gracias por usar el analizador de temperaturas!")
    print("="*50 + "\n")
    
    # Opción para reiniciar el programa
    while True:
        respuesta = input("¿Desea volver a ejecutar el programa? (s/n): ").lower()
        if respuesta in ('s', 'si'):
            main()  # Reinicia el programa
            break
        elif respuesta in ('n', 'no'):
            print("Programa finalizado.")
            break
        else:
            print("Opción no válida. Por favor ingrese 's' o 'n'")

# Llamada inicial al programa
if __name__ == "__main__":
    main()