import funkcje
import os, sys, time

print('''                                                           
888                                888                           
888                                888                            
888 .d88b. 888  888 .d88b. .d8888b 888888 .d88b. 888d888888  888 
888d88""88b888  888d8P  Y8b88K     888   d88""88b888P"  888  888 
888888  888Y88  88P88888888"Y8888b.888   888  888888    888  888 
888Y88..88P Y8bd8P Y8b.         X88Y88b. Y88..88P888    Y88b 888 
888 "Y88P"   Y88P   "Y8888  88888P' "Y888 "Y88P" 888     "Y88888 
                                                             888 
                                                        Y8b d88P  
                                                         "Y88P"
''')

time.sleep(2)
funkcje.anim(
    "Witaj w symulacji związku! Wciel się w rolę bohatera i podejmuj decyzje,\nktóre wpłyną na relacje pomiędzy bohaterami.\nZ wszystkich opcji możesz wybrać tylko jedną, wyborów dokonuj ostrożnie, gdyż będą miały swoje konsekwencje.\nPowodzenia!\nWciśnij enter aby kontynuować.")
input("")
os.system("cls")

funkcje.anim(
    "Jest sobota a twoja ukochana dziewczyna za tobą tęskni,\ndopiero co wstałeś po ciężkiej nocy grania na komputerze – co robisz?")
funkcje.anim(
    "1. Olewasz swoją ukochaną, bo masz ważniejsze rzeczy na głowie.\n2. Rzucasz wszystko i pędzisz do Kai (swojej dziewczyny).")
w1 = input("")
if w1 == "1":
    os.system("cls")
    funkcje.anim("PRZEGRAŁEŚ!\nDokonałeś najgorszego możliwego wyboru :C")
    time.sleep(2)
    sys.exit(0)
elif w1 == "2":
    os.system('cls')
    funkcje.anim(
        "To był dobry wybór, Kaja na pewno ucieszy się z twojego przyjazdu.\nPrzed wyjazdem musisz zastanowić się, co zjeść na śniadanie.\nWpisz 'kuchnia' aby przejść do kuchni.")
    w2 = input("").lower().strip()
    if w2 == "kuchnia":
        os.system('cls')
        print("KUCHNIA")
        print(r'''  <   |  <   |  <   |   | |  | |  | | |  | |      |()|     /  |  |  |
   )  |   )  |   )  |   | |  | |  | | |  | |      |  |     |  |  |  |
   )()|   )()|   )()|   |o|  | |  | | |  | |      |  |     |  |  |()|
   )()|   )()|   )()|   |o|  | |  | | |  | |      |  |     |  |  |()|
  <___|  <___|  <___|   |\|  | |  | | |  | |      |  |     |  |  |__|
   }  |   || |   =  |   | |  | |  -|-\'  | |      |  |     |  |  |   L
   }  |   || |   =  |   | |  | |   /A\\   | |      |  |     |  |  |   J
   }  |   || |   =  |   |/   | |   |H|   | |      |  |     |  |  |    L
   }  |   || |   =  |        | |   |H|   | |     _|__|_    |  |  |    J
   }  |   || |   =  |        | |   \V/   | |    | |   |    |  |  | A   L
   }  |   FF |   =  |        | |    "    | |    | |   |     \ |  | H   J
   }  |   LL |    = |       _F J_       _F J_   \  --|       |  | H H  L
   }  |   LL |     \|     /       \   /       \  .___|       |  | H H A J
   }  |   \ |           J         L  |  _   _  |              |  | H H U L
   }  |    \|           J         F  | | | | | |             /   | U ".-'
    } |     \|            \       /  | | | | | |    .-.-.-.-/    |_.-'
     \|                    -._.-'   | | | | | |   ( (-(-(-( )
                                     -' -' -'    ----

                                     ''')
        funkcje.anim(
            "Jesteś w kuchni, podchodzisz do lodówki i zastanawiasz się, co chcesz zjeść.\n1. Przejdź do półki z nabiałem.\n2. Przejdź do półki z wędlinami.\n3. Zauważasz pizzę z wczoraj i wsuwasz ją aż ci się uszy trzęsą.")
        lodowka = input("")
        if lodowka == "1":
            os.system('cls')
            funkcje.anim(
                "Zobaczyłeś jajka – są pożywne i na pewno dadzą ci dużo energii. Robisz sobie jajecznicę.\nCzy chcesz umyć zęby?\n1. Umyj ząbki\n2. Nie myj ząbków")
            w4 = input("")
            funkcje.zabki(w4)
        elif lodowka == "2":
            os.system('cls')
            funkcje.anim(
                "Jest tutaj wiele rodzajów szynki i kiełbasek.\n1. Chcesz zjeść coś na szybko\n2. Czy masz zamiar zabawić trochę w kuchni?")
            lodowka_1 = input("")
            if lodowka_1 == "1":
                os.system('cls')
                funkcje.anim(
                    "Wcinasz zimne parówki popijając sokiem, czy chcesz umyć zęby?\nCzy chcesz umyć zęby?\n1. Umyj ząbki\n2. Nie myj ząbków")
                lodowka_2 = input("")
                funkcje.zabki(lodowka_2)
            elif lodowka_1 == "2":
                os.system('cls')
                funkcje.anim(
                    "Smarzysz sobie kiełbaski z cebulką.\nMmmmmmmmmm – pyszności!\nCzy chcesz umyć zęby?\n1. Umyj ząbki\n2. Nie myj ząbków")
                lodowka_3 = input("")
                funkcje.zabki(lodowka_3)
        elif lodowka == "3":
            os.system('cls')
            funkcje.anim(
                "Najadłeś się dużo sosu czosnkowego, czy masz zamiar coś z tym zrobić?\nCzy chcesz umyć zęby?\n1. Umyj ząbki\n2. Nie myj ząbków")
            pizza = input("")
            funkcje.zabki(pizza)

print(r''' 
__________________________________________________________________________________
_______O____________________________________________O____________________________/
\______%____________________________________________%___________________________/
 \_____%__o______________________________________o__%__________________________/
  \____%__%______________________________________%__%_________________________/
  |    %  %                                      %  %       [|_|_|_|_|_|]     |
  |    %  %                                      %  %       [_|_|_|_|_|_]     |
  |    %  %            ~@~@~@~@~@~@~@~           %  %       [|_|_|_|_|_|]     |
  |    %  %           *(=(=(=(=)=)=)=)*          %  %       [_|_|_|_|_|_]     |
  |    %  %        _   :|!|:!|!|!:|!|:   _       %  %    _  [|_|~@@@~|_|]  _  |
  |    %  %       /_\  !:|:!:}|{:!:|:!  /_\      %  %   /_\ [_|_|_|_|_|_] /_\ |
  |    %  %       =|=  |!:|!} | {!|:!|  =|=      %  %   =|= [|_|_|_|_|_|] =|= |
  |    %  %            !:!:}  |  {:!:!           %  %       [_|_|_|_|_|_]     |
  |    %  %            ~@~'---+---~@~           %  %   ___/_|_|_|_|_|_|_\___ |
  |    %  %            |:|    |    |:|           %  %  '====================='|
  |    %  o____________:!:____|____:!:_____.-=---o  %   [_|_]===========[_|_] |
  |    % /                                 \      \ %   [___]           [___] |
  |    O/___________________________________\.-=.--\O   [_|_] o  (,  o [_|_] |
  |    |_____________________________________~~~~~~~|   [___] |  ( )  | [___] |
  |____!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!___[_|_]/!\_@@@_/!\[_lc]_|
  /====!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!=========================\
 /==========_==================================================================\
/=========/ /\==================================================================\
=========/_/ /\==================================================================\
=========| \/ /\==================================================================\
=========|\ \/ /\==================================================================\
=========||\ \/====================================================================\
=========||=\ \/=====================================================================\
=========||==\_\======================================================================\
======================================================================================================\
''')
funkcje.anim(
    "Jesteś w swoim pokoju.\nPatrząc po półkach zauważasz, że masz do wyboru tylko parę czystych białych koszulek,\n2 pary spodni, 2 koszule w kratę, które możesz ubrać i 1 bluzę,\nktórą prawdopodobnie stracisz po przyjeździe hshshsh.\nWybierz 1 aby ubrać bluzę\nWybierz 2 aby ubrać czerwonobiałą grubą flanelę\nWybierz 3 aby ubrać czarną koszulę w kratę.")
szafa = input("")
if szafa in ["1", "2", "3"]:
    os.system('cls')
    if szafa == "1":
        funkcje.bluza = True
        funkcje.anim(
            "Odważny wybór\nJuż teraz kończą ci się ubrania, a jednak postawiłeś wszystko na ostatnią kartę.\n")
    elif szafa == "2":
        funkcje.anim("Ciepło i wygodnie\nCałkiem dobry wybór.\n")
    elif szafa == "3":
        funkcje.anim("Czarny nigdy nie wyjdzie z mody! Dobry wybór!\n")
    funkcje.wybor_spodni()
os.system('cls')
print("CORSIA")
print(r'''                                 _..-------++._
                             _.-'/ |      _||  "--._ 
                       __.--'._/_\j_____/_||___\    ----.
                  _.--'_____    |          \     _____    /
                _j    /,---.\   |        =o |   /,---.\   |_
               [__]==// .-. \\=============/== // .-. \\=[__]
                 -._|\ -' /|___\_________/___|\ -' /|_.'
                       ---'                     ---
                       ''')
funkcje.anim(
    "Tak sobie jadąc do swojej ukochanej zauważasz sklep.\nCzy zamierzasz do niego wejść i kupić co nieco?\nWybierz 1 aby wejść do sklepu.\nWybierz 2 aby kontynuować podróż autem.")
droga = input("")
if droga == "2":
    os.system('cls')
    funkcje.domek()
elif droga == "1":
    os.system('cls')
    print('''   ad88                                     
  d8"                                       
  88                                        
MM88MMM 8b,dPPYba,  ,adPPYba,   ,adPPYb,d8  
  88    88P'   "Y8 a8"     "8a a8"    Y88  
  88    88         8b       d8 8b       88  
  88    88         "8a,   ,a8" "8a,   ,d88  
  88    88          "YbbdP"'   "YbbdP"Y8  
                                aa,    ,88  
                                 "Y8bbdP" 

                                ''')
    funkcje.anim(
        "Jesteś biednym studentem, do wydania masz 20zł.\nChodząc po alejkach zauważasz stoisko z kwiatami.\nCzy chcesz kupić kwiatek? (10zł)\n1. Kup kwiatek\n2. Nie kupuj")
    a1 = input("")
    if a1 == "1":
        os.system('cls')
        funkcje.kwiatek = True
        funkcje.budzet -= 10
        funkcje.anim("Kupiłeś kwiatek, Kaja na pewno będzie zadowolona C:")
        funkcje.anim(f"Zostało ci do wydania {funkcje.budzet}zł.\nWciśnij enter aby kontynuować.")
        input("")
        os.system('cls')
    elif a1 == "2":
        os.system('cls')
        funkcje.anim(
            "Nie kupiłeś kwiatka, ale przynajmniej zaoszczędziłeś trochę grosza.")
        funkcje.anim(f"Zostało ci do wydania {funkcje.budzet}zł.\nWciśnij enter aby kontynuować.")
        input("")
        os.system('cls')

    funkcje.anim(
        "Idąc dalej natrafiasz na alejkę z przekąskami,\nw oczka wpadają ci cziperki chacalaka smak afryki (8zł).\nCzy chcesz kupić cziperki?\n1. Kup cziperki\n2. Nie kupuj cziperków")
    cziperki = input("")
    if cziperki == "1":
        funkcje.przekaska = True
        funkcje.budzet -= 8
        os.system('cls')
        funkcje.anim("Kupiłeś cziperki\nBędzie co chrupać :D")
        funkcje.anim(f"Zostało ci do wydania {funkcje.budzet}zł.\nWciśnij enter aby kontynuować.")
        input("")
        os.system('cls')
    elif cziperki == "2":
        os.system("cls")
        funkcje.anim("Nie kupiłeś cziperków, ale zaoszczędziłeś troche kaski")
        funkcje.anim(f"Zostało ci do wydania {funkcje.budzet}zł.\nWciśnij enter aby kontynuować.")
        input("")
        os.system('cls')

    funkcje.anim("Obchodząc sklep trafiasz do ostatniej alejki.\n")
    time.sleep(2)
    funkcje.anim(
        "Trafiłeś do alejki dla zwierząt.\nZastanawiasz się, czy kupić coś dla Mici.\nZauważasz jej ulubioną saszetę (5zł).\n1. Kup saszetę\n2. Nie kupuj")
    saszeta_input = input("")
    if saszeta_input == "1":
        if funkcje.budzet < 5:
            os.system('cls')
            funkcje.anim(
                "Przy kasie zabrakło ci pieniędzy.\nJest ci strasznie głupio przy pani kasjerce,\nmusisz wybrać którą rzecz chcesz zostawić przy kasie ://\n1. Zostaw Kwiatek\n2. Zostaw Cziperki\n3. Zostaw Saszetę")
            wybor_sklep = input("")
            if wybor_sklep == "1":
                os.system('cls')
                funkcje.kwiatek = False
                funkcje.saszeta = True
                funkcje.przekaska = True
                funkcje.budzet += 10
                funkcje.anim(
                    "Zostawiłeś kwiatek.\nMyślę, że Kaja tego nie przeżyje :C\nWciśnij enter aby pojechać do Kai.")
                input("")
            elif wybor_sklep == "2":
                os.system('cls')
                funkcje.przekaska = False
                funkcje.saszeta = True
                funkcje.kwiatek = True
                funkcje.budzet += 8
                funkcje.anim(
                    "Zostawiłeś Cziperki.\nOby Kaja miała coś do jedzenia.\nWciśnij enter aby pojechać do Kai.")
                input("")
            elif wybor_sklep == "3":
                os.system('cls')
                funkcje.saszeta = False
                funkcje.kwiatek = True
                funkcje.przekaska = True
                funkcje.anim("Kot cię chyba rozszarpie, buahahaha\nWciśnij enter aby pojechać do Kai.")
                input("")
        else:
            os.system('cls')
            funkcje.saszeta = True
            funkcje.budzet -= 5
            funkcje.anim("Kupiłeś saszetę, micia na pewno jest już bardzo głodna.")
            funkcje.anim(f"Zostało ci {funkcje.budzet}zł.\nWciśnij enter aby pojechać do Kai.")
            input("")
    elif saszeta_input == "2":
        os.system('cls')
        funkcje.anim(
            "Nie kupiłeś saszety, oby cię micia nie rozszarpała za to hahah.\nWciśnij enter aby pojechać do Kai.")
        input("")
    os.system("cls")
    funkcje.domek()

funkcje.anim("Tylko zadzwoniłeś dzwonkiem, otwiera się okno, a z niego wychyla się głowa.")
time.sleep(3)
os.system('cls')
funkcje.dziewczyna()
funkcje.anim("> A co ty tutaj robisz???\nOdpowiedź Kai, wpisz coś:")
input(">")
time.sleep(1)
funkcje.anim("> Zaskoczyłeś mnie!!")
time.sleep(1)
funkcje.anim(
    "A ja taka nie pomalowana. Mogłeś powiedzieć!!\nBym przynajmniej włosy umyła.\nWchodź, ale ostrzegam, że mam syf w domu.\nKliknij enter aby kontynuować.")
input("")
os.system('cls')
funkcje.anim("Podbiega do ciebie Kaja, Micia i Moris\nWpisz, z kim chcesz przywitać się najpierw:")
przywitanie = input("").lower().strip()
os.system('cls')
if przywitanie in ["moris", "micia"]:
    if a1 == "2":
        funkcje.anim(
            "Twoja ukochana jest na ciebie zła.\nMogłeś najpierw przywitać się z Kają, a później z resztą :C\nPRZEGRAŁEŚ!")
        time.sleep(3)
        sys.exit(0)
    elif funkcje.kwiatek == True:
        funkcje.anim(
            'Kaja się obraziła, czy chcesz ją "odbrazić" wręczając jej kwiatek?\n1. Odbraź Kaję\n2. Nie odbrażaj Kai')
        odbrazanie = input("").lower().strip()
        os.system('cls')
        if odbrazanie == "1":
            funkcje.kwiatek = False
            funkcje.anim("Kaja już się na ciebie nie gniewa.\nCałe szczęście, że kupiłeś ten kwiatek C:")
            funkcje.buziak()
        elif odbrazanie == "2":
            funkcje.anim("Kaja jest na ciebie zła.\nMogłeś postarać się lepiej :C\nPRZEGRAŁEŚ!")
            time.sleep(3)
            sys.exit(0)
elif przywitanie == "Kaja":
    funkcje.dziewczyna()
    funkcje.anim(">Wiedziałam, że mnie wybierzesz od samego początku hshsh.")
    funkcje.buziak()
funkcje.dziewczyna()
funkcje.anim("Wchodź do środka, tylko uważaj żeby nie wypuścić mici.\nKliknij enter aby kontynuować")
input("")
os.system('cls')
funkcje.anim(
    "Jesteś w domu u Kai,\nteraz możesz przmieszczać się po poszczególnych pokojach.\nMożesz też poczekać na Kaję żeby spędzić razem czas.")
time.sleep(1)
funkcje.menu()
