"""
Tuple: list와 유사한 data structure, braces(())로 표현
       tuple의 값을 수정하거나 새로 추가하는 것은 불가능하므로, 값을 수정하거나 추가하지 않을 것이 확실하고, 메모리를 효율적으로 사용하고자 할 때 유용
       tuple(), () 등으로 initialize
       tuple에 있는 값들은 얼마든지 unpacked(다른 변수에 값을 복사) 가능
  >>> tuple documentation: https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences

       
sys.getsizeof(s): sys 내에 있는 함수로, s의 크기를 바이트 단위로 알려주는 함수
"""


import sys


def main():
    coordinates = (42.376, -71.115)    # tuple
    latitude, longitude = coordinates
    
    print(f"Latitude: {latitude}")
    print(f"Longitude: {longitude}")
    
    
    coordinate_tuple = (42.376, -71.115)
    coordinate_list = [42.376, -71.115]
    
    print(f"{sys.getsizeof(coordinate_tuple)} bytes")
    print(f"{sys.getsizeof(coordinate_list)} bytes")


main()