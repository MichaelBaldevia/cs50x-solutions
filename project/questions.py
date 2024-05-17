questionnaires_numbering = ["base_class_q1", "base_class_q2", "base_class_q3", "base_class_q4", "base_class_q5", "base_class_q6", "base_class_q7", "base_class_q8", "base_class_q9", "base_class_q10"]
question_numbering = {"Do you actively help someone in need when you see them in trouble?" : "base_class_q1", "Do you believe in a supreme being?" : "base_class_q2", "What do you do in your free time?" : "base_class_q3", "What do you do when you are ordered to do something?" : "base_class_q4",
                                "When you are sleeping at night and woken up to a loud sound?" : "base_class_q5", "When someone is sizing up with you what do you do?" : "base_class_q6", "There are rumors spreading about you, what do you do?" : "base_class_q7",
                                "You woke up and the day is sunny and full of life. What do you do?" : "base_class_q8", "You woke up and the day is rainy and cold. What do you do?" : "base_class_q9", "What word resonates with you?" : "base_class_q10"}
questionnaires = {"Do you actively help someone in need when you see them in trouble?" :
                    {"Yes" : "Cleric, Warrior",
                    "Yes but i may worsen the problem" : "Academic, Lancea",
                    "Yes but i need to know if i can help" : "Archer, Kali, Sorc",
                    "No because I dont want any trouble" : "Assassin"},
                "Do you believe in a supreme being?" :
                    {"Yes" : "Archer, Cleric",
                    "No " : "Kali, Sorc",
                    "To a certain extent": "Academic, Lancea",
                    "I am the supreme being": "Assassin, Warrior"},
                "What do you do in your free time?":
                    {"Sleep": "Assassin, Kali, Warrior",
                    "Read ": "Academic, Cleric, Sorc",
                    "Whatever comes to mind": "Lancea, Cleric",
                    "Hone my skills": "Archer, Assassin, Sorc, Warrior"},
                "What do you do when you are ordered to do something?":
                    {"Do it immediately" : "Assassin, Lancea",
                    "Do it flawlessly": "Archer, Cleric",
                    "I can do it later" : "Academic, Kali, Warrior",
                    "Let someone do it for me": "Sorc"},
                "When you are sleeping at night and woken up to a loud sound?":
                    {"Prepare first then check what/who made that sound" : "Archer, Lancea",
                    "Check it" : "Cleric, Kali, Warrior",
                    "Stealthily check it then fall back if its dangerous": "Assassin, Sorc",
                    "Pretent nothing happened and go back to sleep.": "Academic"},
                "When someone is sizing up with you what do you do?":
                    {"Size up with them": "Warrior",
                    "he/she doesnt know what' coming": "Assassin, Sorc",
                    "Ignore": "Archer, Cleric",
                    "this doesnt happen with me.": "Academic, Kali, Lancea"},
                "There are rumors spreading about you, what do you do?":
                    {"Rumors? what rumors?": "Academic, Lancea",
                    "Find who made that and make them pay": "Assassin, Warrior",
                    "Rumors are only rumors nothing else": "Archers, Cleric",
                    "Nonsense": "Kali, Sorc"},
                "You woke up and the day is sunny and full of life. What do you do?":
                    {"Go out and enjoy the day" : "Academic, Lancea",
                    "Good time to be productive" : "Archer, Sorc",
                    "Nothing special Just do what you normally do" : "Cleric, Kali, Warrior",
                    "I hate sunny days" : "Assassin"},
                "You woke up and the day is rainy and cold. What do you do?":
                    {"Go back to sleep" : "Kali, Lancea, Warrior",
                    "Get up and make coffee and enjoy the cold morning": "Archer, Sorc",
                    "Nothing special just do what you normally do": "Assassin, Cleric",
                    "I hate rainy days": "Academic"},
                "What word resonates with you?":
                    {"Peace": "Archer, Cleric, Kali, Warrior, Lancea",
                    "Lovely" : "Archer, Kali, Sorc",
                    "Cutesy" : "Academic, Lancea",
                    "Vengeful" : "Assassin, Sorc",
                    "Determined" : "Assassin, Cleric, Warrior, Lancea",
                    "Tinkerer" : "Academic"}}


base_class = {"Academic" : 0, "Archer" : 0, "Assassin" : 0, "Cleric" : 0, "Kali" : 0, "Lancea" : 0, "Sorc" : 0, "Warrior" : 0}
advance_class = {"Adept" : 0, "Gear master" : 0, "Shooting star" : 0, "Physician" : 0,
                "Artillery" : 0, "Sniper" : 0, "Tempest" : 0, "Wind walker" : 0,
                "Ripper" : 0, "Raven" : 0, "Light fury" : 0, "Abyss walker" : 0,
                "Saint" : 0, "Inquisitor" : 0, "Crusader" : 0, "Guardian" : 0,
                "Blade dancer" : 0, "Spirit dancer" : 0, "Soul eater" : 0, "Dark summoner" : 0,
                "Flurry" : 0, "Sting breezer" : 0,
                "Elestra" : 0, "Saleana" : 0, "Majesty" : 0, "Smasher" : 0,
                "Moonlord" : 0, "Destroyer" : 0, "Gladiator" : 0, "Barbarian" : 0}
base_class_questionnaires_numbering = ["advance_class_q1", "advance_class_q2", "advance_class_q3", "advance_class_q4", "advance_class_q5"]
lancea_base_class_questionnaires_numbering = ["advance_class_q1", "advance_class_q2", "advance_class_q3"]
academic_questionnaires_numbering = {"What do you like to tinker with Nature or Man made?" : "advance_class_q1",
                                    "Do you like doing the things you need to do or let someone you trust handle them?" : "advance_class_q2",
                                    "What support would you like to have?" : "advance_class_q3",
                                    "If you are planning to conquer the world what would you use?" : "advance_class_q4",
                                    "If you are going to help someone how will do it?" : "advance_class_q5"}
academic_questionnaires = {"What do you like to tinker with Nature or Man made?" :
                    {"Nature " : "Adept, Physician",
                    "Man made" : "Shooting star, Gear master"},
                "Do you like doing the things you need to do or let someone you trust handle them?" :
                    {"I will do it my self" : "Adept, Physician",
                    "I trust them" : "Gear Master, Shooting star"},
                "What support would you like to have?":
                    {"Many cute robots": "Gear master",
                    "A lot of man made chemicals  ": "Physician",
                    "A realiable robot that can protect me": "Shooting star",
                    "Nothing can beat nature": "Adept"},
                "If you are planning to conquer the world what would you use?":
                    {"Virus and chemicals" : "Physician",
                    "Disasters": "Adept",
                    "Robot invasion" : "Gear master",
                    "Me and my trusted robot can handle anything": "Shooting star"},
                "If you are going to help someone how will do it?":
                    {"Nothing can beat science" : "Physican",
                    "My robots will manage" : "Gear master",
                    "Nature has the answer": "Adept",
                    "I will help": "Shooting star"}}

archer_questionnaires_numbering = {"Are you a stand still and kill from afar or Agile killer?" : "advance_class_q1",
                                    "What would like to fight with: Arrows and Pulling power or Arrows and agile repositioning?" : "advance_class_q2",
                                    "What arrows would you like to use?" : "advance_class_q3",
                                    "What is the most efficient way for you to hunt?" : "advance_class_q4",
                                    "What word best describe you as an archer?" : "advance_class_q5"}
archer_questionnaires = {"Are you a stand still and kill from afar or Agile killer?" :
                    {"Stand still " : "Artillery, Sniper",
                    "Agile" : "Tempest, Wind walker"},
                "What would like to fight with: Arrows and Pulling power or Arrows and agile repositioning?" :
                    {"Pulling power" : "Sniper, Artillery",
                    "Arrows and agile repositioning" : "Wind walker, Tempest"},
                "What arrows would you like to use?":
                    {"Enchanted arrows that tracks your enemy": "Artillery",
                    "Sturdy arrows that can penetrate anything": "Sniper",
                    "Arrows that are fast and cant be evaded": "Tempest",
                    "Arrows enhanced by wind": "Wind walker"},
                "What is the most efficient way for you to hunt?":
                    {"Enchant my arrows before hunting" : "Artillery",
                    "Ambush from afar": "Sniper",
                    "Relentless but efficient chase" : "Tempest",
                    "Let the wind guide my arrow": "Wind walker"},
                "What word best describe you as an archer?":
                    {"Elegant powerful shots" : "Sniper",
                    "Enhancting shots" : "Artillery",
                    "Mystifying shots": "Wind walker",
                    "Agile shots": "Tempest"}}

assassin_questionnaires_numbering = {"If you are going to assassinate someone how will do it?" : "advance_class_q1",
                                    "If you are going someone that you will struggle against with what do you do?" : "advance_class_q2",
                                    "How would you fight?" : "advance_class_q3",
                                    "If you are going to help with someone from getting hurt how will do it?" : "advance_class_q4",
                                    "What describes you the most?": "advance_class_q5"}
assassin_questionnaires = {"If you are going to assassinate someone how will do it?" :
                    {"Hidden weapons" : "Ripper, Raven",
                    "Unknown powers" : "Light fury, Abyss walker"},
                "If you are going someone that you will struggle against with what do you do?" :
                    {"Improve my skills to match or overpower them" : "Ripper, Raven",
                    "Enchant weapons and Summon followers" : "Light fury, Abyss walker"},
                "How would you fight?":
                    {"Relentless attacks and Shadow summon": "Ripper",
                    "Hidden Weapons and Dark Magic": "Raven",
                    "Blinding lights and fast movements": "Light fury",
                    "Attacks that can come from anywhere": "Abyss walker"},
                "If you are going to help with someone from getting hurt how will do it?":
                    {"Punish the bully" : "Raven",
                    "Make that bully regret what he has done": "Ripper",
                    "Consequences must be met" : "Light fury",
                    "Scare that bully so it will not happen to anyone again": "Abyss walker"},
                "What describes you the most?":
                    {"Stealthy" : "Raven",
                    "Passionate " : "Ripper",
                    "Vengeful ": "Abyss walker",
                    "Calm ": "Light fury"}}

cleric_questionnaires_numbering = {"If you are going to teach someone how will you do it?" : "advance_class_q1",
                                    "If you are going to spread your beliefs how will you do it?" : "advance_class_q2",
                                    "If someone is getting attacked in front of you what will you do?" : "advance_class_q3",
                                    "Incase of invasion what will you do?" : "advance_class_q4",
                                    "Someone has offended you what would you do?": "advance_class_q5"}
cleric_questionnaires = {"If you are going to teach someone how will you do it?" :
                    {"Give them lessons" : "Saint, Inquisitor",
                    "Experience is the best teacher" : "Guardian, Crusader"},
                "If you are going to spread your beliefs how will you do it?" :
                    {"Through life lessons and words" : "Saint, Inquisitor",
                    "Show them what you believe in" : "Guardian, Crusader"},
                "If someone is getting attacked in front of you what will you do?":
                    {"Protect": "Guardian",
                    "Escape": "Saint",
                    "Purge the enemy": "Inquisitor",
                    "Face the conquerors": "Crusader"},
                "Incase of invasion what will you do?":
                    {"Protect the people" : "Guardian",
                    "Guide the innocent to a safe place": "Saint",
                    "Consequences must be met" : "Light fury",
                    "Scare that bully so it will not happen to anyone again": "Abyss walker"},
                "Someone has offended you what would you do?":
                    {"'Mistakes happen'" : "Guardian",
                    "Forgive them " : "Saint",
                    "You will face the consequences next time ": "Crusader",
                    "Let them face the appropriate consequence ": "Inquisitor"}}

kali_questionnaires_numbering = {"If you are going to dance how would you do it?" : "advance_class_q1",
                                    "If you are ask to hurt someone how will you do it?" : "advance_class_q2",
                                    "You are going to show someone your skills What what would your skills be?" : "advance_class_q3",
                                    "In pursue of peace what will you do when other's try to hurt you?" : "advance_class_q4",
                                    "What word describe you the best under pressure": "advance_class_q5"}
kali_questionnaires = {"If you are going to dance how would you do it?" :
                    {"Dance elegantly yet with impactful moves" : "Blade Dancer, Spirit Dancer",
                    "Dance Mysticly to captivate the audience" : "Dark summoner, Soul eater"},
                "If you are ask to hurt someone how will you do it?" :
                    {"Hurt the with weapons and summons" : "Blade Dancer, Spirit Dancer",
                    "Hurt them with curses and summons" : "Dark summoner, Soul eater"},
                "You are going to show someone your skills What what would your skills be?":
                    {"Proficiency with weapons combined with elegant movement": "Blade dancer",
                    "proficiency with summoning combined with elegant movement": "Spirit Dancer",
                    "Proficiency with summoning and curses": "Soul eater",
                    "Proficiency with dark enhancement": "Dark summoner"},
                "In pursue of peace what will you do when other's try to hurt you?":
                    {"Peaceful movement" : "Spirit Dancer",
                    "Vengeful actions": "Dark summoner",
                    "Justifiable violence" : "Blade dancer",
                    "Dark magic and curses": "Soul Eater"},
                "What word describe you the best under pressure":
                    {"Calm and collected" : "Blade dancer",
                    "Solution focused" : "Spirit Dancer",
                    "Dont mind the pressure": "Soul Eater",
                    "Avoid the situation you can be under pressure": "Dark Summoner"}}

lancea_questionnaires_numbering = {"What word describes you the most?" : "advance_class_q1",
                                    "If fight is unavoidable how will you fight?" : "advance_class_q2",
                                    "If taunted how do you react?" : "advance_class_q3"}
lancea_questionnaires = {"What word describes you the most?" :
                    {"Enchanting" : "Sting breezer",
                    "Straightforward and direct" : "Flurry"},
                "If fight is unavoidable how will you fight?" :
                    {"Mystical spears" : "Sting breezer",
                    "Elegant swings with spear" : "Flurry"},
                "If taunted how do you react?":
                    {"Ignore ": "Flurry",
                    "Retaliate": "Sting breezer"}}

sorc_questionnaires_numbering = {"What magic do you want to wield?" : "advance_class_q1",
                                    "What element do you resonate the most?" : "advance_class_q2",
                                    "When confronted with enemy how do you react?" : "advance_class_q3",
                                    "When serving the king what do you prioritize?" : "advance_class_q4",
                                    "What house do you resonate with": "advance_class_q5"}
sorc_questionnaires = {"What magic do you want to wield?" :
                    {"Control Magic" : "Smasher, Majesty",
                    "Elemental Magic" : "Saleana - Elestra"},
                "What element do you resonate the most?" :
                    {"Ice" : "Elestra",
                    "Fire" : "Saleana",
                    "Light" : "Smasher",
                    "Dark" : "Majesty"},
                "When confronted with enemy how do you react?":
                    {"Dominate the battlefield with gravity control magic": "Majesty",
                    "Burn the area surrounding with Flame magic": "Saleana",
                    "Freeze everything with ice magic": "Elestra",
                    "Disintegrate anything with Light magic": "Smasher"},
                "When serving the king what do you prioritize?":
                    {"Defending the king" : "Elestra",
                    "Eliminating the enemy": "Saleana",
                    "Research" : "Majesty",
                    "Conquest": "Smasher"},
                "What house do you resonate with":
                    {"Gryffindor" : "Saleana",
                    "Hufflepuff" : "Elestra",
                    "Ravenclaw": "Smasher",
                    "Slytherin ": "Majesty"}}

warrior_questionnaires_numbering = {"In face of danger how do you respond?" : "advance_class_q1",
                                    "In a fight how do you want to act?" : "advance_class_q2",
                                    "In a fight how do you want to be seen?" : "advance_class_q3",
                                    "When you see someone getting bullied what do you do?" : "advance_class_q4",
                                    "How do you end a fight" : "advance_class_q5"}
warrior_questionnaires = {"In face of danger how do you respond?" :
                    {"Danger? What danger" : "Gladiator, Moonlord",
                    "I am the Danger" : "Destroyer, Barbarian"},
                "In a fight how do you want to act?" :
                    {"Blinding speed and Elegant movements" : "Gladiator, Moonlord",
                    "Impactful and powerful" : "Destroyer, Barbarian"},
                "In a fight how do you want to be seen?":
                    {"Elegant and no wasted movements": "Moonlord",
                    "Empowering and motivating": "Gladiator",
                    "Confident and overpowered": "Barbarian",
                    "I dont care": "Destroyer"},
                "When you see someone getting bullied what do you do?":
                    {"Help the person getting bullied" : "Moonlord",
                    "Teach the bully a lesson": "Gladiator",
                    "Destroy the bully" : "Destroyer",
                    "Bully the bully": "Barbarian"},
                "How do you end a fight":
                    {"Smirking to the enemy" : "Destroyer",
                    "Making a triumphant pose" : "Moonlord",
                    "Sitting and resting to what may come": "Gladiator",
                    "Hyped and you still want more ": "Barbarian"}}
class_desc = {"Academic" : "The Academic is the symbol of the advancements of the technology in the future, which she manifests through her artillery attacks, biochemical warfare and her trusty companion, the mechanical butler Alfredo. Originally from the future, the Academic is sent on a journey fifty years into the past on a mission to change the events that led to the destruction of Altea's realm.",
              "Archer" : "The Archer is an expert in marksmanship, utilizing bows and arrows in eliminating threats from afar. Aside from this, she is also known for using her own body as a weapon through her display of flexibility, both in evading and performing damaging blows to her enemies at blinding speeds.",
              "Assassin" : "Assassins are melee combat specialists who use Scimitars and Crooks to attack enemies at blinding speeds. He is also adept in fending off enemies from a distance using ninja weapons such as chains, kunais and shurikens. One main feature of Assassins is his ability to meld into the shadows and strike while unnoticed, and can evade incoming attacks with ease.",
              "Cleric" : "The Cleric is a specialist of Light-based magic and protective spells. He utilizes them by empowering his allies or dealing immobilizing attacks against his opponents. In addition to this, these spells can weaken Light resistances of enemies—making a party made purely out of Clerics a viable choice.",
              "Kali" : "The Kali is a mid-ranged fighter who has the ability to summon spirits to aid her in combat or to destroy her opponents. Her fighting style is graceful, employing dance-like movements to weave through the battlefield, although she does not possess the flexibility of an elven Archer. Depending on the specialization chosen by the Kali, she may use her chakrams to rip through the battlefield, or become a summoner of otherworldly spirits and dark energies, which can debilitate any enemy who stands in her way.",
              "Lancea" : "Lancea Charlotte is highly idealistic and has a strong sense of justice. Always ready to help those in need and never afraid of anything, at least until the threat is actually in front of her. She is cheerful, feminine, spontaneous, optimistic, and always has a wide smile to offer. Her good will and confidence are often proved to be a bad match with her clumsiness and denseness. Luckily, she seems to have a very good long-term memory.",
              "Sorc" : "The Sorceress, or alternatively said Angelica, is described by her peers and tutors to have an exceptional talent for magic. However, said talent is wasted on her immature and carefree nature which promps her to under-perform as a magic user and often upsets her tutor Master Sorceress Cynthia. Angelica believes herself to be cunning and imponent, but it's often the opposite.",
              "Warrior" : "The Warrior is a specialist in physical melee combat. Quick and agile, the Warrior relies on fast-paced melee combos! The Warrior comes from Ironwood Forest. Legend has it that he was brought to the town as an infant by his mother under mysterious circumstances. Even as a young boy, he was always quick and strong. As he grew, he found himself easily outstripping his peers in the arts of war. In his heart though, he always longed for the truth of his birth and his lineage and now finds himself on a path of personal discovery."}

advace_class_desc = {"Adept" : "The Adept is a secondary specialization class of the Alchemist, the other being the Physician. Adept makes use of magma created from earth energy and ice with the power of water. Her alchemy traps enemies into inescapable peril.",
              "Physician" : "The Physician is the secondary specialization class of the Alchemist, the other being the Adept. The Physician uses her alchemical knowledge to create her own types of diseases. Get inticed by her viruses and you'll be hitting your ally for no apparent reason.",
              "Gear master" : "The Gear Master is a secondary specialization class of the Engineer, the other being the Shooting Star. Gearmaster specializes in summoning Mecha Ducks and towers. Hard to approach when in battle because of the machines she summons. If you love machines and mechanic stuff, the Gear Master is waiting for you.",
              "Shooting star" : "The Shooting Star is the secondary specialization class of the Engineer, the other being the Gearmaster. Shooting Stars specializes in using bombs and long range attacks. She summons the robot butler, Alfredo to be with her in times of battle. Wherever the Shooting Star go, destruction awaits you.",
              "Temptest" : "The Tempest focuses more of being a DPS or Support class ingame ( depends on your choice ). As a DPS, Tempest can deal short to mid burst of damage to a target w/o compromising the need to escape if needed ( with the help of evade and variety of skills that can be connected to Kick Shot ex ). Unlike her counterpart w/c is the Windwalker, her skills have a shorter animation",
              "Wind walker" : "Windwalkers are mobile attackers. Windwalker is by far the fastest character in game. With the help of showtime ( skill that removes cooldown from her passive skills ) she can clear a dungeon or clear a group of mobs in a very quick manner.",
              "Sniper" : "Being the class that has the longest range in game, your sniper build should be founded into building up damage as high as you can. Having Agility as the class main attribute, you don't have to worry about reaching the highest critical output since sniper is a natural burst damager thanks to Critical Break that increases attack during critical, affected by your critical percentage",
              "Artillery" : "Unlike Snipers, who are focused on physical damage, Artillery are more aligned towards magical damage. Despite being a magic damage-oriented class, it is advisable for Artilleries to learn some skills from the physical skill tree of Bowmasters like Charged Shot and Aerial Chain Shot for dealing with enemies from up close. The player is free to choose among the available utility skills.",
              "Ripper" : "Unlike Ravens, Rippers focuses more of getting closer to the enemies and unleash a barrage of fiery attacks on them. Rippers should also think of getting good equipment and plates with high weapon defense because going closer to the enemy also means they are at risk of receiving damage.",
              "Raven" : "Raven focus on meelee to mid range attacks. Unlike ripper, most of raven's skills are throw and forget type. It is rather easier to play compared to ripper who requires close melee range to dish out the damage. However, raven's side of skill tree lacks damage and therefore is very reliant of the burst damage under the effect of fade",
              "Light fury" : "Although it is said they act as a healer/supporter, Light Furies are also capable of attacking efficently as their overall damage as a Bringer helps them. Do note that when gearing your Light Fury, it is recommended that they are gears to for survivability instead of DPS as Light Furies main role is still to support instead of damage.",
              "Abyss walker" : "The Abyss Walker focuses on improving one's DPS capabilities by boosting the Dark attack of oneself and fellow members in a party, and adds more ways to trap enemies in a area using large AOE and multi-hit skills.",
              "Inquisitor" : "Inquisitors are the DPS specialization of a Priest meaning that they prioritize dealing a more powerful version of light based damage but offering minimal support. Inquisitors invests on spreading Holy hate throughout the entire battlefield by focusing on multiple AOE based light magic damage spells.",
              "Saint" : "Saints prioritize enhancing their healing and buff spells and always makes sure that the party is alive and buffed up for a fight. Because of this Saints are in always if not a member of a Nest or Party Raid. Saints focus on enhancing their relic tree skills to further aid them upon turning the tide of battle into favorable odds be it staggering foes, nullifying movement and re-invigoration of his entire party",
              "Crusader" : "The Crusader is the secondary specialization class of the Paladin, the other being the Guardian. Crusaders focus on dealing burst damage to foes in small range but with huge AoE. They are reputable for being able to dish out large amount of damage in a single hit as well as take a considerable amount of damage",
              "Guardian" : "The Guardian is the secondary specialization class of the Paladin, the other being the Crusader. Guardians excel in keeping themselves alive not in a matter of heal but based on the amount of their HP and great defense and also fortifies his allies with a Guardian bubble whenever a block is successful. Guardians are notable of being the class with the most defensive capabilities",
              "Spirit dancer" : "The Spirit Dancer is the secondary specialization class of the Dancer, the other being the Blade Dancer. The Spirit Dancer specialize in summoning spirits which aid the Dancer in combat instead of confronting enemies head on. It boosts key skills from the Spirit Dance tree and adds two spirit summoning skills, Wide Stinger and Praetor, to attack groups of enemies at once. They are known for their ability to deal burst damage.",
              "Blade dancer" : "The Blade Dancer is the secondary specialization class of the Dancer, the other being the Spirit Dancer. The Blade Dancer focus on melee combat and skills that destroy enemies from up close. Taking up this specialization class strengthens selected skills from the Blade Dance tree and adds two new skills to the Dancer's offensive arsenal.",
              "Soul eater" : "The Soul Eater is the secondary specialization class of the Screamer, the other being the Dark Summoner. The Soul Eater summons spirits to aid her in long ranged combo attacks. Her ability to strengthen her allies' attacks by placing curses and status ailment on her enemies makes her a valuable party support member!",
              "Dark summoner" : "The Dark Summoner is the secondary specialization class of the Screamer, the other being the Soul Eater. The Dark Summoner is a fantastic PvP class, thanks to her powerful mid to long ranged dark attacks and strong combo skills. She can even partially regenerate her health with every attack!",
              "Flurry" : "The Flurry specialization improves more on the capabilities of the Piercer to deal physical damage. Initially, the physical skill tree of the Piercer relies on straightforward melee damage against groups of enemies, and the powerful Vulnerable debuff is only available when using the ultimate Fling Sky. However, Flurries can now learn Spinning Skewer, whose damage is boosted by 1000% when used on Vulnerable mobs, and the chances of inflicting the Vulnerable debuff is increased from once every three minutes to a certain chance while using skills through the Flurry's Class Mastery",
              "Sting breezer" : "The Sting Breezer is the secondary specialization class of the Piercer, the other being the Flurry. Sting Breezer enhances her weapon with magic so enemies do not stand a chance against her, even if her spear does not touch them physically. They are known for their ability to deal high burst damage.",
              "Elestra" : "The Elestra is the secondary specialisation class of the Elemental Lord, the other being the Saleana. Elestras chooses the path of ice magic, boosting their damage potential using ice-based skills. Elestras also learn new skills that they can use to protect themselves while rendering enemies vulnerable to their frigid magic. As specialists of ice magic, Elestras are often given offensive support roles in PvE, but they are also difficult to take down in PvP due to their freezing skills.",
              "Saleana" : "The Saleana is the secondary specialisation class of the Elemental Lord, the other being the Elestra. Saleanas are masters of fire magic, focusing more on destructive skills to burn their foes to a crisp. They are known for their ability to deal burst damage. Due to the nature of their skills, Saleanas are mostly regarded as nukers due to their ability to unleash a torrent of flame onto many foes at once.",
              "Majesty" : "The Majesty is the secondary specialization class of the Force User, the other being the Smasher. The Majestys can use her talent to read enemy’s buffs and steal one to herself with the flick of her wrist. Forget running away too, because she’s got an explosive Gravity Ball to do her long range bidding. An enemy that so much as lays eyes on the Majesty might as well accept its fate.",
              "Smasher" : "The Smasher is the secondary specialization class of the Force User, the other being the Majesty. Smashers are specialists in neutral-element, her powers manifesting as dazzling displays of light that decimate her foes. In exchange for losing the maximum potential of Dark magic in battle, Smashers become purely focused in DPS, gaining the advantage of independence from element restrictions due to the nature of her core spells.",
              "Gladiator" : "Gladiators are the physical path job of the Sword Master. They are able to deliver quick attacks with their excellent swordsmanship. Gladiators are known for their skill [Finish Attack], which allows them to deal additional damage to the original attack depending on how low the enemies HP are",
              "Moonlord" : "The Moonlord is the secondary specialization class of the Swordmaster, the other being the Gladiator. Moonlords focuses on ranged attacks and magic damage. They are known for their ability to release crescent-shaped energy blasts from their swords, allowing them to eliminate enemies from a greater distance.",
              "Barbarian" : "Barbarians are the DPS job of the Mercenary. They are known for their ability to deal burst damage. They are capable of converting their Strength stat into Physical ATK. They are also able to sacrifice some of their HP to further boost their Critical rate and Physical ATK. The main aspect of the Barbarian is the skill [Bone Crash]. When used, the enemies that get hit will receive a debuff, allow further fix damage per hit to be dealt by party members.",
              "Destroyer" : "The Destroyer is the secondary specialization class of the Mercenary, the other being the Barbarian. Destroyers are able to render enemies' heaviest armor about as useful as a raincoat. He manipulates the surrounding energy field to draw foes to him then pounds and pounds until only dust remains."}


questions_icon = {"base_class_q1" : "/static/Form/icons8-holding-hands-64.png",
                            "base_class_q2" : "/static/Form/icons8-christmas-angel-64.png",
                            "base_class_q3" : "/static/Form/icons8-clock-64.png",
                            "base_class_q4" : "/static/Form/icons8-worker-64.png",
                            "base_class_q5" : "/static/Form/icons8-volume-level-64.png",
                            "base_class_q6" : "/static/Form/icons8-fight-96.png",
                            "base_class_q7" : "/static/Form/icons8-chat-64.png",
                            "base_class_q8" : "/static/Form/icons8-sun-90.png",
                            "base_class_q9" : "/static/Form/icons8-rain-90.png",
                            "base_class_q10" : "/static/Form/icons8-settings-100.png"}
