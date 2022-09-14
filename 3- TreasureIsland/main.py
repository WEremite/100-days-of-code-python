print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

# Write your code below this line 👇
print("""
    You've woken up and found yourself next to dark scary woods. Woooooo! Sounds from forest.
    You frightened shrugged your shoulders and saw two roads which were hidden in grass.
""")
choice1 = input("Where are going to go? (left or right) ").lower()

if choice1 == "left":
    print("""
        You turned left and go into the dark...
        After a while you went to big lake. At the other shore you can see a wooden ferry.
    """)
    choice2 = input("Are you going to swim or wait for the ferry? (swim or wait) ").lower()
    if choice2 == "wait":
        print("""
            While you have been waiting you saw a house with three doors - 
            Red, Yellow and Blue. You came close and held your hand to door handle...
        """)
        choice3 = input("You choose (yellow, red, blue or wait) ")
        if choice3 == "yellow":
            print("""
                
                            _.--.
                        _.-'_:-'||
                    _.-'_.-::::'||
               _.-:'_.-::::::'  ||
             .'`-.-:::::::'     ||
            /.'`;|:::::::'      ||_
           ||   ||::::::'     _.;._'-._
           ||   ||:::::'  _.-!oo @.!-._'-.
           \'.  ||:::::.-!()oo @!()@.-'_.|
            '.'-;|:.-'.&$@.& ()$%-'o.' U||
              `>'-.!@%()@'@_%-'_.-o _.|'||
               ||-._'-.@.-'_.-' _.-o  |'||
               ||=[ '-._.- U/.-'    o |'||
               || '-.]=|| |'|      o  |'||
               ||      || |'|        _| ';
               ||      || |'|    _.-'_.-'
               |'-._   || |'|_.-'_.-'
                '-._'-.|| |' `_.-'
                    '-.||_/.-'
                    
                Hooray! You found a treasure chest!!!
                You win!!!
                """)
        elif choice3 == "red":
            print("""
                
            
                           (  .      )
                       )           (              )
                             .  '   .   '  .  '  .
                    (    , )       (.   )  (   ',    )
                     .' ) ( . )    ,  ( ,     )   ( .
                  ). , ( .   (  ) ( , ')  .' (  ,    )
                 (_,) . ), ) _) _,')  (, ) '. )  ,. (' )
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                You was burned to death by fire trap!
                Game Over!
            """)
        elif choice3 == "blue":
            print("""
                
                   (    )
                  ((((()))
                  |o\ /o)|
                  ( (  _')
                   (._.  /\__
                  ,\___,/ '  ')
    '.,_,,       (  .- .   .    )
     \   \      ( '        )(    )
      \   \    \.  _.__ ____( .  |
       \  /\   .(   .'  /\  '.  )
        \(  \.-' ( /    \/    \)
         '  ()) _'.-|/\/\/\/\/\|
             '\ .( |\/\/\/\/\/|
               '((  \    /\    /
               ((((  '.__\/__.')
                ((,) /   ((()   )
                 "..-,  (()("   /
                 _//.   ((() ."
          _____ //,/" ___ ((( ', ___
                           ((  )
                            / /
                          _/,/'
                        /,/,"
                        
                Crazy beast with axe jumped at you and cut in half!!!
                Game Over!
            """)
        else:
            print("""
                You decided to not open any doors and wait for a ferry.
                When ferry came you saw that it was a vampire.
                
                             /######\
                           /##########\
                          /   \###/    \
                         /     \#/      \
                      /\|               |/\
                      | | \ ==\    /== / | |
                       \|  \<|>\  /<|>/  |/     /|
                \__     |    -   \  -    |     /#|
                 \#\     |        |      |   /###|
                  \##\   |       \|     |  /#####|
                   \###\  |   _______  | /######|
                    \####\ | / \/ \/ \|/#######|
                    |######\|        |#########|
                    |########\______/##########|
                    |#########\    /##########/
                    |##########\  |#########/\
                    /###########\/########/###\
                /################\######/########\
               /##################\###/###########\
              /###################\#/##############\
             /####################/#################\
            /###################/####################\
            
            He bit you and you become a monster!
            Game Over!
            """)
    else:
        print("""
                                   
                       ._.-.\
                     _.-'=. \\
                 .-._.-=-..' \'.
               _.--._-='.'   |  `.
              _`.-.`=-./'.-. / .- \
              _.-=-=-/ | '._)`(_.'|
              _.--=.'  `. (.-v-.)/
              _.-.' \-.' `-..-..'
             .-.'      `.'  " ".
            /   )        \  /   \
           /   /\                \
         .'  .'\ `.        .'     \
        /   /   \  `-    -' .`.    .
      .''\.'    | `.      .'   `.   \
     /   |      |      .'/       `.- `.
    |   /       / `.    |         \   |
    |  /       |       .'.         `. |
    / /       /           \          \ \
   /  |      /             \         |  `.
  /   `.     |      `   .'  \        /    \
 ///.-'.\    |       \ /    `\      / /-.  \
 \\\\   `     \.-     |    `-.\     '/   \\\\
  \\\|        |      / \      |          ////
   '''        |     /   \     |          |//
              |.-  |     \  .-|          ''
              /    |    / ` ../
              |'   /    |    /
              \.'  |    | `./
              /    \   /    \
              \ `. /   \    /
               |  |     '. '
               /  |      |  \
              /   |      /   `.
             | | | \   .'  `.. \
            / / / ._`. \.'-. \`/
            |/ / /  `'  `  |/|/
             \|\|
             
             You went to swim and was attacked by water monster. You tried to fight but
             he was very strong.
             Game Over!
        """)
else:
    print("""
      /^\      /^\
      |  \    /  |
      ||\ \../ /||
      )'        `(
     ,;`w,    ,w';,
     ;,  ) __ (  ,;
      ;  \(\/)/  ;;
     ;|  |vwwv|    ``-...
      ;  `lwwl'   ;      ```''-.
     ;| ; `""' ; ;              `.
      ;         ,   ,          , |
      '  ;      ;   l    .     | |
      ;    ,  ,    |,-,._|      \;
       ;  ; `' ;   '    \ `\     \;
       |  |    |  |     |   |    |;
       |  ;    ;  |      \   \   (;
       | |      | l       | | \  |
       | |      | |       | |  ) |
       | |      | ;       | |  | |
       ; ,      : ,      ,_.'  | |
      :__'      | |           ,_.'
               `--'
    You've been eaten by wolf. Wooooo!
    Game Over!
    """)
