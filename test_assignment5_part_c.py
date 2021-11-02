# Lukas Gabrys
# ID - 400423742
# Explanation at bottom

class TrafficLightSystem:
    main_lights = 0
    main_crosswalk = 0

    side_lights = 0
    side_crosswalk = 0

    sensor = 0
    wait_time = 0
    car_less_wait_time = 0

    def set_initial_lights(self):
        pass

    def set_opp_initial_lights(self):
        pass

    def change_main_lights(self):
        pass

    def change_side_lights(self):
        pass

    def act_traffic_sensor(self):
        pass


# Ensure sensor notices a car on it
def test_sensor():
    lights = TrafficLightSystem()
    assert lights.sensor == 0, "Traffic sensor start unactivated"
    lights.act_traffic_sensor()
    assert lights.sensor == 1, "Activate traffic sensor, 1 means a car is waiting after checking the sensor"


# Ensure no_car timer runs
def test_no_car_timer():
    lights = TrafficLightSystem()
    assert lights.sensor == 0, "Traffic sensor start unactivated"
    assert lights.car_less_wait_time > 0, "No traffic on the side street sensor, the side timer starts counting"


# Ensure timer is started when car arrives
def test_timer():
    lights = TrafficLightSystem()
    assert lights.wait_time == 0, "Ensure timer starts at zero"
    lights.act_traffic_sensor()
    assert lights.wait_time > 0, "Sensor should start the timer, therefore anything above 0 works"


# Ensure car less timer is reset when car arrives
def test_reset_no_car_timer():
    lights = TrafficLightSystem()
    assert lights.car_less_wait_time > 0, "Ensure car less timer was running"
    lights.act_traffic_sensor()
    assert lights.car_less_wait_time == 0, "Car less timer should reset when traffic sensor is active"


# Ensure that the main lights and side lights do not change when the timer is under 90 seconds of waiting
def test_mts_under_time():
    lights = TrafficLightSystem()
    lights.set_initial_lights()
    lights.act_traffic_sensor()
    assert lights.wait_time <= 90, "Do not change lights before 90 seconds of sensor activation"
    lights.change_main_lights()
    assert lights.main_lights == 1, "Main lights should be green"
    lights.change_side_lights()
    assert lights.side_lights == 2, "Side lights should be red"


# Ensure that the main lights and side lights do change when the timer is over 90 seconds of waiting
def test_mts_over_time():
    lights = TrafficLightSystem()
    lights.set_initial_lights()
    assert lights.act_traffic_sensor()
    assert lights.wait_time > 90, "Change lights after 90 seconds of sensor activation"
    lights.change_main_lights()
    assert lights.main_lights == 2, "Main lights should be red"
    lights.change_side_lights()
    assert lights.main_lights == 1, "Side lights should be green"


# Ensure that the side lights do not change when the timer is under 30 seconds of no cars
def test_stm_under_time():
    lights = TrafficLightSystem()
    lights.set_opp_initial_lights()
    assert lights.sensor == 0, "Sensor should not be active"
    assert lights.car_less_wait_time <= 30, "No cars for under 30 seconds"
    lights.change_side_lights()
    assert lights.side_lights == 1, "Side lights should remain green"
    lights.change_main_lights()
    assert lights.main_lights == 2, "Main lights should remain red"


# Ensure that the side lights do change when the timer is over 30 seconds of no cars
def test_stm_over_time():
    lights = TrafficLightSystem()
    lights.set_opp_initial_lights()
    assert lights.sensor == 0, "Sensor should not be active"
    assert lights.wait_time > 30, "No cars for over 30 seconds"
    lights.change_side_lights()
    assert lights.side_lights == 2, "Side lights should change to red"
    lights.change_main_lights()
    assert lights.main_lights == 1, "Main lights should be green"

# The 8 tests above are all necessary to test requirement (c)
# It is assumed that set_initial and set_opp_initial stubs work from previous tests.
# The first three tests ensure that our sensor is activated when a car arrives, the light timer is started when the
# sensor activates and the no wait timer is reset when the sensor is activated.
# Tests mts_under and mts_over, that the light cannot be changed when the timer conditions have not been met.
# mts_under tried to change the main light while the wait_timer is still under 90 seconds
# mts_over makes sure that the main light and side light change in the correct order after the timer has reached 90s
# Lastly the stm_under and stm_over tests are required to ensure the side lights wait a full 30 seconds after
# the last car has crossed the side lights. We ensure the sensor is not active, the timer is under 30 and we try
# to change the side lights to red. We expect this not to work. Stm_over ensures the sensor is not active and the
# time is over 30 seconds. Therefore we expect the side lights to change to red and main lights change to green.
# These tests are sufficient because ensure the senor and timers would and act appropriately by forcing them on or off
# By trying to force lights to change prior to the appropriate time, we prove that the lights cannot be changed until
# timer conditions have been met as well.
