from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from configuracion import cadena_base_datos
from crear_base_entidades import Clinica

engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

# Obtener todas las clínicas usando all()
clinicas = session.query(Clinica).all()

print("--- LISTADO DE CLÍNICAS Y NÚMERO DE HISTORIAS CLÍNICAS ASOCIADAS ---\n")

for clinica in clinicas:
    total_historias = 0
    # Recorrer los consultorios de la clínica y los veterinarios de cada consultorio
    for consultorio in clinica.consultorios:
        for veterinario in consultorio.veterinarios:
            total_historias += len(veterinario.historias_clinicas)

    print(f"Clínica: {clinica.nombre_comercial} (Ciudad/Dirección: {clinica.direccion})")
    print(f"Responsable: {clinica.veterinario_responsable}")
    print(f"Número de Historias Clínicas asociadas: {total_historias}")
    print("-" * 60)
