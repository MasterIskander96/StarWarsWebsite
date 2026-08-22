import time
import random
import webbrowser



print("Bienvenido a StarWarsWebsite")

while True:
    time.sleep(2)
    print("Funciones del sitio web:\n"
          "O - Sitio web oficial de Star Wars\n"
          "R - Registro\n"
          "L - Iniciar sesión\n"
          "A - Sobre el sitio web\n"
          "Q - StarWarsQuiz\n"
          "E - Comentarios\n"
          "S - Configuración\n"
          "F - ¿A qué planeta viajas durante las vacaciones?")

    choice = input("Selecciona una función del sitio web")
    if choice == "O":
        print("Cargando...")
        time.sleep(2)
        webbrowser.open("https://www.starwars.com")


    elif choice == "R":
        input("Nombre:")
        print("Tu código:Starwars9791n")
        time.sleep(1)
    elif choice == "Q":
        score = 0
        answer1 = input("1.¿En qué episodio de Star Wars apareció Boba Fett por primera vez?(A-4,B-5,C-2,D-8)")
        if answer1 == "B":
            print("¡Correcto!")
            score += 1
        else:
            print("¡Incorrecto! Respuesta correcta:B")

        answer2 = input("2.¿Quién es Cad Bane?(A-Leñador,B-El Jedi,C-Cazarrecompensas,D-Sitio web)")
        if answer2 == "C":
            print("¡Correcto!")
            score += 1
        else:
            print("¡Incorrecto! Respuesta correcta:C")

        answer3 = input("3.¿Cuántos años tiene Grogu en 2026?(A-55,B-59,C-84,D-53)")
        if answer3 == "D":
            print("¡Correcto!")
            score += 1
        else:
            print("¡Incorrecto! Respuesta correcta:D")

        answer4 = input("4.¿Qué número de clon llevaba el Capitán Rex?(A-CT-5555,B-CT-1409,C-CT-7567,D-CC-2224)")
        if answer4 == "C":
            print("¡Correcto!")
            score += 1
        else:
            print("¡Incorrecto! Respuesta correcta:C")

        answer5 = input(
            "5.¿Quién fue el primer aprendiz del Conde Dooku después de pasarse al lado oscuro?(A-Asajj Ventress,B-General Grievous,C-Ki-Adi-Mundi,D-Kit Fisto)")
        if answer5 == "A":
            print("¡Correcto!")
            score += 1
        else:
            print("¡Incorrecto! Respuesta correcta:A")

        answer6 = input(
            "6.¿Cómo se llamaba el buque insignia de Darth Vader en El Retorno del Jedi?(A-Devastator,B-Executor,C-Eclipse,D-Chimaera)")
        if answer6 == "B":
            print("¡Correcto!")
            score += 1
        else:
            print("¡Incorrecto! Respuesta correcta:B")

        answer7 = input(
            "7.¿Cuál era el nombre original del planeta conocido ahora como Exegol en El Ascenso de Skywalker?(A-Korriban,B-Dathomir,C-Malachor,D-Moraband)")
        if answer7 == "D":
            print("¡Correcto!")
            score += 1
        else:
            print("¡Incorrecto! Respuesta correcta:D")

        answer8 = input(
            "8.¿Cuál era la designación del soldado clon que llegó a ser conocido como el Comandante Cody?(A-CT-7567,B-CC-1119,C-CC-2224,D-CT-1409)")
        if answer8 == "C":
            print("¡Correcto!")
            score += 1
        else:
            print("¡Incorrecto! Respuesta correcta:C")

        answer9 = input(
            "9.¿Cómo se llamaba el antiguo Lord Sith que creó la Regla de Dos?(A-Darth Bane,B-Darth Revan,C-Darth Nihilus,D-Darth Malak)")
        if answer9 == "A":
            print("¡Correcto!")
            score += 1
        else:
            print("¡Incorrecto! Respuesta correcta:A")

        answer10 = input("10.¿Qué Jedi fue responsable de descubrir a los kaminoanos y su ejército de clones?(A-Obi-Wan Kenobi,B-Qui-Gon Jinn,C-Sifo-Dyas,D-Mace Windu)")
        if answer10 == "C":
            print("¡Correcto!")
            score += 1
            print(f"¡Respondiste correctamente {score} de 10 preguntas!")
        else:
            print("¡Incorrecto! Respuesta correcta:C")
            print(f"¡Respondiste correctamente {score} de 10 preguntas!")
            time.sleep(3)


    elif choice == "L":
        name = input("Nombre:")
        code = input("Código:")
        if code == "MasterIskander9602":
            print("Perfil")
            print("------------")
            print("|          |")
            print("|          |")
            print("|          |")
            print("|          |")
            print("------------")
            print("MasterIskander96")
            print("Cargo: Creador del sitio web")
            time.sleep(2)

        elif code == "Starwars9791n":
            print("Perfil")
            print("------------")
            print("|          |")
            print("|          |")
            print("|          |")
            print("|          |")
            print("------------")
            print(f"{name}")
            print("Cargo: Visitante")
            time.sleep(2)

        else:
            print("Nombre o código no válidos")


    elif choice == "A":
        print("========== Sobre el sitio web ==========")
        print("Sitio web: StarWarsWebsite")
        print("Creador: Iskander Abdullayev")
        print("Fecha de creación: 11.08.2026")
        print("Tema: Star Wars")
        print("Versión: 1.0")
        print("StarWarsWebsite es un sitio web creado por fans")
        print("con cuestionarios, juegos e información sobre Star Wars.")
        print("¡Gracias por visitar StarWarsWebsite! 🚀")
        print("===================================")
        time.sleep(5)

    elif choice == "F":
        planets = [
            "Tatooine (donde hay mucha arena)",
            "Coruscant (planeta-ciudad)",
            "Hoth (donde hace mucho frío)",
            "Endor (donde viven los ewoks)"]



        input("Presiona Enter para descubrir dónde ir de vacaciones...")


        planet_name = random.choice(planets)
        print("🚀 Tu nave se dirige al planeta:", planet_name)
        time.sleep(2)

    elif choice == "E":

        clar = input("👍 - Me gusta, 👎 - No me gusta, <")
        if clar == "Me gusta":
            print("Gracias por tu Me gusta")
            print("El sitio web fue creado por Iskander Abdullaev.")

        elif clar == "No me gusta":
            print("Intentaremos hacerlo mejor.")
            print("El sitio web fue creado por Iskander Abdullaev")

        elif clar == "<":
            print("Enlace:")
            print("El sitio web fue creado por Iskander Abdullaev")

        else:
            print("Emoji desconocido")


    elif choice == "S":
        choi = input("========== CONFIGURACIÓN ==========\n"
              "1 - Eliminar cuenta\n"
              "2 - Recargar el sitio\n"
              "3 - Reglas\n"
              "===================================")

        if choi == "1":
            print("Tu cuenta ha sido eliminada.")



        elif choi == "2":
            print("Recargando...")
            time.sleep(3)
            print("El sitio ha sido recargado")


        elif choi == "3":
            print("Reglas:")
            print("1. No uses lenguaje ofensivo.")
            print("2. No hagas spam.")
            print("3. ¡Diviértete con Star Wars!")

        else:
            print("Opción no válida")

    else:
        print("¡Error! Función desconocida")