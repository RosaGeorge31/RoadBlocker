import random
def get_elevation_matrix(n_rows, n_cols):
    from bingmaps.apiservices import ElevationsApi
    key = 'Aok77W6veJ7IHNM_lCMZqmfV-r82f07hTxaRWaYR1byZgbSrzZcdzxDUynbNEMVC'
    data = {'method': 'Bounds','bounds': [17.0778, 78.0524, 17.7735, 78.8640],'rows': n_rows, 'cols': n_cols,'key': key}
    elevations = ElevationsApi(data)
    elev_val = list(elevations.elevations[0][0])
    itr=0
    elevation_matrix = [[0 for _ in range(n_cols)] for _ in range(n_rows)]
    for i in range(n_rows):
        for j in range(n_cols):
            elevation_matrix[i][j] = elev_val[itr]
            itr+=1
    '''for i in elevation_matrix:
        print(i)
    print('\n\n')'''
    for i in range(n_rows//2):
        temp =elevation_matrix[i]
        elevation_matrix[i] = elevation_matrix[n_rows-i-1]
        elevation_matrix[n_rows-i-1] = temp
    return elevation_matrix
    '''print("\n")
    for i in elevation_matrix:
        print(i)'''

def flood_checker(road_matrix, elevation_matrix, n_rows, n_cols):
    if n_cols == 0:
        return 0
    max_height = elevation_matrix[0][0]
    for i in range(n_rows):
        for j in range(n_cols):
            max_height = max(max_height, elevation_matrix[i][j])
    proportionality_matrix = [[0 for _ in range(n_cols)] for _ in range(n_rows)]
    c = 1
    total_proportion = 0
    for i in range(n_rows):
        for j in range(n_cols):
            proportionality_matrix[i][j] = c * (1 / (1 + (elevation_matrix[i][j] / max_height)))
            total_proportion += proportionality_matrix[i][j]
    rainfall = 20
    volume = n_rows * n_cols * rainfall
    time = 4
    threshold = 80
    flooded_matrix = [[0 for _ in range(n_cols)] for _ in range(n_rows)]
    for i in range(n_rows):
        for j in range(n_cols):
            factor = (proportionality_matrix[i][j] / total_proportion) * volume * time
        	
            if i==0 and j==0:
            	print(str(factor) + '  ' + str(elevation_matrix[i][j]))
            if(factor >= threshold):
                flooded_matrix[i][j] = 1
    # for i in flooded_matrix:
    #     print(i)
    print("\n")
    blocked_matrix = [[0 for _ in range(n_cols)] for _ in range(n_rows)]
    for i in range(n_rows):
        for j in range(n_cols):
            if(flooded_matrix[i][j] == 1 and road_matrix[i][j]==1):
                blocked_matrix[i][j] = 1
    for i in blocked_matrix:
        print(i)
    print("\n")
    return blocked_matrix

n_rows = 10
n_cols = 10
# elevation_matrix = [[random.randint(1,11) for i in range(n_cols)] for j in range(n_rows)]

elevation_matrix = get_elevation_matrix(n_rows, n_cols)
# for i in elevation_matrix:
    # print(i)
print("\n")
f = open ( 'Road.txt' , 'r')
road_matrix = [[num for num in (line.split(' '))] for line in f]
for i in range(len(road_matrix)):
    for j in range(len(road_matrix)):
        road_matrix[i][j] = int(road_matrix[i][j])
    road_matrix[i].pop()
# for i in road_matrix:
    # print(i)
print("\n")
blocked_matrix = flood_checker(road_matrix, elevation_matrix, n_rows, n_cols)

