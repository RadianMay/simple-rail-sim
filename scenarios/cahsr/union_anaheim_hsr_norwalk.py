scenario_name = "Union - Anaheim, 144km/h"

# Each tuple: (start kilometer, end kilometer, speed limit (km/h), ends at stop, name)

# Mileposts are from https://chicagorailfan.com/mmupnw.html
# Speed limits are from OpenRailwayMap

route = [
                                # UNION stop
    (0.0, 1.0, 80, False),
    (1.0, 3.7, 144, False),
    (3.7, 5.0, 90, False),
    (5.0, 25.1, 144, True),
                                # NORWALK stop
    (25.1, 39.7, 144, False),
    (39.7, 40.9, 120, False),
    (40.9, 48.7, 144, True),
                                # ANAHEIM stop
]

stops = {
    0.0:  'Union',
    25.1:  'Norwalk',
    48.7: 'Anaheim',
}

dwell_time = 90 # seconds
pad_factor = 1.07 # 7% padding for acceleration/cruise/deceleration