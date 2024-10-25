import datetime
from sqlmodel import Field, SQLModel
#Modelos usados para el rol del usuario

class Rol(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    nombre_rol: str

#Modelos correspondientes al usuario

class Usuario(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    password: str
    username: str = Field(index=True)
    nombre: str
    correo: str

    rol_id: int | None = Field(default=None, foreign_key=("rol.id"))

#Modelos respecto a cada curso

class Curso(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    profesor_id: int = Field(foreign_key='usuario.id')
    nombre: str

class ListaCurso(SQLModel, table=True):
    curso_id: int | None = Field(default=None, foreign_key='curso.id', primary_key=True)
    estudiante_id: int | None = Field(default=None, foreign_key='usuario.id', primary_key=True)

class Sesion(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    curso_id: int | None = Field(default=None, foreign_key='curso.id')
    fecha: datetime.date

class Asistencia(SQLModel, table=True):
    sesion_id: int | None = Field(default=None, primary_key=True, foreign_key='sesion.id')
    estudiante_id: int | None = Field(default=None, primary_key=True, foreign_key='usuario.id')
    asistencia: bool = Field(default=False)