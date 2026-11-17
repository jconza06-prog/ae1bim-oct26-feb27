from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Importar configuración y entidades
from configuracion import cadena_base_datos
from crear_base_entidades import Clinica, Consultorio, Veterinario, HistoriaClinica

# Motor y la sesión
engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

# 1. Crear Clínicas
clinica1 = Clinica(
    nombre_comercial="VetCare Quito Norte",
    direccion="Av. Amazonas N34-120, Quito",
    veterinario_responsable="Dr. Carlos Andrade"
)
clinica2 = Clinica(
    nombre_comercial="Hospital Veterinario Guayaquil",
    direccion="Av. Francisco de Orellana Km 4.5, Guayaquil",
    veterinario_responsable="Dra. María Fernanda López"
)
clinica3 = Clinica(
    nombre_comercial="Clínica Animalia Cuenca",
    direccion="Av. Solano 8-45, Cuenca",
    veterinario_responsable="Dr. Andrés Villavicencio"
)

session.add_all([clinica1, clinica2, clinica3])
session.commit()

# 2. Crear Consultorios asociados a cada clínica
cons1 = Consultorio(nombre_numero="Consultorio 101", especialidad="Medicina General", clinica=clinica1)
cons2 = Consultorio(nombre_numero="Consultorio 102", especialidad="Cirugía", clinica=clinica1)
cons3 = Consultorio(nombre_numero="Consultorio 201", especialidad="Dermatología", clinica=clinica2)
cons4 = Consultorio(nombre_numero="Consultorio 301", especialidad="Medicina General", clinica=clinica3)

session.add_all([cons1, cons2, cons3, cons4])
session.commit()

# 3. Crear Veterinarios asociados a cada consultorio
vet1 = Veterinario(
    nombres_apellidos="Carlos Alberto Andrade",
    correo="candrade@vetcare.ec",
    licencia="VET-EC-1045",
    consultorio=cons1
)
vet2 = Veterinario(
    nombres_apellidos="Sofía Elena Mendoza",
    correo="smendoza@vetcare.ec",
    licencia="VET-EC-2089",
    consultorio=cons2
)
vet3 = Veterinario(
    nombres_apellidos="María Fernanda López",
    correo="mlopez@hvguayaquil.ec",
    licencia="VET-EC-3112",
    consultorio=cons3
)
vet4 = Veterinario(
    nombres_apellidos="Jorge Luis Cevallos",
    correo="jcevallos@hvguayaquil.ec",
    licencia="VET-EC-3490",
    consultorio=cons3
)
vet5 = Veterinario(
    nombres_apellidos="Andrés Felipe Villavicencio",
    correo="avillavicencio@animalia.ec",
    licencia="VET-EC-4021",
    consultorio=cons4
)

session.add_all([vet1, vet2, vet3, vet4, vet5])
session.commit()

# 4. Crear Historias Clínicas asociadas a los veterinarios
hc1 = HistoriaClinica(
    fecha_atencion="2026-11-02",
    diagnostico="Gastritis aguda por ingesta indebida",
    tratamiento="Dieta blanda y protector gástrico por 5 días",
    nombre_mascota="Max",
    veterinario=vet1
)
hc2 = HistoriaClinica(
    fecha_atencion="2026-11-05",
    diagnostico="Control de vacunación anual",
    tratamiento="Aplicación de vacuna séxtuple y desparasitación",
    nombre_mascota="Luna",
    veterinario=vet1
)
hc3 = HistoriaClinica(
    fecha_atencion="2026-11-08",
    diagnostico="Fractura de fémur derecho",
    tratamiento="Osteosíntesis quirúrgica y reposo absoluto",
    nombre_mascota="Rocky",
    veterinario=vet2
)
hc4 = HistoriaClinica(
    fecha_atencion="2026-11-10",
    diagnostico="Esterilización preventiva",
    tratamiento="Cirugía ambulatoria y antibiótico oral por 7 días",
    nombre_mascota="Mia",
    veterinario=vet2
)
hc5 = HistoriaClinica(
    fecha_atencion="2026-11-11",
    diagnostico="Dermatitis alérgica por pulgas",
    tratamiento="Baño medicado y antiparasitario externo",
    nombre_mascota="Toby",
    veterinario=vet3
)
hc6 = HistoriaClinica(
    fecha_atencion="2026-11-12",
    diagnostico="Otitis externa bilateral",
    tratamiento="Limpieza ótica y gotas antiinflamatorias",
    nombre_mascota="Simba",
    veterinario=vet4
)
hc7 = HistoriaClinica(
    fecha_atencion="2026-11-14",
    diagnostico="Infección respiratoria leve",
    tratamiento="Nebulizaciones y jarabe mucolítico",
    nombre_mascota="Kira",
    veterinario=vet5
)
hc8 = HistoriaClinica(
    fecha_atencion="2026-11-15",
    diagnostico="Chequeo geriátrico general",
    tratamiento="Suplemento articular y control nutricional",
    nombre_mascota="Bruno",
    veterinario=vet1
)

session.add_all([hc1, hc2, hc3, hc4, hc5, hc6, hc7, hc8])
session.commit()

print("Datos ingresados correctamente en la base de datos.")
