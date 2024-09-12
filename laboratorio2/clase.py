import estudiante

def estudiante_registrado_en_materia(student, subject):
    subjects = estudiante.devolver_materias(student)
    
    return subject in subjects