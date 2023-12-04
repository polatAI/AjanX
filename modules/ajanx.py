import requests
import json
from contextlib import contextmanager
import time
from itertools import chain, combinations, permutations
import instaloader
from instaloader.exceptions import ConnectionException, InstaloaderException, LoginRequiredException

@contextmanager
def FileManager(path, methods, encod):
    try:
        file = open(path, methods, encoding=encod)
        yield file
    finally:
        file.close()

class Scanner:
    
    def __init__(self):
        self.instagram_usernames = list()
        self.loader = instaloader.Instaloader()
    
    def kullanici_bilgileri(self):
        
        with open("olasi_kullanici_adlari.txt", "r") as file:
            lines = file.readlines()
            self.instagram_usernames = [line.split("https://instagram.com/")[1].strip() for line in lines if "https://instagram.com/" in line]

        for kullanici_adi in self.instagram_usernames:
            try:
                profile = instaloader.Profile.from_username(self.loader.context, kullanici_adi)
                with FileManager("olasi_kullanici_bilgileri" , "a+", "utf-8") as file:
                    file.write("Kullanıcı Adı: " + str(profile.username) + '\n')
                    file.write("Takipçi Sayısı: " + str(profile.followers) + '\n')
                    file.write("Takip Edilen Sayısı: " + str(profile.followees) + '\n')
                    file.write("Gönderi Sayısı: " + str(profile.mediacount) + '\n')
                    file.write("Biografisi: " + str(profile.biography) + '\n')
                    file.write("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n")
                    file.write("                                 AJANX TOOLS                               \n")
                    file.write("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n")
            except instaloader.exceptions.ProfileHasNoPicsException:
                print(f"Kullanıcı adı bulunamadı: {kullanici_adi}")
                
                
    def gonderileri_indir(self):
        
        for kullanici_adi in self.instagram_usernames:
            try:
                profile = instaloader.Profile.from_username(self.loader.context, kullanici_adi)
            
                for post in profile.get_posts():
                    self.loader.download_post(post, target=profile.username)
            except instaloader.exceptions.ProfileHasNoPicsException:
                print(f"Kullanıcı adı bulunamadı: {kullanici_adi}")

class Instagram:

    def __init__(self, config, permutations_list):
        self.delay = config['plateform']['instagram']['rate_limit'] / 1000
        self.format = config['plateform']['instagram']['format']
        self.permutations_list = permutations_list
        self.kullanici_adi_listesi = list()

    def possible_usernames(self):
        possible_usernames = []
        for permutation in self.permutations_list:
            possible_usernames.append(self.format.format(permutation=permutation))
        return possible_usernames

    def search(self):
        instagram_usernames = {"accounts": []}
        bibliogram_URL = "https://bibliogram.art/u/{}"
        possible_usernames_list = self.possible_usernames()

        for username in possible_usernames_list:
            try:
                bibliogram_formatted_URL = bibliogram_URL.format(username.replace("https://instagram.com/", ""))
                r = requests.get(bibliogram_formatted_URL)
            except requests.ConnectionError:
                print("Failed to connect to Instagram")

            if r.status_code == 200:
                instagram_usernames["accounts"].append({"value": username})
                print(f"Found username: {username}")

            time.sleep(self.delay)

        with FileManager("olasi_kullanici_adlari.txt", "w", "utf-8") as file:
            for kullanici_adi in instagram_usernames["accounts"]:
                file.write(kullanici_adi["value"] + '\n')
        with FileManager("olasi_kullanici_adlari.txt", "a+", "utf-8") as file:
            icerik = file.read()
            icerik.strip("https://instagram.com/")
        
        print("Finished searching")

class Core:

    def __init__(self, config_path, items):
        with open(config_path, 'r') as f:
            self.CONFIG = json.load(f)
        self.items = items
        self.permutations_list = []

    def config(self):
        return self.CONFIG

    def get_permutations(self):
        combinations_list = list(chain(*map(lambda x: combinations(self.items, x), range(1, len(self.items) + 1))))
        for combination in combinations_list:
            for perm in list(permutations(combination)):
                self.permutations_list.append("".join(perm))

    def instagram(self):
        try:
            Instagram(self.CONFIG, self.permutations_list).search()
        except ConnectionException as e:
            print(f"Hata: {e}")
            print("Çok fazla istek gönderdiğiniz için geçici olarak engellendiniz. Lütfen bir süre sonra tekrar deneyin.")
        except LoginRequiredException as e:
            print(f"Hata: {e}")
            print("Instagram hesabınıza giriş yapmanız gerekiyor.")
            self.login_instaloader()


def main():
    ad_soyad_username = input("Lütfen ad, soyad ve kullanıcı adınızı boşluk bırakarak girin: ")
    items = ad_soyad_username.split()
    config_path = "config.json"  # Replace with your config file path
    core = Core(config_path, items)
    core.get_permutations()
    core.instagram()

    getir = Scanner()
    try:
        getir.kullanici_bilgileri()
        getir.gonderileri_indir()
    except instaloader.exceptions.LoginRequiredException:
        print("Fazla istek gönderdiğiniz için yetkisizleştirildiniz lütfen giriş yapın.")
        try:
            L = instaloader.Instaloader()
            username = input("Lütfen kullanıcı adınızı giriniz: ")
            password = input("Lütfen şifrenizi giriniz: ")
            L.context.login(username, password)
        except InstaloaderException as ex:
            print(f"Giriş başarısız. Hata: {ex}")
            exit()
            
    getir.kullanici_bilgileri()
    getir.gonderileri_indir()
