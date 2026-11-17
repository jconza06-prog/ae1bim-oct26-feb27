from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

# Importar cadena_base_datos desde configuracion.py
from configuracion import cadena_base_datos

# Motor de base de datos
engine = create_engine(cadena_base_datos)

# Clase base para los modelos
Base = declarative_base()

class Clinica(Base):
    __tablename__ = 'clinica'

    id = Column(Integer, primary_key=True)
    nombre_comercial = Column(String(100), nullable=False)
    direccion = Column(String(200), nullable=False)
    veterinario_responsable = Column(String(100), nullable=False)

    # Relación: Una clínica tiene muchos consultorios
    consultorios = relationship("Consultorio", back_populates="clinica")

    def __repr__(self):
        return (f"Clinica: id={self.id}, nombre_comercial='{self.nombre_comercial}', "
                f"direccion='{self.direccion}', veterinario_responsable='{self.veterinario_responsable}'")


class Consultorio(Base):
    __tablename__ = 'consultorio'

    id = Column(Integer, primary_key=True)
    nombre_numero = Column(String(50), nullable=False)
    especialidad = Column(String(100), nullable=False)

    # Llave foránea hacia Clinica
    clinica_id = Column(Integer, ForeignKey('clinica.id'), nullable=False)

    # Relaciones
    clinica = relationship("Clinica", back_populates="consultorios")
    veterinarios = relationship("Veterinario", back_populates="consultorio")

    def __repr__(self):
        return (f"Consultorio: id={self.id}, nombre_numero='{self.nombre_numero}', "
                f"especialidad='{self.especialidad}', clinica_id={self.clinica_id}")


class Veterinario(Base):
    __tablename__ = 'veterinario'

    id = Column(Integer, primary_key=True)
    nombres_apellidos = Column(String(150), nullable=False)
    correo = Column(String(100), nullable=False)
    licencia = Column(String(50), nullable=False)

    # Llave foránea hacia Consultorio
    consultorio_id = Column(Integer, ForeignKey('consultorio.id'), nullable=False)

    # Relaciones
    consultorio = relationship("Consultorio", back_populates="veterinarios")
    historias_clinicas = relationship("HistoriaClinica", back_populates="veterinario")

    def __repr__(self):
        return (f"Veterinario: id={self.id}, nombres_apellidos='{self.nombres_apellidos}', "
                f"correo='{self.correo}', licencia='{self.licencia}', consultorio_id={self.consultorio_id}")


class HistoriaClinica(Base):
    __tablename__ = 'historia_clinica'

    id = Column(Integer, primary_key=True)
    fecha_atencion = Column(String(50), nullable=False)
    diagnostico = Column(String(250), nullable=False)
    tratamiento = Column(String(250), nullable=False)
    nombre_mascota = Column(String(100), nullable=False)

    # Llave foránea hacia Veterinario
    veterinario_id = Column(Integer, ForeignKey('veterinario.id'), nullable=False)

    # Relación
    veterinario = relationship("Veterinario", back_populates="historias_clinicas")

    def __repr__(self):
        return (f"HistoriaClinica: id={self.id}, fecha_atencion='{self.fecha_atencion}', "
                f"diagnostico='{self.diagnostico}', tratamiento='{self.tratamiento}', "
                f"nombre_mascota='{self.nombre_mascota}', veterinario_id={self.veterinario_id}")


# Crear todas las tablas en la base de datos SQLite
if __name__ == '__main__':
    Base.metadata.create_all(engine)
    print("Base de datos y tablas creadas correctamente.")
