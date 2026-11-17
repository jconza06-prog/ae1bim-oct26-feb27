from sqlalchemy import create_engine, or_
from sqlalchemy.orm import sessionmaker

from configuracion import cadena_base_datos
from crear_base_entidades import Consultorio, HistoriaClinica

engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

# Ejem1: Consultorios cuya especialidad sea 'Cirugía' O 'Dermatología'
print("--- CONSULTORIOS DE CIRUGÍA O DERMATOLOGÍA (or_) ---")
consultorios_esp = session.query(Consultorio).filter(
    or_(
        Consultorio.especialidad == "Cirugía",
        Consultorio.especialidad == "Dermatología"
    )
).all()

for c in consultorios_esp:
    print(c)

# Ejem2: Historias clínicas donde la mascota se llame 'Max' O 'Luna'
print("\n--- HISTORIAS CLÍNICAS DE LAS MASCOTAS 'Max' O 'Luna' ---")
historias_mascotas = session.query(HistoriaClinica).filter(
    or_(
        HistoriaClinica.nombre_mascota == "Max",
        HistoriaClinica.nombre_mascota == "Luna"
    )
).all()

for h in historias_mascotas:
    print(h)
