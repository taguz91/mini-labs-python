import estudiante

def estudiante_registrado_en_materia(student: str, subject: str) -> bool:
    subjects = estudiante.devolver_materias(student)
    
    return subject in subjects