import math

''' take json database and separate it into host and gusts groups'''


def host_gust_ids(full_data):
    hosts_ids = []
    gust_ids = []
    for dict in full_data:
        if dict['host'] == 'Host':
            hosts_ids.append(dict['id'])
        elif dict['host'] == 'Gust':
            gust_ids.append(dict['id'])
    return hosts_ids, gust_ids


'''return a list of dicts consist of a single host and a list of its gusts'''


def to_groups(hosts, ids):
    hosts_list = hosts
    gusts_list = ids
    groups =[]
    number_of_gusts = len(ids)/len(hosts)
    remaining_gusts = len(ids)%len(hosts)
    groups_number = ((remaining_gusts, math.ceil(number_of_gusts)), (len(hosts)-remaining_gusts,math.floor(number_of_gusts)))
    for pair in groups_number:
        number_groups = pair[0]
        number_gusts = pair[1]
        for i in range(0, number_groups):
            g_gusts = gusts_list[0:number_gusts]
            groups.append({'Host': hosts_list[0], 'Gusts': g_gusts})
            hosts_list.pop(0)
            for i in range(0, number_gusts):
                gusts_list.pop(0)
    return groups


# this function is for checking and printing parts of the data.
# not relevant for the full script and may be deleted.
def print_info(json_full_data, n_hosts, n_gusts, basic_groups):
    print('hosts:{}, gusts total: {}'.format(n_hosts, n_gusts))
    print('basic groups: ', len(basic_groups), '\n', basic_groups)
    print('json_full_data:\n', json_full_data)
    print('basic group : \n', basic_groups[0])
    print('host data: ')
    for dict in json_full_data:
        if dict['id'] == basic_groups[0]['Host']:
            print(dict)
    print('gusts data')
    for dict in json_full_data:
        for id in basic_groups[0]['Gusts']:
            if dict['id'] == id:
                print(dict)
