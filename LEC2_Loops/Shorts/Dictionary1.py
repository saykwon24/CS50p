"""
Dictionary Methods (1)
    .update(dict): dictionary에 dict의 key-value pair를 추가하는 method
    .get(A, B):    A라는 key를 찾고, 없으면 B를 반환하는 method


Dictionary에 key-value pair를 추가하는 방법
1) 1개씩 추가: dict에 key indexing을 사용하여 value를 assign (dict['key'] = value)
2) 여러 개를 한 번에 추가: .update() method 이용
"""


def main():
    spacecraft = {"name": "James Webb Space Telescope"}
    spacecraft.update({"distance": 0.01, "orbit": "Sun"})
    print(create_report(spacecraft))


def create_report(spacecraft):
    # """"""를 이용하여 여러 줄의 값을 return
    
    return f"""
    ========= REPORT =========
    
    Name: {spacecraft.get("name", "Unknown")}
    Distance: {spacecraft.get("distance", "Unknown")} AU
    Orbit: {spacecraft.get("orbit", "Unknown")}
    
    ==========================
    """


main()