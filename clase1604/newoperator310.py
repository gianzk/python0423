
## nueva structura de 3.10 en adelante 
opcion=1 # opcion 

match opcion:
    case 1:
        print("action 1")
    case 2:
        print("action 2")
    case 3:
        print("action 3")
    case _:
        print("action default")

""" match subject:
    case <pattern_1>:
        <action_1>
    case <pattern_2>:
        <action_2>
    case <pattern_3>:
        <action_3>
    case _:
        <action_wildcard> """