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
          sizden instagram hesabına giriş yapmanız istenecektir.\n
          """ + Bcolors.BOLD)
    
    
    print("""
          İşlemler
          
          1 - Instagram Hesap Verilerini Çekme
          
          2 - Hastag Verilerini Çekme 
          
          3 - Gönderi Verilerini Çekme(Beğenenler, Yorumlar vs)

          4 - Ip Konum Tespiti
          
          5 - Tüm Sosyal Ağlarda Kullanıcı Adı Arama
          """)
    
    islem = input("Lütfen bir işlem seçiniz: ")
    
    if(islem == "1"):
        ajanx.userosint()
        
    elif(islem == "2"):
        hastag = input(Bcolors.YELLOW + "Lütfen Veri Çekmek İstediğiniz Hastag'i Giriniz: " + Bcolors.ENDC)
        ajanx.hastagosint(hastag)
        
    elif(islem == "3"):
        post_url = input(Bcolors.YELLOW + "Lütfen Veriler Çekilecek Post URL ini Giriniz(URL FORMAT: 'https://www.instagram.com/p/Cz4LjV4MsFn/?igshid=MzRlODBiNWFlZA=='): " + Bcolors.ENDC)
        ajanx.detayli_post_osint(post_url)

    elif(islem == "4"):
        print(Bcolors.RED + "Bu özellik güncellemeden sonra gelecek!!!" + Bcolors.ENDC)
    
    elif(islem == "5"):
        print(Bcolors.RED + "Bu özellik güncellemeden sonra gelecek!!!" + Bcolors.ENDC)
    
    else:
        print(Bcolors.RED + "Hatalı işlem girdiniz!!" + Bcolors.ENDC)
        
    
    