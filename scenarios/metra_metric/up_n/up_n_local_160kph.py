scenario_name = "UP-N, high-level boarding, 160kph"

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
    (4.5, 11.0, 160, True),
                                # RAVENSWOOD stop
    (11.0, 13.5, 160, True),
                                # PETERSON/RIDGE stop
    (13.5, 15.6, 160, True),
                                # ROGERS PARK stop
    (15.6, 18.2, 160, True),
                                # MAIN STREET stop
    (18.2, 19.8, 160, True),
                                # EVANSTON stop
    (19.8, 21.9, 160, True),
                                # CENTRAL STREET stop
    (21.9, 23.7, 160, True),
                                # WILMETTE stop
    (23.7, 25.0, 160, True),
                                # KENILWORTH stop
    (25.0, 25.9, 160, True),
                                # INDIAN HILL stop
    (25.9, 27.2, 160, True),
                                # WINNETKA stop
    (27.2, 29.0, 160, True),
                                # HUBBARD WOODS stop
    (29.0, 31.4, 160, True),
                                # GLENCOE stop
    (31.4, 33.5, 160, True),
                                # BRAESIDE stop
    (33.5, 34.1, 160, True),
                                # RAVINIA PARK stop
    (34.1, 35.1, 160, True),
                                # RAVINIA stop
    (35.1, 37.5, 160, True),
                                # HIGHLAND PARK stop
    (37.5, 40.0, 160, True),
                                # HIGHWOOD stop
    (40.0, 41.9, 160, True),
                                # FT. SHERIDAN stop
    (41.9, 46.1, 160, True),
                                # LAKE FOREST stop
    (46.1, 49.1, 160, True),
                                # LAKE BLUFF stop
    (49.1, 52.3, 160, True),
                                # GREAT LAKES stop
    (52.3, 54.8, 160, True),
                                # NORTH CHICAGO stop
    (54.8, 55.9, 160, False),
    (55.9, 56.4, 100, False),
    (56.4, 58.3, 160, True),
                                # WAUKEGAN stop

]

stops = {
    0.0:   'Chicago - Union',
    2.2:   'Chicago',
    4.5:   'North',
    11.0:  'Ravenswood',
    13.5:  'Peterson/Ridge',
    15.6:  'Rogers Park',
    18.2:  'Main Street',
    19.8:  'Evanston',
    21.9:  'Central Street',
    23.7:  'Wilmette',
    25.0:  'Kenilworth',
    25.9:  'Indian Hill',
    27.2:  'Winnetka',
    29.0:  'Hubbard Woods',
    31.4:  'Glencoe',
    33.5:  'Braeside',
    34.1:  'Ravinia Park',
    35.1:  'Ravinia',
    37.5:  'Highland Park',
    40.0:  'Highwood',
    41.9:  'Fort Sheridan',
    46.1:  'Lake Forest',
    49.1:  'Lake Bluff',
    52.3:  'Great Lakes',
    54.8:  'North Chicago',
    58.3:  'Waukegan',
}

dwell_time = 30 # seconds
pad_factor = 1.07 # 7% padding for acceleration/cruise/deceleration