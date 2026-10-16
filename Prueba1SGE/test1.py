ventas = [
    {"id": "PED-01", "total": 1250.0},
    {"id": "PED-02", "total": 80.0},
    {"id": "PED-03", "total": 3500.0},
    {"id": "PED-04", "total": 100.0},
    {"id": "PED-05", "total": 220.0}
]
 
# 1. Filtrar pedidos relevantes por umbral (devuelve IDs)
def pedidos_relevantes(datos: list[dict], umbral: float) -> list[str]:
    return [str(v['id']) for v in datos if float(v['total']) > umbral]

# 2. Indexar pedidos por ID para búsqueda rápida (ID -> Total)
def indexar_por_id(datos: list[dict]) -> dict[str, float]:
    return {str(v['id']): float(v['total']) for v in datos}

print(pedidos_relevantes(ventas, 200))
print(indexar_por_id(ventas))