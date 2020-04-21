import pandas as pd
import random
import json


def get_streets_of_city(data_file, city_symbol, header_row):
    streets_names = pd.read_csv(data_file, header=header_row)
    ta_streets = streets_names[['סמל_ישוב', 'שם_ישוב', 'שם_רחוב']]
    ta_streets = ta_streets.loc[ta_streets['סמל_ישוב'] == city_symbol]
    ta_streets.dropna
    return ta_streets['שם_רחוב']


def user_id_gen():
    id = ''
    for i in range(0, 9):
        id += str(random.randint(0, 9))
    return id


def ishost():
    rnd_int = random.randint(1, 10)
    if rnd_int <= 3:
        return 'Host'
    else:
        return 'Gust'


def gen_random_address(street_names_database, top_hous_number, num_of_test_streets ):
    street_lower_range = street_names_database.index[0]
    street_h_range = street_names_database.index[-1]
    streets_all = []

    for i in range(0, num_of_test_streets):
        street_index = random.randint(street_lower_range,street_h_range)
        street_name = street_names_database[street_index]
        street_num = random.randint(1, top_hous_number)
        user_id = user_id_gen()
        is_host = ishost()
        city = 'תל אביב - יפו'
        address = {'index': '{}: '.format(i+1),
                   'street': street_name,
                   'street_num': street_num,
                   'city': city,
                   'id': user_id,
                   'host': is_host
                   }
        streets_all.append(address)
    return streets_all


def create_streets_db():
    tel_aviv_city_streets_names = get_streets_of_city('rechovot_israel', 5000, 1)
    streets_list = gen_random_address(tel_aviv_city_streets_names, 41, 70)
    json_street = json.dumps(streets_list)
    return json_street
