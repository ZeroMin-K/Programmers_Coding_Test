def solution(rsp):
    # 가위 2, 바위 0, 보 5
    # 가위 2 => 바위0, 바위 0 => 보5, 보 5 => 가위 2
    win_dict = {'2':'0', '0': '5', '5':'2'}
    return ''.join([win_dict[turn] for turn in rsp])