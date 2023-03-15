import requests
import json

from bs4 import BeautifulSoup

# Swordman
url_swordman = "https://nostale.fandom.com/wiki/Swordsman"
url_warrior = "https://nostale.fandom.com/wiki/Warrior"
url_blade = "https://nostale.fandom.com/wiki/Blade"
url_crusader = "https://nostale.fandom.com/wiki/Crusader"
url_berserker = "https://nostale.fandom.com/wiki/Berserker"

# Archer
url_archer = "https://nostale.fandom.com/wiki/Archer"
url_ranger = "https://nostale.fandom.com/wiki/Ranger"
url_assassin = "https://nostale.fandom.com/wiki/Ranger"
url_destroyer = "https://nostale.fandom.com/wiki/Destroyer"
url_wildkeeper = "https://nostale.fandom.com/wiki/Wildkeeper"

# Mage
url_mage = "https://nostale.fandom.com/wiki/Mage"
url_redmage = "https://nostale.fandom.com/wiki/Red_Magician"
url_holymage = "https://nostale.fandom.com/wiki/Holy_Magician"
url_bluemage = "https://nostale.fandom.com/wiki/Blue_Magician"
url_darkgunner = "https://nostale.fandom.com/wiki/Dark_Gunner"


#  ------------------------------------------------------------------------------


def save_json(json_file, save_path):
    json_file = json.dumps(json_file)
    save_file = open(save_path, 'w')
    json.dump(json_file, save_file, indent = 6)
    save_file.close()

def fetch_json_version_1(url, sp_class, sp_name):
    """ 
    Fetch character/SPs skills for Swordman and Archer
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    skills = []

    # find all skills inside table
    for table in soup.find_all('table'):
        tds = table.find_all('td')
        skill_name = tds[1].find('b').text
        skill = {'skill': skill_name}
        for td in tds[2:]:
            text = td.text
            keys = [td.text for td in td.find_all('b')]
            tmp = text

            # removing 
            for key in keys:
                tmp = tmp.replace(key, '')
            tmp = tmp.replace('seconds', '')
            tmp = tmp.replace('Gold', '')
            values = tmp.split()

            # adding to skill
            for key, value in zip(keys, values):
                key = key.replace(':', '')
                skill[key] = value

        skills.append(skill)

    # crate as json
    json = {'class': sp_class, 'sp_name': sp_name,'skills': skills}
    return json

def fetch_json_version_2(url, sp_class, sp_name):
    """ 

    """
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # get all character skills
    skills = []
    for table in soup.find_all('table'):
        tds = table.find_all('td')
        skill_name = (tds[1].text).strip()
        skill = {'skill': skill_name}
        for skillbox in tds[2:]:
            tmp = (skillbox.text).split(':')
            tmp = [w.strip() for w in tmp]
            if len(tmp) != 2:
                break
            key, value = tmp
            skill[key] = value

        skills.append(skill)

    # create json
    json = {'class': sp_class, 'sp_name': sp_name,'skills': skills}
    return json



#  ------------------------------------------------------------------------------



def test_fetch_json1():
    data = [(url_swordman, 'Swordman', 'Normal'), (url_archer, 'Archer', 'Normal')]

    for (url, sp_class, sp_name) in data:
        json = fetch_json_version_1(url, sp_class, sp_name)
        print(json)

        # save as json
        save_path = f"configs/{sp_class}/{sp_name}.json"
        save_json(json, save_path)

def test_fetch_json2():
    data = [(url_mage, 'Mage', 'Normal'), (url_warrior, 'Swordman', 'Warrior'),
            (url_blade, 'Swordman', 'Blade'), (url_crusader, 'Swordman', 'Crusader'),
            (url_berserker, 'Swordman', 'Berserker'), (url_ranger, 'Archer', 'Ranger'),
            (url_assassin, 'Archer', 'Assassin'), (url_destroyer, 'Archer', 'Destroyer'),
            (url_wildkeeper, 'Archer', 'Wildkeeper'), (url_redmage, 'Mage', 'Red_Magician'), 
            (url_holymage, 'Mage', 'Holy_Magician'), (url_bluemage, 'Mage', 'Blue_Magician'),
            (url_darkgunner, 'Mage', 'Dark_Gunner')]


    for (url, sp_class, sp_name) in data:
        json = fetch_json_version_2(url, sp_class, sp_name)
        print(json)

        # save as json
        save_path = f"configs/{sp_class}/{sp_name}.json"
        save_json(json, save_path)

#  ------------------------------------------------------------------------------

def main():
    test_fetch_json1()
    test_fetch_json2()


if __name__ == "__main__":
    main()
