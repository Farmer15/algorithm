def solution(emergency):
    ranked_dict = { v : i for i, v in enumerate(sorted(emergency))}

    return list(map(lambda x: len(emergency) - ranked_dict[x], emergency)) 