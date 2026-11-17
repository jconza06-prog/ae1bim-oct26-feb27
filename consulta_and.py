from sqlalchemy import create_engine, and_
from sqlalchemy.orm import sessionmaker

from configuracion import cadena_base_datos
from crear_base_entidades import Consultorio, HistoriaClinica

engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

# Ejem1: Consultorios de la clínica 1 Y que sean de especialidad 'Cirugía'
print("--- CONSULTORIOS DE LA CLÍNICA 1 Y ESPECIALIDAD CIRUGÍA (and_) ---")
consultorios_and = session.query(Consultorio).filter(
    and_(
        Consultorio.clinica_id == 1,
        Consultorio.especialidad == "Cirugía"
    )
).all()

for c in consultorios_and:
    print(c)

# Ejem2: Historias clínicas atendidas por el veterinario 1 Y en fecha '2026-11-02'
print("\n--- HISTORIAS CLÍNICAS DEL VETERINARIO 1 Y FECHA 2026-11-02 ---")
historias_and = session.query(HistoriaClinica).filter(
    and_(
        HistoriaClinica.veterinario_id == 1,
        HistoriaClinica.fecha_atencion == "2026-11-02"
    )
).all()

for h in historias_and:
    print(h)
