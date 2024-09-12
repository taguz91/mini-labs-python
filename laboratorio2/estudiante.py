from exceptions import StudentNotFoundException

# declare static data
data = {
    'Daniel': ['Matematica', 'Computacion'],
    'Maria': ['Matematica', 'Fisica']
}

def devolver_materias(student: str) -> list:
    if student not in data.keys():
        raise StudentNotFoundException()
    
    return data[student]