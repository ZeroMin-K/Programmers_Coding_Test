"""
장군개미 : 공격력 5
병정개미 : 공격력 3
일개미 : 공격력 1
사냥감의 체력에 맞게 최소한 병력 구성하려면 몇마리 개미가 필요한지 return 
"""

def solution(hp):
    
    answer = 0
    # 개미들 공격력 리스트 ants 생성
    ants = [5, 3, 1]
    
    # 개미들 공격력 리스트 ants 하나씩 반복하며 => ant
    for ant in ants:
        # 현재 개미의 공격력에서 현재 사냥감의 hp로 나눈 몫, 나머지 구하기
        div, rest = divmod(hp, ant)
        # 몫은 answer에 넣어서 증가 (개미 수)
        answer += div 
        # 현재 hp는 나머지 
        hp = rest 
        
    return answer