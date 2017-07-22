# -------------------------
# | 0| 1| 2| 3| 4| 5| 6| 7|
# -------------------------
# | 8| 9|10|11|12|13|14|15|
# -------------------------
# |16|17|18|19|20|21|22|23|
# -------------------------
# |24|25|26|27|28|29|30|31|
# -------------------------
# |32|33|34|35|36|37|38|39|
# -------------------------
# |40|41|42|43|44|45|46|47|
# -------------------------
# |48|49|50|51|52|53|54|55|
# -------------------------
# |56|57|58|59|60|61|62|63|
# -------------------------

BOARD_SIZE = 8

def get_coordinate(num):
    coordinate = {}

    x = (num % BOARD_SIZE) + 1
    y = (num / BOARD_SIZE) + 1

    coordinate['x'] = int(x)
    coordinate['y'] = int(y)

    return coordinate

def move(src_coord, dest_coord):
    dist = {}
    start_x = src_coord['x']
    start_y = src_coord['y']
    end_x = dest_coord['x']
    end_y = dest_coord['y']

    start = (start_x,start_y)
    end = (end_x, end_y)

    possible_moves = [(1, 2), (-1, -2), (1, -2), (-1, 2), (2, 1), (-2, -1), (2, -1), (-2, 1)]

    queue = [start]
    dist[start] = 0

    while len(queue):
        # pop from the queue
        current = queue[0]
        queue.pop(0)

        if current == end:
            return dist[current]

        for move in possible_moves:
            next_pos = move[0] + current[0],move[1] + current[1]

            if isValidPostion(next_pos[0], next_pos[1]):
                if next_pos not in dist:
                    dist[next_pos] = dist[current] + 1
                    queue.append(next_pos)
                    print queue

def isValidPostion(x, y):
    if x <= 0 or x > BOARD_SIZE:
        return False
    if y <= 0 or y > BOARD_SIZE:
        return False
    return True

def answer(src, dest):
    # your code here
    src_coord = get_coordinate(src)
    dest_coord = get_coordinate(dest)

    print move(src_coord, dest_coord)

answer(1,3)
answer(62,3)
answer(8,27)