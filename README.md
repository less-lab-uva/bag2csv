# bag2csv
Interpolated uniformly spaced csv representation of bagged ROS messages

TEST BAGS:
sweep_for_target_test1.bag:
path:        sweep_for_target_test1.bag
version:     2.0
duration:    49.1s
start:       Apr 08 2019 09:57:52.79 (1554731872.79)
end:         Apr 08 2019 09:58:41.90 (1554731921.90)
size:        43.7 MB
messages:    374436
compression: none [53/53 chunks]
types:       dronet_tello/FlightData        [8c659bf934436b7cb2d969ddd123268a]
             dronet_tello/HeadedString      [c99a9440709e4d4a9716d55b8270d5e7]
             geometry_msgs/PoseStamped      [d3812c3cbc69362b77dc0b19b345f8f5]
             geometry_msgs/TransformStamped [b5764a33bfeb3588febc2682852579b0]
             geometry_msgs/Twist            [9f195f881246fdfa2798d1d3eebca84a]
             rosgraph_msgs/Log              [acffd30cd6b6de30f120938c17c593fb]
             std_msgs/Int8                  [27ffa0c9c4b8fb8492252bcad9e5c57b]
topics:      /command_state                         1390 msgs    : dronet_tello/HeadedString     
             /flight_data                         363818 msgs    : dronet_tello/FlightData       
             /machine_state                          923 msgs    : dronet_tello/HeadedString     
             /mission_state                          735 msgs    : dronet_tello/HeadedString     
             /rosout                                1090 msgs    : rosgraph_msgs/Log              (8 connections)
             /user_input                               1 msg     : dronet_tello/HeadedString     
             /velocity                               750 msgs    : geometry_msgs/Twist           
             /vicon/TELLO/TELLO                     2690 msgs    : geometry_msgs/TransformStamped
             /visp_auto_tracker/object_position     1102 msgs    : geometry_msgs/PoseStamped     
             /visp_auto_tracker/status              1102 msgs    : std_msgs/Int8                 
             /warning_state                          835 msgs    : dronet_tello/HeadedString
- one user command around 30 second mark, UserCommand.Land
