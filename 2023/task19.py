import re


def task1(content):
    dic = {}
    ratings = []
    isRatings = False
    counter = 0

    for line in content:
        line = line.strip('\n')

        if len(line) == 0:
            isRatings = True
            continue
        
        if not isRatings:
            matches = re.match(r"^(\w+)\{(.*)\}", line)
            name = matches.group(1)
            rules = matches.group(2).split(',')
            dic[name] = rules
        else:
            matches = re.match(r'^\{x=(\d+),m=(\d+),a=(\d+),s=(\d+)\}$', line)
            ratings.append({
                'x':int(matches.group(1)),
                'm': int(matches.group(2)), 
                'a': int(matches.group(3)),
                  's':int(matches.group(4)) 
                  })

    for rating in ratings:
        following_workflow = 'in'
        while not following_workflow in ['A', 'R']:
            workflow = dic[following_workflow]
            following_workflow = check_workflow(rating, workflow)

        if following_workflow == 'A':
            counter += rating['x'] + rating['m']+ rating['a'] +rating['s'] 

    print(counter)

def check_workflow(rating_elements, workflow: list[str]):

    for step in workflow:
        if len(step) > 1 and step[1] in ['<', '>']:
            matches = re.match(r'^(.)(.)([0-9]+):(\w+)', step)
            letter = matches.group(1)
            sign = matches.group(2)
            value = int(matches.group(3))
            destination = matches.group(4)

            rating_value = rating_elements[letter]

            if sign == '<' and rating_value < value:
                return destination
            
            if sign == '>' and rating_value > value:
                return destination
            
            continue
            

        return step

                

