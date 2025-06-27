def read_file_to_dict(filename):
    try:
        with open(filename, 'r') as file:
            data = {}
            for line in file:
                line = line.strip()
                if not line:
                    continue
                items = line.split(';')
                for item in items:
                    if ':' not in item or not item.strip():
                        continue 
                    product, value = item.split(':')
                    value = float(value)
                    if product not in data:
                        data[product] = []
                    data[product].append(value)
            return data
    except FileNotFoundError:
        raise FileNotFoundError(f"El archivo '{filename}' no existe.")

read_file_to_dict('datos.csv')

def process_dict(data):
    """Para cada producto, imprime el total de ventas y el promedio, en el orden natural del diccionario.

    :param data: dict - diccionario a procesar.
    :return: None
    """
    for product, values in data.items():
        total = sum(values)
        promedio = total / len(values)
        print(f"{product}: ventas totales ${total:.2f}, promedio ${promedio:.2f}")
        
    pass


