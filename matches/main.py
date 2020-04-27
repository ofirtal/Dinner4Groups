from json_from_url import read_data_form_url
from json_to_groups import host_gust_ids, to_groups, print_info
from groups_to_distance import group_address, score_host_n_gust_distance


def main():
    target_url = 'https://streets-gen.herokuapp.com'
    json_full_data = read_data_form_url(target_url)
    hosts, gusts = host_gust_ids(json_full_data)
    number_hosts = len(hosts)
    number_gusts = len(gusts)
    '''basic groups return a list of dicts with host id and a list of gust ids - {host,[gusts id,id,id]}'''
    basic_groups = to_groups(hosts, gusts)
    # print_info(json_full_data, number_hosts, number_gusts, basic_groups)
    all_groups_address = []
    all_groups_scored = []
    for group in basic_groups:
        host_address, gusts_address = group_address(group, json_full_data)
        all_groups_address.append({'Host': host_address, 'Gusts': gusts_address})
    for gro in all_groups_address:
        score = score_host_n_gust_distance(gro)
        all_groups_scored.append(score)

    # a print for check up- will be deleted
    for g in all_groups_scored:
        print(g)


if __name__ == '__main__':
    main()
