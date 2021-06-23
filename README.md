# bag2csv
Interpolated uniformly spaced csv representation of bagged ROS messages

bag_reader.py -- no interpolation

bag_reader2.py -- interpolation and uniform spacing between messages such that each row is one timestep apart. Timestep is determined by subdivision of message frequencies.

test_hz.py -- test Hz of messages published in bag.
