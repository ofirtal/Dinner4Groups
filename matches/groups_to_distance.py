from to_api import api_response
'''gets group host_address and gusts_address from the full data '''


def group_address(group_dict, full_data):
    gusts_address = []
    host_address = []
    for person_dict in full_data:
        if person_dict['id'] == group_dict['Host']:
            host_address.append({'id': person_dict['id'],'address':('{} {} {}').format(person_dict['street'], person_dict['street_num'],person_dict['city'])})
        for id in group_dict['Gusts']:
            if person_dict['id'] == id:
                gusts_address.append({'id':person_dict['id'],'address': ('{} {} {}').format(person_dict['street'], person_dict['street_num'], person_dict['city'])})
    return host_address, gusts_address


def score_host_n_gust_distance(group_dict):
    host_destination = group_dict['Host'][0]['address']
    for gust_dict in group_dict['Gusts']:
        score = api_response(host_destination, gust_dict['address'])
        gust_dict.__setitem__('api answer', score)

    return group_dict
