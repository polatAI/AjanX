from modules import ajanx


class Bcolors:
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    RED = '\033[31m'
    YELLOW = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    BGRED = '\033[41m'
    WHITE = '\033[37m'



def logo():
    print(Bcolors.RED + Bcolors.BOLD)
    logo = """

                     _
                  __~a~_
                  ~~;  ~_
    _                ~  ~_                _
   '_\;__._._._._._._]   ~_._._._._._.__;/_`
   '(/'/'/'/'|'|'|'| (    )|'|'|'|'\'\'\'\)'
   (/ / / /, | | | |(/    \) | | | ,\ \ \ \)
  (/ / / / / | | | ^(/    \) ^ | | \ \ \ \ \)
 (/ / / / /  ^ ^ ^   (/  \)    ^ ^  \ \ \ \ \)
(/ / / / ^          / (||)|          ^ \ \ \ \)
^ / / ^            M  /||\M             ^ \ \ ^
 ^ ^                  /||\                 ^ ^
                     //||\\
                     //||\\
                     //||\\
                     '/||\'
    # v1.0.0 #
       >> AjanX <<
       >> 5/12/2023 <<

    """
    print(logo)
    print(Bcolors.ENDC)

logo()

while True:
    print(Bcolors.GREEN +"""
          
          Not: Fazla istek gönderildiği zaman programda hatalar çıkabiliyor. Eğer fazla istek gönderirseniz
          sizden instagram hesabına giriş yapmanız istenecektir.
          
          """ + Bcolors.BOLD)
    
    ajanx.main()
