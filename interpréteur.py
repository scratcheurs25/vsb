from fileinput import filename
import time
update = True
uplingne = "1"


variables = {}  # Dictionnaire pour stocker les variables
execute_if_block = False

def interpret_bsharp(code):
    global variables
    global execute_if_block
    global uplingne
    global update
    if code.strip().startswith("draw(") and code.strip().endswith(")"):
        text = code.strip()[5:-1]
        if text in variables:
            value = variables[text]
            print(value)
        else:
           print(code.strip()[6:-2])
    elif code.strip().startswith("txt(") and code.strip().endswith(")"):
        text = code.strip()[4:-1]
        if text in variables:
            value = variables[text]
            input(value)
        else:
            input(code.strip()[5:-2])
    elif "=" in code and not "-=" in code and not "!=" in code:
        variable, value = code.split("=")
        variable = variable.strip()
        value = value.strip()
        if value.strip().startswith("txt(") and value.strip().endswith(")"):
                text = value.strip()[4:-1]
                variables[variable] = input(value.strip()[5:-2])
        elif value.strip().startswith("ctxt(") and value.strip().endswith(")"):
            if execute_if_block:
                text = value.strip()[5:-1]
                variables[variable] = input(value.strip()[6:-2])
        else:
            variables[variable] = value
    elif code.strip().startswith("wt(") and code.strip().endswith(")"):
        duration = code.strip()[3:-1]
        try:
            duration = float(duration)
            time.sleep(duration)
        except ValueError:
            print("Erreur : Durée invalide")
    elif code.strip().startswith("//") and code.strip().endswith("\\"):
        pass
    elif code.strip().startswith("if {") and code.strip().endswith("}:"):
        condition = code.strip()[4:-2]
        if "=-=" in condition:
            val,valuee = condition.split("-=")
            valuee = valuee + "x"
            valuev = valuee.strip()[0: -1]
            value = variables[val.strip()[0:-2]]

            if value == valuev:
                execute_if_block = True
            else:
                execute_if_block = False
        if "=!=" in condition:
            val,valuee = condition.split("!=")
            valuee = valuee + "x"
            valuev = valuee.strip()[0: -1]
            value = variables[val.strip()[0:-2]]

            if value != valuev:
                execute_if_block = True
            else:
                execute_if_block = False
    elif code.strip().startswith("cdraw(") and code.strip().endswith(")"):
        text = code.strip()[6:-1]
        if execute_if_block == True:
            if text in variables:
                value = variables[text]
                print(value)
            else:
                print(code.strip()[7:-2])
    elif code.strip().startswith("cif {") and code.strip().endswith("}:"):
        condition = code.strip()[5:-2]
        if execute_if_block:
            if "=-=" in condition:
                val,valuee = condition.split("-=")
                valuee = valuee + "x"
                valuev = valuee.strip()[0: -1]
                value = variables[val.strip()[0:-2]]

                if value == valuev:
                    execute_if_block = True
                else:
                    execute_if_block = False
            if "=!=" in condition:
                val,valuee = condition.split("!=")
                valuee = valuee + "x"
                valuev = valuee.strip()[0: -1]
                value = variables[val.strip()[0:-2]]

                if value != valuev:
                    execute_if_block = True
                else:
                    execute_if_block = False
    elif code.strip().startswith("ctxt(") and code.strip().endswith(")"):
        if execute_if_block:
            text = code.strip()[5:-1]
            if text in variables:
                value = variables[text]
                input(value)
            else:
                input(code.strip()[6:-2])
    elif code.strip().startswith("cwt(") and code.strip().endswith(")"):
        duration = code.strip()[4:-1]
        try:
            duration = float(duration)
            time.sleep(duration)
        except ValueError:
            print("Erreur : Durée invalide")
    elif code.strip() == "end;":
        # Code pour marquer la fin du bloc "if"
        execute_if_block = False
    elif code.strip().startswith("update(") and code.strip().endswith(")"):
        text = code.strip()[7:-1]
        time.sleep(0.02)
        uplingne = text
        update = True
        

        


def interpret_bsharp_file(filename):
    global uplingne
    global update
    start_line = int(uplingne)
    with open(filename, "r") as file:
        lines = file.readlines()
    if update == True:
        for i in range(start_line - 1, len(lines)):
            line = lines[i]
            interpret_bsharp(line)
            update = False


filename = "main.b#"
if filename:
    # Exécuter le fichier .b# spécifié
    while True:
        interpret_bsharp_file(filename)