from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from configuracion import cadena_base_datos
from crear_base_entidades import Consultorio, HistoriaClinica

engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

# Ejem1: Filtrar consultorios cuya especialidad sea 'Medicina General'
print("--- CONSULTORIOS DE MEDICINA GENERAL (filter) ---")
consultorios_mg = session.query(Consultorio).filter(
    Consultorio.especialidad == "Medicina General"
).all()

for c in consultorios_mg:
    print(c)

# Ejem2: Filtrar historias clínicas usando like() dentro de filter()
print("\n--- HISTORIAS CLÍNICAS CON DIAGNÓSTICO DE 'Control' o 'Chequeo' ---")
historias_control = session.query(HistoriaClinica).filter(
    HistoriaClinica.diagnostico.like("%Control%")
).all()

for h in historias_control:
    print(h)
