import os, sys, time
import random

budzet = 20
zlykod = 0
kwiatek = False
przekaska = False
saszeta = False
teeth_washed = False
tylko_raz = False
klucz = False
bluza = False
jedenfilm = False



def anim(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def zabki(action):
    global teeth_washed
    os.system("cls")
    if action == "1":
        teeth_washed = True
        anim("Myjesz ząbki i lecisz do szafy, jakim fitem zaskoczysz tym razem?\nWpisz 'szafa' aby pobiec do szafy.\n")
        w5 = input("").lower().strip()
        if w5 == "szafa":
            os.system('cls')
            print("POKÓJ")
        return "1"
    elif action == "2":
        teeth_washed = False
        anim("Nie umyłeś ząbków brudasku!\nWpisz 'szafa' aby pobiec do szafy.\n")
        w5_1 = input("").lower().strip()
        if w5_1 == "szafa":
            os.system('cls')
            print("POKÓJ")
        return "2"

def wybor_spodni():
    anim("Czas przejść do spodni.\nWybierz 1 aby ubrać granatowe joggery.\nWybierz 2 aby ubrać joggery koloru khaki.\n")
    spodnie = input("")
    if spodnie == "1":
        os.system('cls')
        anim("Całkiem luźno, ale przynajmniej wygodnie.\nNapisz 'czas ruszać' aby wyjechać z domu.\n")
        auto1 = input("").lower().strip()
        if auto1 == "czas ruszać":
            os.system('cls')
            print("CORSIA")
    elif spodnie == "2":
        os.system('cls')
        anim(
            "No, no, ale z ciebie elegancik.\nKai na pewno się spodoba ;)\nNapisz 'czas ruszać' aby wyjechać z domu.\n")
        auto2 = input("").lower().strip()
        if auto2 == "czas ruszać":
            os.system('cls')
            print("CORSIA")


def domek():
    print("DOMEK")
    print('''
              ________
             / ______ \\
             || _  _ ||
             ||| || |||
             |||_||_|||
             || _  _o|| (o)
             ||| || |||
             |||_||_|||      ^~^  ,
             ||______||     ('Y') )
            /__________\\    /   \\
    ________|__________|__ (\\|||/) _________
   hjw     /____________\\
   97     |____________|

    ''')
    anim("Gratulacje!\nDotarłeś bezpiecznie do swojej dziewczyny.\n")


def buziak():
    global teeth_washed
    anim("Naciśnij enter aby kontynuować")
    input("")
    os.system('cls')
    anim(
        "Kajka rzuciła ci się w ramiona,\nBardzo za tobą tęskniła.\nCzy chcesz jej dać buziaka na powitanie?\n1. Daj jej soczystego buziaczka\n2. Nie dawaj jej buziaczka")
    buziaczek = input("")
    if buziaczek == "2":
        anim("Jak mogłeś nie wycałować swojej ukochanej, gdy ją zobaczyłeś???\nPRZEGRAŁEŚ!")
        time.sleep(3)
        sys.exit(0)
    elif buziaczek == "1":
        if not teeth_washed:
            anim("Nie umyłeś ząbków!\nZioniesz jak smok!\nPowaliłeś Kaję swoim oddechem.\nPRZEGRAŁEŚ!")
            time.sleep(3)
            sys.exit(0)
        else:
            os.system('cls')
            print('''            .,,,,,,,,,,.
         ,;;;;;;;;;;;;;;,
       ,;;;;;;;;;;;)));;(((,,;;;,,_
      ,;;;;;;;;;;'      |)))))))))))\\
      ;;;;;;/ )''    - /,)))((((((((((\\
      ;;;;' \\        ~|\\  ))))))))))))))))
      /     /         |   (((((((((((((( 
    /'      \\      _/~'    ')|()))))))))
  /'         \\   />     o_/)))(((((((( 
 /          /' ~~(____ /  ()))))))))))
|     ---,   \\        \\     (((((((((( 
          \\   \\~-_____|      ))))))))
            \\  |      |_.---.  

            ''')
            anim(
                "Dałeś Kai buziaczka,\nprzy czym ona nie pozostała ci dłużna na długo hshsh C:\nKliknij enter aby kontynuować")
            input("")
            os.system('cls')


def maro():
    os.system('cls')
    print('''⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣤⣤⣤⣄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠽⠿⡛⢿⣿⣷⡄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣇⠀⣀⢀⠀⢿⣯⡿⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠁⠛⠁⠀⣼⣿⡷⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⠭⣄⠀⠀⣰⣼⠃⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣄⠠⠴⡞⢸⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣀⡠⠄⠾⢡⠄⢠⢃⠞⣷⢄⡀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⡰⠊⡉⠀⠀⠀⠈⢂⡑⣃⠅⠊⠀⠀⠉⠛⠲⢤⠀
⠀⠀⠀⠀⢰⢇⠀⡎⠀⠀⠀⠀⠀⠏⠀⠀⠀⠀⠀⢸⣸⠀⢸⡇
⠀⠀⠀⢠⠃⠻⣟⢧⡀⠀⠀⠀⢸⠀⠀⠀⠀⠀⣀⡼⠁⠀⢸⡇
⠀⠀⠀⢸⠀⢀⡻⠦⠵⠤⢄⣀⣀⡠⠄⢤⣀⣰⣿⠁⠀⠀⠘⡅
⠀⠀⠀⢸⡀⠋⠀⠀⠀⠀⠀⠈⠀⠈⣅⣸⠀⠤⢾⣄⠀⠀⡰⡇
⠀⠀⠀⠘⢧⣀⠀⠀⢀⣀⣠⣴⣞⡉⠁⠀⠀⠀⠈⠉⠀⠐⣿⠀
⠀⠀⠀⠀⠀⠈⢹⣿⡏⠀⣩⠉⠉⠙⠓⠻⠵⢾⣶⣶⣶⠞⠁⠀
⠀⠀⠀⠀⠀⠀⠈⠚⠛⠿⠅⠒⢊⣽⣛⡩⠤⠖⠒⠚⠋⠀⠀⠀
⠠⠀⠠⠶⠶⠶⠶⠶⠖⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⢒''')


def dziewczyna():
    print('''⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⡶⢾⣿⣶⡿⣷⣤⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⡿⣯⣾⣿⣿⣼⣽⣷⡄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⡟⣼⣿⣿⠟⠁⢹⣿⡽⣷⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣀⣠⢾⣿⣿⢇⣿⣿⠏⠀⡠⠄⣿⣧⢹⣇⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠉⣩⣾⣿⠟⣼⣿⡿⠀⠠⢶⡶⠋⢻⣎⣿⣆⠀⠀⠀
⠀⠀⠀⠀⠀⣾⢟⣻⣥⣾⣿⣿⡇⢀⠀⠀⠀⢀⡶⣽⣿⣟⠓⠂⠀
⠀⠀⠀⠀⠀⡿⣾⢱⣾⣷⣿⡟⠀⢚⡒⠀⢀⣾⣿⢹⣿⢿⣄⠀⠀
⠀⠀⠀⠀⠀⠴⣃⣾⣿⣿⠃⣷⣤⣈⣀⡤⢺⣿⣿⣇⢻⡄⠈⠙⠒
⠀⠀⠀⣀⠤⠾⣻⣭⡿⣫⡆⢻⠙⠻⠟⢁⣾⣿⣿⣿⢹⡍⠒⠀⠀
⠀⠀⠀⠀⣠⣿⣿⡿⣴⣿⣷⢸⣇⠀⠀⡾⠋⢹⣿⣿⢸⣿⡄⠀⠀
⠀⠀⠀⣼⣿⠇⣿⡟⣿⣿⣿⢸⢻⠀⢸⠀⠀⣸⡿⣫⣿⢟⣷⠀⠀
⠀⠀⠀⣿⢃⣴⣿⢣⣿⣿⡟⠜⢸⠀⢸⠀⢼⡿⢹⣿⣿⣝⢿⣆⠀
⠀⠀⠾⣿⣿⣿⣿⠿⣿⡿⠃⠀⢸⠀⢸⠀⠘⣿⠀⠉⠻⣿⣷⣿⠀
⠀⠀⠀⢻⣿⢿⣇⣿⣟⠀⠀⠀⡞⢻⡟⢣⠀⣿⡆⢀⣶⠿⢻⡏⠀
⠈⠒⠴⠾⢻⣬⢻⣿⡻⣆⠀⢰⠁⠀⠀⠀⣳⡿⠀⠀⢻⡄⠘⠆⠀
⠀⠀⠀⢰⡿⠟⠋⣻⣿⠃⢀⠎⠀⠀⠈⠉⠉⠀⠀⠀⣼⠇⠀⠀⠀
⠀⠀⢀⣾⠃⠀⣴⠟⠁⢀⡜⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀
⠀⠐⠚⠁⠀⠸⡇⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

''')


def micia():
    print(r'''                      _                        
                      \*-.                    
                       )  _-.                 
                      .  : . .                
                      : _   '  \               
                      ; * _.   *-._          
                      -.-'          -.       
                        ;              .     
                        :.       .        \    
                        . \  .   :   .-'   .   
                        '  +.;  ;  '      :   
                        :  '  |    ;       ;-. 
                        ; '   : :-:     _.* ;
               [bug] .*' /  .*' ; .*- +'  *' 
                     *-*   *-*  *-*'    ''')

def kamien():
    global klucz
    maro()
    anim("Wpisz: kamień, papier, nożyce: ")
    user_choice = input("").lower().strip()
    while user_choice not in ["kamień", "papier", "nożyce"]:
        anim("Nieprawidłowy wybór. Spróbuj ponownie.")
        anim("Wybierz: kamień, papier, nożyce: ")
        user_choice = input("").lower().strip()

    computer_choice = random.choice(["kamień", "papier", "nożyce"])

    anim(f"Twój wybór: {user_choice}")
    anim(f"Wybór Mara: {computer_choice}")

    if user_choice == computer_choice:
        anim("REMIS")
        time.sleep(1)
        anim("Zagrajmy jeszcze raz!\nWcisnij enter aby spróbowac wygrać z Marem")
        input("")
        kamien()
    elif (user_choice == "kamień" and computer_choice == "nożyce") or \
            (user_choice == "papier" and computer_choice == "kamień") or \
            (user_choice == "nożyce" and computer_choice == "papier"):
        anim("WYGRAŁEŚ!")
        anim("> Aaaaaa to niesprawiedliwe, na pewno oszukiwałeś.\n")
        time.sleep(1)
        anim("No ale trudno słowo się rzekło. Proszę to dla ciebie.\nWciśnij enter aby zobaczyć co wygrałeś!")
        input("")
        os.system('cls')
        print("Dostałeś od Marka klucz, ciekawe co otwiera.")
        print("")
        print("")
        print('''     8 8 8 8                     ,ooo.
     8a8 8a8                    oP   ?b
    d888a888zzzzzzzzzzzzzzzzzzzz8     8b
     ""^""'                    ?o___oP''')
        klucz = True
        print("")
        anim("Wciśnij enter aby wyjść z pokoju")
        input("")
        menu()
    else:
        anim("PRZEGRAŁEŚ!\nWciśnij enter aby spróbować pokonać Mara")
        input("")
        kamien()

def gra():
    maro()
    anim("> Cześć!")
    input("> ")
    anim("> Jak tam u ciebie, jak w pracy?")
    input("> ")
    anim("> A tak w ogóle, widziałeś jak nasi skaczą? To już nie to samo co kiedyś.")
    input("> ")
    anim("> Chcesz usłyszeć zagadkę?")
    time.sleep(2)
    anim("Ma mnie każdy lecz nie każdy lubi – potrafisz uwierzyć?")
    time.sleep(1)
    anim("Możesz mnie zobaczyć, lecz nie zdołasz uderzyć.")
    time.sleep(1)
    anim("Bawię dziecko, przygnębiam starca, cieszę dziewcze urocze.")
    time.sleep(1)
    anim("Kiedy płaczesz – ja szlocham, gdy się śmiejesz – i ja chichoczę.")
    time.sleep(1)
    anim("Czym jestem")
    odpowiedz = input("> ").lower().strip()
    if odpowiedz == "odbicie":
        anim("> Brawo hah, nie sądziłem że uda ci się zgadnąć!")
    else:
        anim("> Nie zgadłeś ale to bardzo trudna zagadka więc spokojnie hah")
        anim("Odpowiedź brzmi: Odbicie")
    anim("Podobała ci się zagadka?")
    input("> ")
    anim(
        "To może teraz zagramy w kamień papier nożyce?\nJeżeli wygrasz dam ci coś w sekrecie.\nTYLKO NIE MÓW KAI\n> 1. Chętnie z tobą zagram")
    zagraj = input("")
    if zagraj == "1":
        kamien()

def src_pokoj():
    global zlykod
    global tylko_raz
    os.system("cls")
    anim("Potrzebujesz kodu, czy chcesz kontynuować?\n1. Tak\n2. Nie")
    kod1 = input("")
    if kod1 == "2":
        menu()
    elif kod1 == "1":
        os.system("cls")
        time.sleep(2)
        anim("Masz 2 próby\nWpisz kod:")
        kod = input("")
        if tylko_raz:
            os.system('cls')
            time.sleep(2)
            anim("Chyba już raz to zobaczyłaś w tej grze hshshsh")
            time.sleep(2)
            menu()
        elif zlykod == 2:
            os.system('cls')
            anim("Wpisałeś zły kod 2 razy,\n nie możesz już dostać się do tego pokoju ://")
            menu()
        elif kod == "29.11.2023":
            os.system('cls')
            time.sleep(3)
            anim("Gratuluję! Udało ci się wejść do pokoju!")
            time.sleep(2)
            anim("Nie było to łatwe wyzwanie.")
            time.sleep(1)
            anim("Naciśnij enter aby kontynuować")
            input("")
            tylko_raz = True
            menu()
        else:
            zlykod += 1
            os.system("cls")
            anim("Nie prawidłowy kod")
            time.sleep(1)
            menu()
    elif kod1 == "2":
        menu()

def salon():
    os.system("cls")
    if klucz == False:
        print(r'''        888d8b        d8b                                                     
        888Y8P        Y8P                                                     
        888                                                                   
        888888888  88888888888b.  .d88b. 888d888 .d88b.  .d88b. 88888b.d88b.  
        888888888  888888888 "88bd88P"88b888P"  d88""88bd88""88b888 "888 "88b 
        888888Y88  88P888888  888888  888888    888  888888  888888  888  888 
        888888 Y8bd8P 888888  888Y88b 888888    Y88..88PY88..88P888  888  888 
        888888  Y88P  888888  888 "Y88888888     "Y88P"  "Y88P" 888  888  888 
                                    888                                     
                                Y8b d88P                                     
                                "Y88P" 

                                ''')
        anim(
            "Znalazłeś się w salonie, w telewizji pokazują skoki narciarskie,\nsiadasz sobie na kanapie i po chwili słyszysz męski głos.\nWciśnij enter aby kontynuować")
        input("")
        os.system("cls")
        maro()
        anim("To teściu Marek, czy chcesz sie z nim przywitać?\n1. Olej go\n2. Przywitaj się z Marem")
        przywitanie1 = input("")
        if przywitanie1 == "1":
            maro()
            anim(">Wstań chłopcze!")
            time.sleep(2)
            anim("Maro zwrócił ci uwagę teraz to już musisz wstać.\nWcisnij enter aby kontynuować")
            input("")
            gra()
        if przywitanie1 == "2":
            gra()
    else:
        anim("Już byłeś w tym pokoju")
        time.sleep(2)
        menu()

def szkatulka():
    print('''888                      
888                      
888                      
88888b.  .d88b. 888  888 
888 "88bd88""88bY8bd8P' 
888  888888  888  X88K   
888 d88PY88..88P.d8""8b. 
88888P"  "Y88P" 888  888 

''')

def choice_Kai():
    global saszeta
    os.system("cls")
    anim("Jesteś w pokoju Kai. Co chcesz zrobić?")
    anim("1. Połóż się do łóżka\n2. Podejdź do biurka\n3. Włącz telewizor\n4. Nakarm micie\n5. Zmień pokój")
    pkwybor = input("")
    os.system("cls")
    if pkwybor == "1":
        anim("Upsss, położyłeś się dosłownie na chwilkę a już rozkopałeś Kai łóżko.")
        anim("Raczej nie będzie zadowolona hah")
        anim("Naciśnij enter aby kontynuować")
        input("")
        choice_Kai()
    elif pkwybor == "2":
        os.system("cls")
        szkatulka()
        anim(
            "Podchodząc do biurka widzisz szkatułkę, która cię zainteresowała.\n1. Spróbuj otworzyć\n2. Zostaw w spokoju")
        otwieranie = input("")
        os.system("cls")
        if otwieranie == "1":
            if klucz == True:
                anim("Udało ci się otworzyć szkatułkę! W środku widzisz jakąś karteczkę.\nKliknij enter aby kontynuować")
                input("")
                os.system("cls")
                print(r''' ___     ___      __   __      ___     ___    ___    ____   
|__ \   / _ \    /_ | /_ |    |__ \   / _ \  |__ \  |___ \  
   ) | | (_) |    | |  | |       ) | | | | |    ) |   __) | 
  / /   \__, |    | |  | |      / /  | | | |   / /   |__ <  
 / /_     / /   __| |  | |  __ / /_  | |_| |  / /_   ___) | 
|____|   /_/   (__)_|  |_| (__)____|  \___/  |____| |____/  



                                                            ''')
                anim("To jakiś kod! Lepiej go zapamiętać, może się do czegoś przydać!\nWciśnij enter aby kontynuować")
                input("")
                choice_Kai()
            else:
                anim("Nie masz klucza aby otworzyć zamek\nWciśnij enter aby kontynuować")
                input("")
                choice_Kai()
        elif otwieranie == "2":
            choice_Kai()
    elif pkwybor == "3":
        os.system("cls")
        anim("Włączyłeś telewizor ale zapomniałeś, że nie ma tam dekodera hahah\n Wciśnij enter aby kontynuować")
        input("")
        choice_Kai()
    elif pkwybor == "4":
        os.system("cls")
        if saszeta == False:
            micia()
            anim(
                "Micia przyszła do ciebie i zrobiła 'a, a, a' prosząc o jedzonko,\n ale nie kupiłeś saszety w sklepie,\nwięc musisz teraz jakoś znieść jej lamentowanie głodomorka :C\nWciśnij enter aby kontynuować")
            input("")
            choice_Kai()
        else:
            micia()
            anim(
                "Micia przyszła do ciebie, zrobiła 'a, a, a' prosząc o jedzonko.\nDobrze że kupiłeś tą saszetę hshs\nWciśnij enter aby kontynuować")
            input("")
            choice_Kai()
    elif pkwybor == "5":
        menu()

def koniec():
    os.system("cls")
    time.sleep(1)
    if bluza == True:
        anim("KONIEC GRY")
        time.sleep(3)
        print("")
        anim("Jak podejrzewałeś wróciłeś do domu bez bluzy.\nUrooocze\nGratuluję przejścia gry.\nMam nadzieję że ci się podobała C:")
        print("")
        print("")
        print("")
        time.sleep(2)
        anim("Autor gry i wykonawca:")
        anim("Daniel Segeth")
        print("")
        time.sleep(2)
        anim("Wciśnij enter aby zakończyć grę.")
        input()
        sys.exit(0)
    else:
        anim("KONIEC GRY")
        time.sleep(3)
        print("")
        anim("Gratuluję przejścia gry.\nMam nadzieję że ci się podobała C:")
        time.sleep(2)
        print("")
        print("")
        print("")
        anim("Autor gry i wykonawca:")
        anim("Daniel Segeth")
        time.sleep(2)
        print("")
        anim("Wciśnij enter aby zakończyć grę.")
        input()
        sys.exit(0)

def menuakc():
    global jedenfilm
    os.system("cls")
    anim("1. Obejrzycie razem film\n2. Polóżcie się do łóżka i się poprzytulajcie")
    akc = input("")
    os.system("cls")
    if akc == "1":
        if jedenfilm == True:
            anim("Już oglądaliście razem film")
            time.sleep(2)
            menuakc()
        else:
            if przekaska == True:
                anim("Otwieracie cziperki i włączcie telewizor, jako że ty kupiłeś przekąski możesz wybrać co będzecie oglądać.")
                anim("1. Atack on Titan\n2. Dzień Świra\n3. Rybki z ferajny")
                film = input("")
                os.system("cls")
                if film == "1":
                    anim("Oglądacie to arcydzieło Kaja ma mindfucka nikt się niczego nie spodział ale buja.\nOboje płaczecie na końcówce.")
                    time.sleep(3)
                    jedenfilm = True
                    menuakc()
                elif film == "2":
                    anim("Wybrałeś bardzo cięzki i dołujący film,\nno ale grzechem byłoby nie znać takiego arcydzieła więc oglądacie go razem.\nOboje płaczecie na końcówce")
                    time.sleep(3)
                    jedenfilm = True
                    menuakc()
                elif film == "3":
                    anim("Bardzo fajna, ciekawa, niekonwencjonalna bajka.\nGłówną postać dubbinguje Cezary Pazura\nOglądacie Rybki z Ferajny i widzisz po twarzy Kai że jej się podobało.")
                    time.sleep(3)
                    jedenfilm = True
                    menuakc()
            else:
                anim("Nie kupiłeś przekąsek, nie masz żadnego asa w rękawie i Kaja wybrała na ten wieczór Vincenzo.\nTrochę nad tym ubolewasz ale wiesz, że sprawi jej to ogromą przyjemność\ngdy będzie mogła to z tobą zobaczyć")
                time.sleep(3)
                jedenfilm = True
                menuakc()
    elif akc == "2":
        if bluza == True:
            anim("Kładziecie się razem do łóżka.\nKaja zaczyna cię obwąchiwać.\nJuż wiesz, że wyjedziesz stąd bez bluzy hshsh")
            input("")
            koniec()
        else:
            anim("Kładziecie się do łóżka.\nKaja się w ciebie wtula i zasypia, oby ta chwila trwała wiecznie,\nale niestety jesteś już na finiszu gry.\nWciśnij enter aby kontynuować")
            input("")
            koniec()

def menu():
    os.system("cls")
    time.sleep(1)
    anim("1. Spędź czas z Kają\n2. Pójdź do salonu\n3. Pójdź do pokoju od Kai\n4. Przejdź do sekretnego pokoju")
    pokoje = input("")
    if pokoje == "4":
        src_pokoj()
    elif pokoje == "2":
        salon()
    elif pokoje == "3":
        choice_Kai()
    elif pokoje == "1":
        os.system("cls")
        anim("Wchodzisz do pokoju Kai a ona już tam na ciebie czeka.")
        time.sleep(2)
        os.system("cls")
        dziewczyna()
        anim("> No w końcu hshshs\nNie mogłam się ciebie doczekać.")
        anim("Co dla nas dzisiaj zaplanowałeś?\nWciśnij enter aby kontynuować")
        input("")
        menuakc()

