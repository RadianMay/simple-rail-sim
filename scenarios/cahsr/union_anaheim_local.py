scenario_name = "Union - Anaheim, 144km/h"

# Each tuple: (start kilometer, end kilometer, speed limit (km/h), ends at stop, name)

# Mileposts are from https://chicagorailfan.com/mmupnw.html
# Speed limits are from OpenRailwayMap

route = [
                                # UNION stop
    (0.0, 1.0, 80, False),
    (1.0, 3.7, 144, False),
    (3.7, 5.0, 90, False),
    (5.0, 12.4, 144, True),
                                # COMMERCE stop
    (12.4, 25.1, 144, True),
                                # NORWALK stop
    (25.1, 33.1, 144, True),
                                # BUENA PARK stop
    (33.1, 39.3, 144, True),
                                # FULLERTON stop
    (39.3, 39.7, 144, False),
    (39.7, 40.9, 120, False),
    (40.9, 48.7, 144, True),
                                # ANAHEIM stop
]

stops = {
    0.0:  'Union',
    12.4:  'Commerce',
    25.1:  'Norwalk',
    33.1:  'Buena Park',
    39.3: 'Fullerton',
    48.7: 'Anaheim',
}

dwell_time = 30 # seconds
pad_factor = 1.07 # 7% padding for acceleration/cruise/deceleration