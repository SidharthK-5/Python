"""
This is situation in an infinite hotel
A tourist group consists of a captain and an unknown number of families consisting of K members per group (K != 1 and 1 < K < 1000)
Captain will given a separate room. For other groups, they'll get one room per group
Except for captain's room, the room numbers will repeat K times per group

From K and room numbers list, find captain's room no.
"""

K = int(input())

room_nos_list = map(int, input().split())
room_nos_list = sorted(room_nos_list)

for room_index in range(len(room_nos_list)):
    if room_index != len(room_nos_list) - 1:
        # For each room number, check if the adjacent room numbers do not match with it
        if (
            room_nos_list[room_index] != room_nos_list[room_index - 1]
            and room_nos_list[room_index] != room_nos_list[room_index + 1]
        ):
            # If adjacent room numbers aren't matching, it will be captain's room
            print(room_nos_list[room_index])
            break
    else:
        # When room_index is the last room in the list
        print(room_nos_list[room_index])
