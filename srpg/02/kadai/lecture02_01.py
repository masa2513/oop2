import csv

def lecture02_01_printHeroStatus() -> None:
    # CSVファイルを読み込み、ID=1のHeroの情報を出力する
    with open('lecture02_Hero.csv', 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['ID'] == '1':
                print(f"{row['Name']}のステータスはHP:{row['HP']},MP:{row['MP']},Atk:{row['Atk']},Def:{row['Def']},Age:{row['Age']}")
                break

def lecture02_01_printWeaponStatus() -> None:
    # CSVファイルを読み込み、ID=1の武器の情報を出力する
    with open('lecture02_Weapon.csv', 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['ID'] == '1':
                print(f"{row['Weapon_Name']}のステータスはHP:{row['HP']},MP:{row['MP']},Atk:{row['Atk']},Def:{row['Def']},Age:{row['Age']}")
                break

def lecture02_01_printHeroStatusWithWeapon() -> None:
    # HeroのCSVファイルを読み込み、ID=1のHeroの情報を変数に代入
    hero_name = ""
    hero_hp = hero_mp = hero_atk = hero_def = hero_age = hero_weapon = 0
    
    with open('lecture02_Hero.csv', 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['ID'] == '1':
                hero_name = row['Name']
                hero_hp = int(row['HP'])
                hero_mp = int(row['MP'])
                hero_atk = int(row['Atk'])
                hero_def = int(row['Def'])
                hero_age = int(row['Age'])
                hero_weapon = int(row['Weapon'])
                break
    
    # WeaponのCSVファイルを読み込み、hero_weaponと一致するIDの武器情報を変数に代入
    weapon_name = ""
    weapon_hp = weapon_mp = weapon_atk = weapon_def = weapon_age = 0
    
    with open('lecture02_Weapon.csv', 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if int(row['ID']) == hero_weapon:
                weapon_name = row['Weapon_Name']
                weapon_hp = int(row['HP'])
                weapon_mp = int(row['MP'])
                weapon_atk = int(row['Atk'])
                weapon_def = int(row['Def'])
                weapon_age = int(row['Age'])
                break
    
    # ステータス情報を出力する
    print(f"{weapon_name}を装備した{hero_name}のステータスは" +
        f"HP:{hero_hp+weapon_hp}," +
        f"MP:{hero_mp+weapon_mp}," +
        f"Atk:{hero_atk+weapon_atk}," +
        f"Def:{hero_def+weapon_def}," +
        f"Age:{hero_age+weapon_age}")

if __name__ == '__main__':
    lecture02_01_printHeroStatus()
    lecture02_01_printWeaponStatus()
    lecture02_01_printHeroStatusWithWeapon()