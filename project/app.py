import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
import questions

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///characters.db")

#Create table for characters
listOfTables = db.execute("""SELECT name FROM sqlite_master WHERE type='table' AND name='characters'; """)
if listOfTables == []:
    db.execute("CREATE TABLE characters(base_class CHAR(20), final_class CHAR(20))")

@app.route("/")
def index():
    questionnaires = questions.questionnaires
    question_numbering = questions.question_numbering
    questions_icon = questions.questions_icon
    session.clear()
    #Show results
    characters_results = db.execute("SELECT base_class,final_class, COUNT(final_class) AS total FROM characters GROUP BY final_class")
    return render_template("index.html", questionnaires=questionnaires, questionnaires_numbering=question_numbering, questions_icon=questions_icon, characters_results=characters_results)


@app.route("/base_class", methods=["GET", "POST"])
def base_class():
    #Ensure username was submitted
    for question_numbers in questions.questionnaires_numbering:
       answers = request.form.get(question_numbers).split(", ")
       for answer in answers:
           if (answer in questions.base_class):
               questions.base_class[answer] += 1

    base_class_result = max(questions.base_class, key=questions.base_class.get)
    class_desc = questions.class_desc[base_class_result]
    session["base_class"] = base_class_result

    if (base_class_result == "Academic"):
        questionnaire = questions.academic_questionnaires
        question_numbering =  questions.academic_questionnaires_numbering
        class_image = "/static/Academic/academic.png"
        class_image_logo = "/static/Academic/academic-logo.png"
    elif (base_class_result == "Archer" ):
        questionnaire = questions.archer_questionnaires
        question_numbering =  questions.archer_questionnaires_numbering
        class_image = "/static/Archer/archer.png"
        class_image_logo = "/static/Archer/archer-logo.png"
    elif (base_class_result == "Assassin"):
        questionnaire = questions.assassin_questionnaires
        question_numbering =  questions.assassin_questionnaires_numbering
        class_image = "/static/Assassin/assassin.png"
        class_image_logo = "/static/Assassin/assassin-logo.png"
    elif (base_class_result == "Cleric"):
        questionnaire = questions.cleric_questionnaires
        question_numbering =  questions.cleric_questionnaires_numbering
        class_image = "/static/Cleric/cleric.png"
        class_image_logo = "/static/Cleric/cleric-logo.png"
    elif (base_class_result == "Kali"):
        questionnaire = questions.kali_questionnaires
        question_numbering =  questions.kali_questionnaires_numbering
        class_image = "/static/Kali/kali.png"
        class_image_logo = "/static/Kali/kali-logo.png"
    elif (base_class_result == "Lancea"):
        questionnaire = questions.lancea_questionnaires
        question_numbering =  questions.lancea_questionnaires_numbering
        class_image = "/static/Lancea/lancea.png"
        class_image_logo = "/static/Lancea/lancea-logo.png"
    elif (base_class_result == "Sorc"):
        questionnaire = questions.sorc_questionnaires
        question_numbering =  questions.sorc_questionnaires_numbering
        class_image = "/static/Sorc/sorc.png"
        class_image_logo = "/static/Sorc/sorc-logo.png"
    else:
        questionnaire = questions.warrior_questionnaires
        question_numbering =  questions.warrior_questionnaires_numbering
        class_image = "/static/Warrior/warrior.png"
        class_image_logo = "/static/Warrior/warrior-logo.png"

    return render_template("base_class.html", base_class=base_class_result, questionnaires=questionnaire, questionnaires_numbering=question_numbering, class_image=class_image, class_desc=class_desc, class_image_logo=class_image_logo)

@app.route("/advance_class", methods=["GET", "POST"])
def advance_class():

    if (session["base_class"] != "Lancea"):
        for question_numbers in questions.base_class_questionnaires_numbering:
            answers = request.form.get(question_numbers).split(", ")
            for answer in answers:
                if (answer in questions.advance_class):
                    questions.advance_class[answer] += 1
    else:
        for question_numbers in questions.lancea_base_class_questionnaires_numbering:
            answers = request.form.get(question_numbers).split(", ")
            for answer in answers:
                if (answer in questions.advance_class):
                    questions.advance_class[answer] += 1
    advance_class_result = max(questions.advance_class, key=questions.advance_class.get)
    class_desc = questions.advace_class_desc[advance_class_result]

    #Academic
    if (advance_class_result == "Adept"):
        class_image = "/static/Academic/adept.jpg"
        class_image_logo = "/static/Academic/adept-logo.png"
    elif (advance_class_result == "Shooting star" ):
        class_image = "/static/Academic/shooting-star.jpg"
        class_image_logo = "/static/Academic/shooting-star-logo.png"
    elif (advance_class_result == "Gear master" ):
        class_image = "/static/Academic/gear-master.jpg"
        class_image_logo = "/static/Academic/gear-master-logo.png"
    elif (advance_class_result == "Physician" ):
        class_image = "/static/Academic/pysician.jpg"
        class_image_logo = "/static/Academic/pysician-logo.png"
    #Archer
    elif (advance_class_result == "Sniper" ):
        class_image = "/static/Archer/sniper.jpg"
        class_image_logo = "/static/Archer/sniper-logo.png"
    elif (advance_class_result == "Artillery" ):
        class_image = "/static/Archer/artillery.jpg"
        class_image_logo = "/static/Archer/artillery-logo.png"
    elif (advance_class_result == "Temptest" ):
       class_image = "/static/Archer/tempest.jpg"
       class_image_logo = "/static/Archer/tempest-logo.png"
    elif (advance_class_result == "Wind walker" ):
       class_image = "/static/Archer/wind-walker.jpg"
       class_image_logo = "/static/Archer/wind-walker-logo.png"
    #Assassin
    elif (advance_class_result == "Ripper" ):
       class_image = "/static/Assassin/ripper.jpg"
       class_image_logo = "/static/Assassin/ripper-logo.png"
    elif (advance_class_result == "Raven" ):
        class_image = "/static/Assassin/raven.jpg"
        class_image_logo = "/static/Assassin/raven-logo.png"
    elif (advance_class_result == "Light fury" ):
        class_image = "/static/Assassin/light-fury.jpg"
        class_image_logo = "/static/Assassin/light-fury-logo.png"
    elif (advance_class_result == "Abyss walker" ):
        class_image = "/static/Assassin/abyss-walker.jpg"
        class_image_logo = "/static/Assassin/abyss-walker-logo.png"
    #Cleric
    elif (advance_class_result == "Saint" ):
        class_image = "/static/Cleric/saint.jpg"
        class_image_logo = "/static/Cleric/saint-logo.png"
    elif (advance_class_result == "Inquisitor" ):
        class_image = "/static/Cleric/inquisitor.jpg"
        class_image_logo = "/static/Cleric/inquisitor-logo.png"
    elif (advance_class_result == "Guardian" ):
        class_image = "/static/Cleric/guardian-and-crusader.jpg"
        class_image_logo = "/static/Cleric/guardian-logo.png"
    elif (advance_class_result == "Crusader" ):
        class_image = "/static/Cleric/guardian-and-crusader.jpg"
        class_image_logo = "/static/Cleric/crusader-logo.png"
    #Kali
    elif (advance_class_result == "Spirit dancer" ):
        class_image = "/static/Kali/spirit-dancer.jpg"
        class_image_logo = "/static/Kali/spirit-dancer-logo.png"
    elif (advance_class_result == "Blade dancer" ):
        class_image = "/static/Kali/blade-dancer.jpg"
        class_image_logo = "/static/Kali/blade-dancer-logo.png"
    elif (advance_class_result == "Soul eater" ):
        class_image = "/static/Kali/soul-eater.jpg"
        class_image_logo = "/static/Kali/soul-eater-logo.png"
    elif (advance_class_result == "Dark summoner" ):
        class_image = "/static/Kali/dark-summoner.jpg"
        class_image_logo = "/static/Kali/dark-summoner-logo.png"
    #Lancea
    elif (advance_class_result == "Flurry" ):
        class_image = "/static/Lancea/sting-breezer-flurry.jpg"
        class_image_logo = "/static/Lancea/flurry-logo.png"
    elif (advance_class_result == "Sting breezer" ):
        class_image = "/static/Lancea/sting-breezer-flurry.jpg"
        class_image_logo = "/static/Lancea/sting-breezer-logo.png"
    #Sorc
    elif (advance_class_result == "Elestra" ):
        class_image = "/static/Sorc/elestra.jpg"
        class_image_logo = "/static/Sorc/elestra-logo.png"
    elif (advance_class_result == "Saleana" ):
        class_image = "/static/Sorc/saleana.jpg"
        class_image_logo = "/static/Sorc/saleana-logo.png"
    elif (advance_class_result == "Majesty" ):
        class_image = "/static/Sorc/majesty.jpg"
        class_image_logo = "/static/Sorc/majesty-logo.png"
    elif (advance_class_result == "Smasher" ):
        class_image = "/static/Sorc/smasher.jpg"
        class_image_logo = "/static/Sorc/smasher-logo.png"
    #Warrior
    elif (advance_class_result == "Gladiator" ):
        class_image = "/static/Warrior/gladiator.jpg"
        class_image_logo = "/static/Warrior/gladiator-logo.png"
    elif (advance_class_result == "Moonlord" ):
        class_image = "/static/Warrior/moonlord.jpg"
        class_image_logo = "/static/Warrior/moonlord-logo.png"
    elif (advance_class_result == "Barbarian" ):
        class_image = "/static/Warrior/barbarian.jpg"
        class_image_logo = "/static/Warrior/barbarian-logo.png"
    else:
        class_image = "/static/Warrior/destroyer.jpg"
        class_image_logo = "/static/Warrior/destroyer-logo.png"

    #Insert results into characters
    db.execute("INSERT INTO characters (base_class, final_class) VALUES (?, ?);",session["base_class"], advance_class_result)

    return render_template("advance_class.html", advance_class=advance_class_result, class_image=class_image, class_desc=class_desc, class_image_logo=class_image_logo)

