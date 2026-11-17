from sqlalchemy import create_engine, desc
from sqlalchemy.orm import sessionmaker

from configuracion import cadena_base_datos
from crear_base_entidades import Veterinario, HistoriaClinica

engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

# Ejem1: Ordenar veterinarios alfabéticamente (ascendente)
print("--- VETERINARIOS ORDENADOS POR NOMBRE ASCENDENTE (order_by) ---")
veterinarios_ordenados = session.query(Veterinario).order_by(
    Veterinario.nombres_apellidos
).all()

for v in veterinarios_ordenados:
    print(v)

# Ejem2: Ordenar historias clínicas por fecha más reciente (descendente)
print("\n--- HISTORIAS CLÍNICAS ORDENADAS POR FECHA DESCENDENTE ---")
historias_ordenadas = session.query(HistoriaClinica).order_by(
    desc(HistoriaClinica.fecha_atencion)
).all()

for h in historias_ordenadas:
    print(h)
