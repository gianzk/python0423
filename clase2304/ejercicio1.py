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

print(colegio)
print(colegio["students"])

msg="registrando estudiante nuevo"

fullname=input('ingrese su nombre completo')
grade=int(input('ingrese el grado'))
curso=input('ingrese los cursos')
templateStudents={
    "fullname":"",
    "grade":"",
    "cursos":[],
    "notas":{}
}

templateStudents["fullname"]=fullname
if grade in colegio["grades"]:
    templateStudents['grade']=grade
else:
    print("ingrese un valor correcto ")
templateStudents['cursos'].append(curso)
colegio['students'].append(templateStudents)
print(colegio)

