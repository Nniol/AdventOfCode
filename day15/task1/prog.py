import sys
sys.path.append('..\..')
sys.path.append('..')

from file_lib import get_lines_from_file,strip_line
from structs import Point,PointType, Grid

lines = get_lines_from_file(day_number=15)

SENSORS:dict[str,Point] = {}
BEACONS:dict[str,Point] = {}
GRID: Grid = Grid()
for line in lines:
    line = strip_line(line)
    inputs = line.split(' ')
    sensor_x = int(inputs[2].split('=')[1].split(',')[0])
    sensor_y = int(inputs[3].split('=')[1].split(':')[0])
    beacon_x = int(inputs[8].split('=')[1].split(',')[0])
    beacon_y = int(inputs[9].split('=')[1])
    sensor = Point(sensor_x,sensor_y,PointType.SENSOR)
    beacon = Point(beacon_x,beacon_y,PointType.BEACON)
    sensor.set_beacon(beacon)
    GRID.check_min_max(sensor)
    GRID.check_min_max(beacon)
    SENSORS.update({sensor.get_dict_key():sensor})
    if beacon.get_dict_key() not in BEACONS:
        BEACONS.update({beacon.get_dict_key():beacon})

test_y = 2000000

COVERED:dict[str:Point] = {}
for key,sensor in SENSORS.items():
    print (sensor)
    # Does the sensor distance reach row test-y
    radial_distance = sensor.distance_to_beacon - abs(sensor.y - test_y)
    print (f"amount of cross over of row:{test_y} -> radial_distance {radial_distance}")
    if radial_distance >0 : # we are closer
        r = range(sensor.x - radial_distance,sensor.x + radial_distance+1)
        for test_x in r:
            p = Point(test_x,test_y,PointType.COVERED)
            point_key = p.get_dict_key()
            if point_key not in SENSORS and point_key not in BEACONS and point_key not in COVERED:
                COVERED.update({point_key:p})
    else:
        print ("DOES NOT REACH")
    

print (len(COVERED))
# GRID.calculate_dimensions()
# GRID.build_grid()
# for key,sensor in SENSORS.items():
#     GRID.add_point(sensor)
# for key,beacon in BEACONS.items():
#     GRID.add_point(beacon)
# sensor = SENSORS["8_7"]
# top_left_x = sensor.x - sensor.distance_to_beacon
# top_left_y = sensor.y - sensor.distance_to_beacon
# test_y = top_left_y
# while test_y <=sensor.y + sensor.distance_to_beacon:
#     test_x = top_left_x
#     while test_x <= sensor.x + sensor.distance_to_beacon:
#         test_p = Point(test_x,test_y,PointType.NOT_COVERED)
#         if Grid.point_on_grid(test_p): 
#             if Grid.point_is_not_covered(test_p):
#                 if sensor.is_closer_or_equal_to_beacon(test_p):
#                     test_p.set_covered()
#                 GRID.add_point(test_p)
#         test_x += 1
#     test_y += 1
    
# GRID.print_grid()

