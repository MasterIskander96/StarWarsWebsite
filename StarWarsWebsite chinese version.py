import time
import random
import webbrowser


print("欢迎来到 StarWarsWebsite")

while True:
    time.sleep(2)
    print("网站功能：\n"
          "官 - 星球大战官方网站\n"
          "注 - 注册\n"
          "登 - 登录\n"
          "关 - 关于网站\n"
          "测 - StarWarsQuiz\n"
          "评 - 反馈\n"
          "设 - 设置\n"
          "假 - 假期你要飞往哪里？")

    choice = input("请选择一个网站功能：")

    if choice == "官":
        print("正在加载...")
        time.sleep(2)
        webbrowser.open("https://www.starwars.com")

    elif choice == "注":
        input("姓名：")
        print("你的代码：Starwars9791n")
        time.sleep(1)

    elif choice == "测":
        score = 0

        answer1 = input(
            "1. Boba Fett第一次出现在哪一部Star Wars电影中？"
            "(A-4,B-5,C-2,D-8)"
        )
        if answer1 == "B":
            print("正确！")
            score += 1
        else:
            print("错误！正确答案：B")

        answer2 = input(
            "2. Cad Bane是谁？"
            "(A-伐木工,B-绝地武士,C-赏金猎人,D-网站)"
        )
        if answer2 == "C":
            print("正确！")
            score += 1
        else:
            print("错误！正确答案：C")

        answer3 = input(
            "3. Grogu在2026年多大？"
            "(A-55,B-59,C-84,D-53)"
        )
        if answer3 == "D":
            print("正确！")
            score += 1
        else:
            print("错误！正确答案：D")

        answer4 = input(
            "4. Captain Rex的克隆编号是什么？"
            "(A-CT-5555,B-CT-1409,C-CT-7567,D-CC-2224)"
        )
        if answer4 == "C":
            print("正确！")
            score += 1
        else:
            print("错误！正确答案：C")

        answer5 = input(
            "5. Count Dooku转向黑暗面后，第一个学徒是谁？"
            "(A-Asajj Ventress,B-General Grievous,"
            "C-Ki-Adi-Mundi,D-Kit Fisto)"
        )
        if answer5 == "A":
            print("正确！")
            score += 1
        else:
            print("错误！正确答案：A")

        answer6 = input(
            "6. Darth Vader在Return of the Jedi中的旗舰叫什么？"
            "(A-Devastator,B-Executor,C-Eclipse,D-Chimaera)"
        )
        if answer6 == "B":
            print("正确！")
            score += 1
        else:
            print("错误！正确答案：B")

        answer7 = input(
            "7. The Rise of Skywalker中，Exegol原来的名字是什么？"
            "(A-Korriban,B-Dathomir,C-Malachor,D-Moraband)"
        )
        if answer7 == "D":
            print("正确！")
            score += 1
        else:
            print("错误！正确答案：D")

        answer8 = input(
            "8. 后来成为Commander Cody的克隆士兵编号是什么？"
            "(A-CT-7567,B-CC-1119,C-CC-2224,D-CT-1409)"
        )
        if answer8 == "C":
            print("正确！")
            score += 1
        else:
            print("错误！正确答案：C")

        answer9 = input(
            "9. 创建Rule of Two的古代Sith Lord是谁？"
            "(A-Darth Bane,B-Darth Revan,"
            "C-Darth Nihilus,D-Darth Malak)"
        )
        if answer9 == "A":
            print("正确！")
            score += 1
        else:
            print("错误！正确答案：A")

        answer10 = input(
            "10. 哪位Jedi发现了Kamino人和他们的克隆军队？"
            "(A-Obi-Wan Kenobi,B-Qui-Gon Jinn,"
            "C-Sifo-Dyas,D-Mace Windu)"
        )
        if answer10 == "C":
            print("正确！")
            score += 1
        else:
            print("错误！正确答案：C")

        print(f"你答对了10道题中的{score}道！")
        time.sleep(3)

    elif choice == "登":
        name = input("姓名：")
        code = input("代码：")

        if code == "MasterIskander9602":
            print("个人资料")
            print("------------")
            print("|          |")
            print("|          |")
            print("|          |")
            print("|          |")
            print("------------")
            print("MasterIskander96")
            print("职位：网站创建者")
            time.sleep(2)

        elif code == "Starwars9791n":
            print("个人资料")
            print("------------")
            print("|          |")
            print("|          |")
            print("|          |")
            print("|          |")
            print("------------")
            print(f"{name}")
            print("职位：访客")
            time.sleep(2)

        else:
            print("姓名或代码无效")

    elif choice == "关":
        print("========== 关于网站 ==========")
        print("网站：StarWarsWebsite")
        print("创建者：Iskander Abdullayev")
        print("创建日期：11.08.2026")
        print("主题：Star Wars")
        print("版本：1.0")
        print("StarWarsWebsite是一个粉丝制作的网站")
        print("包含Star Wars测验、游戏和信息。")
        print("感谢你访问StarWarsWebsite！🚀")
        print("==============================")
        time.sleep(5)

    elif choice == "假":
        planets = [
            "Tatooine（那里有很多沙子）",
            "Coruscant（城市星球）",
            "Hoth（那里非常寒冷）",
            "Endor（Ewok居住的地方）"
        ]

        input("按Enter键查看你的假期目的地...")

        planet_name = random.choice(planets)
        print("🚀 你的飞船正在前往星球：", planet_name)
        time.sleep(2)

    elif choice == "评":
        clar = input("👍 - 喜欢，👎 - 不喜欢，<")

        if clar == "喜欢":
            print("感谢你的点赞！")
            print("该网站由Iskander Abdullaev创建。")

        elif clar == "不喜欢":
            print("我们会努力做得更好。")
            print("该网站由Iskander Abdullaev创建。")

        elif clar == "<":
            print("链接：")
            print("该网站由Iskander Abdullaev创建。")

        else:
            print("未知表情")

    elif choice == "设":
        choi = input(
            "========== 设置 ==========\n"
            "1 - 删除账户\n"
            "2 - 重新加载网站\n"
            "3 - 规则\n"
            "=========================="
        )

        if choi == "1":
            print("你的账户已被删除。")

        elif choi == "2":
            print("正在重新加载...")
            time.sleep(3)
            print("网站已重新加载。")

        elif choi == "3":
            print("规则：")
            print("1. 不要使用冒犯性语言。")
            print("2. 不要发送垃圾信息。")
            print("3. 享受Star Wars！")

        else:
            print("选项无效")

    else:
        print("错误！未知功能")