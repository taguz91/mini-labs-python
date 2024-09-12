import clase
from exceptions import StudentNotFoundException 

print("---------------------")
print(clase.estudiante_registrado_en_materia('Daniel', 'Matematica'))
print(clase.estudiante_registrado_en_materia('Daniel', 'Pintura'))

try:
    print(
        clase.estudiante_registrado_en_materia('Johnny', 'Matematica')
    )
except StudentNotFoundException:
    print('El estudiante no se registro')