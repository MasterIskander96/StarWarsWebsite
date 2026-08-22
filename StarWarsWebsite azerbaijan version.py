import time
import random
import webbrowser


print("StarWarsWebsite-ə xoş gəlmisiniz!")

while True:
    time.sleep(2)
    print("Sayt funksiyaları:\n"
          "S - Rəsmi Star Wars saytı\n"
          "Q - Qeydiyyat\n"
          "D - Daxil ol\n"
          "M - Sayt haqqında\n"
          "V - StarWars viktorinası\n"
          "R - Rəy\n"
          "N - Nizamlamalar\n"
          "T - Tətil üçün hara uçacaqsınız?")

    choice = input("Sayt funksiyasını seçin: ")

    if choice == "S":
        print("Yüklənir...")
        time.sleep(2)
        webbrowser.open("https://www.starwars.com")

    elif choice == "Q":
        input("Ad: ")
        print("Sizin kodunuz: Starwars9791n")
        time.sleep(1)

    elif choice == "V":
        score = 0

        answer1 = input(
            "1. Boba Fett ilk dəfə Star Wars-un hansı epizodunda görünüb?"
            "(A-4, B-5, C-2, D-8): ")

        if answer1 == "B":
            print("Doğrudur!")
            score += 1
        else:
            print("Yanlışdır! Düzgün cavab: B")

        answer2 = input(
            "2. Cad Bane kimdir?"
            "(A-Taxtaçı, B-Ceday, C-Baş ovçusu, D-Veb-sayt): ")

        if answer2 == "C":
            print("Doğrudur!")
            score += 1
        else:
            print("Yanlışdır! Düzgün cavab: C")

        answer3 = input(
            "3. 2026-cı ildə Qroqunun neçə yaşı var?"
            "(A-55, B-59, C-84, D-53): ")

        if answer3 == "D":
            print("Doğrudur!")
            score += 1
        else:
            print("Yanlışdır! Düzgün cavab: D")

        answer4 = input(
            "4. Kapitan Reks hansı klon nömrəsini daşıyırdı?"
            "(A-CT-5555, B-CT-1409, C-CT-7567, D-CC-2224): ")

        if answer4 == "C":
            print("Doğrudur!")
            score += 1
        else:
            print("Yanlışdır! Düzgün cavab: C")

        answer5 = input(
            "5. Qraf Duku qaranlıq tərəfə keçdikdən sonra onun ilk şagirdi kim idi?"
            "(A-Asajj Ventress, B-General Grievous, C-Ki-Adi-Mundi, D-Kit Fisto): ")

        if answer5 == "A":
            print("Doğrudur!")
            score += 1
        else:
            print("Yanlışdır! Düzgün cavab: A")

        answer6 = input(
            "6. 'Return of the Jedi' filmində Darth Vaderin flaqman gəmisinin adı nə idi?"
            "(A-Devastator, B-Executor, C-Eclipse, D-Chimaera): ")

        if answer6 == "B":
            print("Doğrudur!")
            score += 1
        else:
            print("Yanlışdır! Düzgün cavab: B")

        answer7 = input(
            "7. 'The Rise of Skywalker' filmində Exegolun qədim adı nə idi?"
            "(A-Korriban, B-Dathomir, C-Malachor, D-Moraband): ")

        if answer7 == "D":
            print("Doğrudur!")
            score += 1
        else:
            print("Yanlışdır! Düzgün cavab: D")

        answer8 = input(
            "8. Commander Cody kimi tanınan klon əsgərinin nömrəsi nə idi?"
            "(A-CT-7567, B-CC-1119, C-CC-2224, D-CT-1409): ")

        if answer8 == "C":
            print("Doğrudur!")
            score += 1
        else:
            print("Yanlışdır! Düzgün cavab: C")

        answer9 = input(
            "9. İki Qaydasını yaradan qədim Sith Lordunun adı nə idi?"
            "(A-Darth Bane, B-Darth Revan, C-Darth Nihilus, D-Darth Malak): ")

        if answer9 == "A":
            print("Doğrudur!")
            score += 1
        else:
            print("Yanlışdır! Düzgün cavab: A")

        answer10 = input(
            "10. Kaminoalıları və onların klon ordusunu hansı Jedi kəşf etmişdi?"
            "(A-Obi-Wan Kenobi, B-Qui-Gon Jinn, C-Sifo-Dyas, D-Mace Windu): ")

        if answer10 == "C":
            print("Doğrudur!")
            score += 1
        else:
            print("Yanlışdır! Düzgün cavab: C")

        print(f"10 sualdan {score} düzgün cavab verdiniz!")
        time.sleep(3)

    elif choice == "D":
        name = input("Ad: ")
        code = input("Kod: ")

        if code == "MasterIskander9602":
            print("Profil")
            print("------------")
            print("|          |")
            print("|          |")
            print("|          |")
            print("|          |")
            print("------------")
            print("MasterIskander96")
            print("Vəzifə: Sayt yaradıcısı")
            time.sleep(2)

        elif code == "Starwars9791n":
            print("Profil")
            print("------------")
            print("|          |")
            print("|          |")
            print("|          |")
            print("|          |")
            print("------------")
            print(f"{name}")
            print("Vəzifə: Ziyarətçi")
            time.sleep(2)

        else:
            print("Yanlış ad və ya kod")

    elif choice == "M":
        print("========== Sayt haqqında ==========")
        print("Sayt: StarWarsWebsite")
        print("Yaradıcı: Iskander Abdullayev")
        print("Yaradılma tarixi: 11.08.2026")
        print("Mövzu: Star Wars")
        print("Versiya: 1.0")
        print("StarWarsWebsite fan saytdır.")
        print("Burada Star Wars viktorinaları, oyunları")
        print("və məlumatları var.")
        print("StarWarsWebsite-i ziyarət etdiyiniz üçün təşəkkürlər! 🚀")
        print("===================================")
        time.sleep(5)

    elif choice == "T":
        planets = [
            "Tatooine (çoxlu qum olan planet)",
            "Coruscant (şəhər-planeti)",
            "Hoth (çox soyuq planet)",
            "Endor (Ewokların yaşadığı planet)"
        ]

        input("Tətil üçün hara gedəcəyinizi öyrənmək üçün Enter düyməsini basın...")

        planet_name = random.choice(planets)
        print("🚀 Gəminiz bu planetə uçur:", planet_name)
        time.sleep(2)

    elif choice == "R":
        clar = input(
            "👍 - Bəyənirəm, 👎 - Bəyənmirəm, < - Keçid: ")

        if clar == "Bəyənirəm":
            print("Bəyənməniz üçün təşəkkürlər!")
            print("Sayt Iskander Abdullayev tərəfindən yaradılıb.")

        elif clar == "Bəyənmirəm":
            print("Daha yaxşı olmağa çalışacağıq.")
            print("Sayt Iskander Abdullayev tərəfindən yaradılıb.")

        elif clar == "<":
            print("Keçid:")
            print("Sayt Iskander Abdullayev tərəfindən yaradılıb.")

        else:
            print("Naməlum seçim")

    elif choice == "N":
        choi = input(
            "========== NİZAMLAMALAR ==========\n"
            "1 - Hesabı sil\n"
            "2 - Saytı yenilə\n"
            "3 - Qaydalar\n"
            "==================================\n"
            "Nizamlamanı seçin: ")

        if choi == "1":
            print("Hesabınız silindi.")

        elif choi == "2":
            print("Yenilənir...")
            time.sleep(3)
            print("Sayt yeniləndi.")

        elif choi == "3":
            print("Qaydalar:")
            print("1. Təhqiramiz sözlərdən istifadə etməyin.")
            print("2. Spam göndərməyin.")
            print("3. Star Wars-dan zövq alın!")

        else:
            print("Yanlış seçim")

    else:
        print("Xəta! Naməlum funksiya")
