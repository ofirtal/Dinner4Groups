''' grades the group by an avg score of gusts distance score to host'''


def grade_group_avg(group_dict):
    count = 0
    group_score = 0

    for i in group_dict['Gusts']:
        count += 1
        group_score += int(i['api answer'])
    total_score = round(group_score/count, 2)
    group_dict.__setitem__('Group_score', total_score)
    return group_dict

