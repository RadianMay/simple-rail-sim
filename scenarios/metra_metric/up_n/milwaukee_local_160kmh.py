scenario_name = "UP-N, Milwaukee Extension Local, 160kph"

# Each tuple: (start kilometer, end kilometer, speed limit (km/h), ends at stop, name)

# Mileposts are from https://chicagorailfan.com/mmupn.html and https://chicagorailfan.com/rfttucn.html
# Stations north of Kenosha are from satellite imagery
# Speed limits are from OpenRailwayMap

route = [
    (0.0, 120.8, 160, True),     # from Chicago Union Station Resolve
                                # SOUTH MILWAUKEE stop
    (120.8, 123.3, 160, True),
                                # COLLEGE stop
    (123.3, 126.4, 100, True),
                                # CUDAHY stop
    (126.4, 130.4, 160, True),
                                # OKLAHOMA stop
    (130.4, 131.7, 160, True),
                                # LINCOLN AVE stop
    (131.7, 134.1, 80, False),
    (134.1, 134.6, 50, True),
                                # NATIONAL stop
    (134.6, 136.0, 50, True),
                                # MILWAUKEE INTERMODAL stop

]

stops = {
    0.0: 'Chicago Union Station',
    120.8: 'South Milwaukee',
    123.3: 'College',
    126.4: 'Cudahy',
    130.4: 'Oklahoma',
    131.7: 'Lincoln Ave',
    134.6: 'National',
    136.0: 'Milwaukee Intermodal'
}

dwell_time = 30 # seconds
pad_factor = 1.07 # 7% padding for acceleration/cruise/deceleration