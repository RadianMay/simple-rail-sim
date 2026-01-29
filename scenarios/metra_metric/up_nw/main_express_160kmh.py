scenario_name = "UP-N - through running local, 160kph"

# Each tuple: (start kilometer, end kilometer, speed limit (km/h), ends at stop, name)

# Mileposts are from https://chicagorailfan.com/mmupnw.html
# Speed limits are from OpenRailwayMap

route = [
                                # UNION stop
    (0.0, 1.0, 80, False),
    (1.0, 1.2, 50, False),
    (1.2, 2.2, 80, True),
                                # CHIGAGO stop
    (2.2, 4.5, 100, True),
                                # NORTH stop
    (4.5, 5.4, 160, False),
    (5.4, 6.0, 130, False),
    (6.0, 9.3, 160, True),
                                # BELMONT/KEDZIE stop
    (9.3, 13.2, 160, True),
                                # MAYFAIR stop
    (13.2, 27.9, 160, True),
                                # DES PLAINES stop
    (27.9, 37.2, 160, True),
                                # ARLINGTON HEIGHTS stop
    (37.2, 40.0, 160, True),
                                # ARLINGTON PARK stop
    (40.0, 51.7, 160, True),
                                # BARRINGTON stop
    (51.7, 60.6, 160, True),
                                # FOX RIVER GROVE stop
    (60.6, 62.6, 160, True),
                                # CARY stop
    (62.6, 68.3, 160, True),
                                # PINGREE ROAD stop
    (68.3, 70.1, 160, True),
                                # CRYSTAL LAKE stop
    (70.1, 74.6, 160, True),
                                # RIDGEFIELD stop
    (74.6, 83.6, 160, True),
                                # WOODSTOCK stop
    (83.6, 90.7, 160, True),
                                # HARTLAND stop
    (90.7, 102.1, 160, True),
                                # HARVARD stop
]

stops = {
    0.0:  'Union',
    2.2:  'Chicago',
    4.5:  'North',
    9.3:  'Belmont/Kedzie',
    13.2: 'Mayfair',
    27.9: 'Des Plaines',
    37.2: 'Arlington Heights',
    40.0: 'Arlington Park', 
    51.7: 'Barrington',
    60.6: 'Fox River Grove',
    62.6: 'Cary',
    68.3: 'Pingree Road',
    70.1: 'Crystal Lake',
    74.6: 'Ridgefield',
    83.6: 'Woodstock',
    90.7: 'Hartland',
    102.1: 'Harvard',
}

dwell_time = 30 # seconds
pad_factor = 1.07 # 7% padding for acceleration/cruise/deceleration