import time
import random
import webbrowser



print("Welcome to StarWarsWebsite")

while True:
    time.sleep(2)
    print("Website functions:\n"
          "O -  Offical Star Wars Website\n"
          "R - Registration\n"
          "L - Log in\n"
          "A - About website\n"
          "Q - StarWarsQuiz\n"
          "E- Feedback\n"
          "S- Settings\n"
          "F - Where are you flying to for the holidays?")

    choice = input("Select a website function")
    if choice == "O":
        print("Loading...")
        time.sleep(2)
        webbrowser.open("https://www.starwars.com")


    elif choice == "R":
        input("Name:")
        print("Your code:Starwars9791n")
        time.sleep(1)
    elif choice == "Q":
        score = 0
        answer1 = input("1.In which Star Wars episode did Boba Fett first appear?(A-4,B-5,C-2,D-8)")
        if answer1 == "B":
            print("Right!")
            score += 1
        else:
            print("Wrong!Correct answer:B")
        answer2 = input("2.Who is Cad Bane?(A-Lumberjack,B-The Jedi,C-Bounty Hunter,D-Website)")
        if answer2 == "C":
            print("Right!")
            score += 1
        else:
            print("Wrong!Correct answer:C")
        answer3 = input("3.How old is Grogu in 2026?(A-55,B-59,C-84,D-53)")
        if answer3 == "D":
            print("Right!")
            score += 1
        else:
            print("Wrong!Correct answer:D")
        answer4 = input("4.What clone number did Captain Rex wear?(A-CT-5555,B-CT-1409,C-CT-7567,D-CC-2224)")
        if answer4 == "С":
            print("Right!")
            score += 1
        else:
            print("Wrong!Correct answer:C")
        answer5 = input(
            "5.Who was Count Dooku's first apprentice after he turned to the dark side?(A-Asajj Ventress,B-General Grievous,C-Ki-Adi-Mundi,D-Kit Fisto)")
        if answer5 == "A":
            print("Right!")
            score += 1
        else:
            print("Wrong!Correct answer:A")
        answer6 = input(
            "6.What was the name of Darth Vader's flagship in Return of the Jedi?(A-Devastator,B-Executor,C-Eclipse,D-Chimaera)")
        if answer6 == "B":
            print("Right!")
            score += 1
        else:
            print("Wrong!Correct answer:B")
        answer7 = input(
            "7.What was the original name of the planet now known as Exegol's Sith world in The Rise of Skywalker?(A-Korriban,B-Dathomir,C-Malachor,D-Moraband)")
        if answer7 == "D":
            print("Right!")
            score += 1
        else:
            print("Wrong!Correct answer:D")
        answer8 = input(
            "8.What was the designation of the clone trooper who became known as Commander Cody?(A-CT-7567,B-CC-1119,CCC-2224-,D-CT-1409)")
        if answer8 == "С":
            print("Right!")
            score += 1
        else:
            print("Wrong! Correct answer:С")
        answer9 = input(
            "9.What was the name of the ancient Sith Lord who created the Rule of Two?(A-Darth Bane,B-Darth Revan,C-Darth Nihilus,D-Darth Malak)")
        if answer9 == "A":
            print("Right!")
            score += 1
        else:
            print("Wrong! Correct answer:A")

        answer10 = input("10.Which Jedi was responsible for discovering the Kaminoans and their clone army?(A-Obi-Wan Kenobi,B-Qui-Gon Jinn,C-Sifo-Dyas,D-Mace Windu)")
        if answer10 == "C":
            print("Right!")
            score += 1
            print(f"You answered {score} out of 10 questions correctly!")
        else:
            print("Wrong! Correct answer:C")
            print(f"You answered {score} out of 10 questions correctly!")
            time.sleep(3)


    elif choice == "L":
        name = input("Name:")
        code = input("Code:")
        if code == "MasterIskander9602":
            print("Profile")
            print("------------")
            print("|          |")
            print("|          |")
            print("|          |")
            print("|          |")
            print("------------")
            print("MasterIskander96")
            print("Job title:Website creator")
            time.sleep(2)
        elif code == "Starwars9791n":
            print("Profile")
            print("------------")
            print("|          |")
            print("|          |")
            print("|          |")
            print("|          |")
            print("------------")
            print(f"{name}")
            print("Job title:Visitor")
            time.sleep(2)

        else:
            print("Invalid name or code")


    elif choice  == "A":
        print("========== About website ==========")
        print("Website: StarWarsWebsite")
        print("Creator: Iskander Abdullayev")
        print("Creation date: 11.08.2026")
        print("Theme: Star Wars")
        print("Version: 1.0")
        print("StarWarsWebsite is a fan-made website")
        print("with Star Wars quizzes, games and information.")
        print("Thank you for visiting StarWarsWebsite! 🚀")
        print("===================================")
        time.sleep(5)

    elif choice == "F":
        planets = [
            "Tatooine (where there is a lot of sand)",
            "Coruscant (city-planet)",
            "Hoth (where it is very cold)",
            "Endor (where ewoks live)"]



        input("Press Enter to find out where to go on vacation...")


        planet_name = random.choice(planets)
        print("🚀 Your ship is heading to the planet:",planet_name)
        time.sleep(2)

    elif choice == "E":

        clar = input("👍 - like,👎 -  Dislike,<")
        if clar == "Like":
            print("Thanks for the like")
            print("The website was created by Iskander Abdullaev.")
        elif clar == "Dislike":
            print("We will try to do better.")
            print("The website was created by Iskander Abdullaev")
        elif clar == "<":
            print("Link:")
            print("The website was created by Iskander Abdullaev")
        else:
            print("Unknown smiley face")


    elif choice == "S":
        choi = input("========== SETTINGS ==========\n"
              "1 - Delete account\n"
              "2 - Reload the site\n"
              "3 - Rules\n"
              "===============================")
        if choi == 1:
            print("Your account has been deleted.")



        elif choi == 2:
            print("Reloading...")
            time.sleep(3)
            print("The site has been reloaded")


        elif choi == 3:
            print("Rules:")
            print("1. Do not use offensive language.")
            print("2. Do not spam.")
            print("3. Have fun with Star Wars!")

        else:
            print("Invalid choice")

    else:
        print("Error!Unknown feature")
