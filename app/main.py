import datetime
from typing import Annotated
from fastapi import FastAPI, Depends
from sqlmodel import create_engine, select, Session
from app.models import Rol, Usuario, Curso, ListaCurso, Sesion, Asistencia
from fastapi.middleware.cors import CORSMiddleware

origins = ['*']



sql_uri = 'sqlite:///database.db'
connect_args =  {'check_same_thread': False}
engine = create_engine(sql_uri, connect_args=connect_args, echo=True)

def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_credentials= True,
    allow_origins= origins,
    allow_methods=['*'],
    allow_headers=['*']
)

#Endpoints para el estudiante
@app.post('/asistencia/{sesion_id}')
async def asistencia(sesion_id: int, estudiante_id: int, session: SessionDep):
    '''
    Dada una sesion de id: sesion_id y un id de estudiante: estudiante_id:
    coloca como presente a ese estudiante
    '''
    asistencia = session.exec(select(Asistencia).where(Asistencia.sesion_id == sesion_id, Asistencia.estudiante_id == estudiante_id)).first()
    if not asistencia:
        return {'message': 'No es miembro de este curso'}
    if not asistencia.asistencia:
        asistencia.asistencia = True
        session.add(asistencia)
        session.commit()
        return {'message': 'Asistencia actualizada', 'asistencia': asistencia.asistencia}
    return {'message': 'Ya se encuentra presente'}
    

#Endpoints profesor
@app.get('/profesor/{profesor_id}')
async def cursos_profesor(profesor_id: int, session: SessionDep) -> list[Curso]:
    '''
    Obtenemos el listado de cursos de un profesor.
    '''
    cursos = session.exec(select(Curso).where(Curso.profesor_id==profesor_id))
    return cursos

@app.get('/sesiones/{curso_id}')
async def get_sesiones(curso_id: int, session: SessionDep) -> list[Sesion]:
    '''
    Obtenemos el listado de sesiones existentes de un curso
    '''
    sesiones: list[Sesion] = session.exec(select(Sesion).where(Sesion.curso_id == curso_id)).all()
    return sesiones

@app.post('/cursos/nueva_sesion')
async def nueva_sesion(curso_id: int, session: SessionDep) :
    '''
    Dado un curso: curso_id:
        Si no existe una sesion al dia de hoy:
            Crea una sesion.
        En todo caso:
            Devuelve la sesion del curso al dia de hoy, junto con la lista de alumnos.
            Estructura:
            {
                sesion_id: sesion_id
                lista_alumnos: list[alumno_asistencia]
                                alumno_asistencia: {
                                                    nombre_alumno: nombre_alumno
                                                    asistencia: bool
                                                    }
            }
    '''

    nueva_sesion= Sesion(curso_id=curso_id, fecha=datetime.date.today())
    sesion = session.exec(select(Sesion).where(Sesion.curso_id==nueva_sesion.curso_id, Sesion.fecha==nueva_sesion.fecha)).first()
    if not sesion:
        session.add(nueva_sesion)
        session.commit()
        session.refresh(nueva_sesion)
        sesion_id: int = nueva_sesion.id
        estudiantes = session.exec(select(Usuario).join(ListaCurso).where(ListaCurso.curso_id==curso_id))
        for estudiante in estudiantes:
            asistencia = Asistencia(sesion_id=nueva_sesion.id, estudiante_id=estudiante.id)
            session.add(asistencia)
            session.commit()
        print('Nueva sesion ingresada')
    else:
        print('Sesion existente encontrada')
        sesion_id: int = sesion.id

    ret_dict = {
        'sesion_id' : sesion_id,
        'lista_alumnos' : []
    }


    asistencias = session.exec(select(Usuario.nombre, Asistencia.asistencia).join(Usuario).where(Asistencia.sesion_id==sesion_id)).all()
    for estudiante in asistencias:
        al_dict = {
            'nombre_alumno': estudiante[0],
            'asistencia': estudiante[1]
        }
        ret_dict['lista_alumnos'].append(al_dict)
    print(ret_dict)
    return ret_dict

#Endpoints de login
@app.post('/login/')
async def login(username: str, password: str, session: SessionDep):
    usuario = session.exec(select(Usuario).where(Usuario.username == username, Usuario.password==password)).first()
    if not usuario:
        return {'Error': 'Error',
        'rol_id': -1}
    return usuario

#Endpoint de prueba
@app.get('/rol')
async def rol_prueba(session: SessionDep):
    roles = session.exec(select(Rol)).all()
    return roles