colegio={
    "name":"colegio1",
    "grades":[1,2,3,4,5],
    "profesores":{
        "profesor1":{
            "listGrades":[1,2,3]
        },
        "profesor2":{
          "listGrades":[4,5]
        }
    },
    "cursos":["python","sql","power bi"],
    "students":[
        {
            "fullname":"alumno1",
            "grade":1,
            "cursos":["python","sql"],
            "notas":{
                "python":[],
                "sql":[]
            }
        },
        {"fullname":"alumno2",
            "grade":2,
            "cursos":["python","power bi"],
            "notas":{
                "python":[],
                "power bi":[]
            }
        }
    ]
}
templateStudents={
    "fullname":"",
    "grade":"",
    "cursos":[],
    "notas":{}
}

msg="""
    1.) agregar alumno nuevo
    2.) agregar profesor 
    3.) agregar nota
    4.) Mostrar sistema
    5.) Salir
"""
def verificarGrado(colegio,grado):
    if grado in colegio["grades"]:
        return True 
    else:
        return False

def agregarAlumno():
    fullname=input('ingrese su nombre completo')
    while True:
        grade=int(input('ingrese el grado'))
        if verificarGrado(colegio,grade) :
            break
    cantidadCursos=int(input("que cantidad de cursos desea agregar"))
    cursosNew=[]
    print(f"""
        la lista de cursos son {colegio['cursos']}
    """)
    for i in range(cantidadCursos):
        curso=input(f'ingrese el curso numero {i}')
        cursosNew.append(curso)
    templateStudents["fullname"]=fullname
    templateStudents["grade"]=grade
    templateStudents["cursos"]=cursosNew
    colegio['students'].append(templateStudents)

def agregarProfesor():
    name=input("nombre de profesor")
    cantidad=int(input("ingrese la cantidad de grados "))
    listGradesNew=[]
    for i in range(cantidad):
        while True:
         grade=int(input(f'ingrese el grado numero{i}'))
         #reutilizacion
         if verificarGrado(colegio,grade) :
                listGradesNew.append(grade)
                break
    colegio["profesores"][name]={"listGrades":listGradesNew}
        
def agregarNota():
    pass
def mostrarSistema():
    print(colegio)

while True:
    print("Bienvenido al sistema escolar")
    print(msg)
    opcion=int(input("elija opcion por realizar"))
    match opcion:
        case 1:
            agregarAlumno()
        case 2:
            agregarProfesor()
        case 3:
            agregarNota()
        case 4:
            mostrarSistema()
            break
        case 5:
            print("Saliendo...")
            break
        case _:
            print("Elija acction correcta")








