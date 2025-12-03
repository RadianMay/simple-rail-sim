scenario_name = "UP-N + KRM, high-level boarding, 160kph"

# Each tuple: (start milepost, end milepost, speed limit (km/h), ends at stop, name)

# Mileposts are from https://chicagorailfan.com/mmupn.html and https://chicagorailfan.com/rfttucn.html
# Stations north of Kenosha are from satellite imagery
# Speed limits are from OpenRailwayMap

route = [
                                # UNION stop
    (0.0, 1.0, 80, False),
    (1.0, 1.2, 50, False),
    (1.2, 2.2, 80, True),
                                # CHIGAGO stop
    (2.2, 4.5, 100, True),
                                # NORTH stop
    (4.5, 19.8, 160, True),
                                # EVANSTON stop
    (19.8, 27.2, 160, True),
                                # WINNETKA stop
    (27.2, 31.4, 160, True),
                                # GLENCOE stop
    (31.4, 37.5, 160, True),
                                # HIGHLAND PARK stop
    (37.5, 46.1, 160, True),
                                # LAKE FOREST stop
    (46.1, 55.9, 160, False),
    (55.9, 56.4, 100, False),
    (56.4, 58.3, 160, True),
                                # WAUKEGAN stop
    (58.3, 68.3, 160, True),
                                # ZION stop
    (68.3, 72.1, 160, True),
                                # WINTHROP HARBOR stop
    (72.1, 81.9, 160, False),
    (81.9, 82.5, 150, False),
    (82.5, 83.6, 160, True),
                                # KENOSHA stop
    (83.6, 86.2, 160, True),
    (86.2, 87.7, 144, False),
    (87.7, 89.6, 160, True),
                                # SOMERS stop
    (89.6, 96.3, 160, True),
                                # DURAND stop
    (96.3, 99.9, 160, True),
                                # RACINE stop
    (99.9, 106.7, 160, True),
                                # CALEDONIA stop
    (106.7, 116.4, 160, True),
                                # OAK CREEK stop
    (116.4, 120.8, 160, True),
                                # SOUTH MILWAUKEE stop
    (120.8, 131.7, 160, False),
    (131.7, 134.1, 80, False),
    (134.1, 134.6, 50, True),
                                # NATIONAL stop
    (134.6, 136.0, 50, True),
                                # MILWAUKEE INTERMODAL stop

]

stops = {
    0.0:   'Chicago - Union',
    2.2:   'Chicago',
    4.5:   'North',
    19.8:  'Evanston',
    27.2:  'Winnetka',
    31.4:  'Glencoe',
    37.5:  'Highland Park',
    46.1:  'Lake Forest',
    58.3:  'Waukegan',
    68.3:  'Zion',
    72.1:  'Winthrop Harbor',
    83.6:  'Kenosha',
    89.6:  'Somers',
    96.3:  'Durand',
    99.9:  'Racine',
    106.7: 'Caledonia',
    116.4: 'Oak Creek',
    120.8: 'South Milwaukee',
    134.6: 'National',
    136.0: 'Milwaukee Intermodal'
}

dwell_time = 30 # seconds
pad_factor = 1.07 # 7% padding for acceleration/cruise/deceleration