# Lukas Gabrys
# ID - 400423742
# Explanation at bottom

class TrafficLightSystem:
    main_lights = 0
    main_crosswalk = 0

    side_lights = 0
    side_crosswalk = 0

    def set_initial_lights(self):
        pass

    def set_opp_initial_lights(self):
        pass

    def change_main_lights(self):
        pass

    def change_side_lights(self):
        pass

    def change_main_crosswalk(self):
        pass

    def change_side_crosswalk(self):
        pass


# Ensures that main crosswalk sets green when set_initial_lights is used
def test_main_crosswalk():
    lights = TrafficLightSystem()
    lights.set_initial_lights()
    assert lights.main_crosswalk == 1, "Main crosswalk should be green (1)"


# Ensures that main crosswalk can be red while main lights are green
def test_greenmain_redcrosswalk():
    lights = TrafficLightSystem()
    lights.set_initial_lights()
    lights.change_main_crosswalk()
    assert lights.main_crosswalk == 2, "Main crosswalk should be red (2)"


# Ensures that the main crosswalks changes when the main lights turn red
def test_normal_main_crosswalk():
    lights = TrafficLightSystem()
    lights.set_initial_lights()
    lights.change_main_lights()
    assert lights.main_crosswalk == 2, "Main crosswalk should become red (2)"


# Ensures that the main crosswalks cannot change green when main lights are red
def test_negative_main_crosswalk():
    lights = TrafficLightSystem()
    lights.set_opp_initial_lights()
    lights.change_main_crosswalk()
    assert lights.main_crosswalk == 2, "Main crosswalk should still be red (2)"


# Ensures that side crosswalk sets green when set_opp_initial_lights is used
def test_side_crosswalk():
    lights = TrafficLightSystem()
    lights.set_opp_initial_lights()
    assert lights.side_crosswalk == 1, "Side crosswalk should be green (1)"


# Ensures that side crosswalk can be red while side lights are green
def test_greenside_redcrosswalk():
    lights = TrafficLightSystem()
    lights.set_opp_initial_lights()
    lights.change_side_crosswalk()
    assert lights.side_crosswalk == 2, "Side crosswalk should be red (2)"


# Ensures that the side crosswalks changes when the side lights turn red
def test_abnormal_side_crosswalk():
    lights = TrafficLightSystem()
    lights.set_opp_initial_lights()
    lights.change_side_lights()
    assert lights.side_crosswalk == 2, "Side crosswalk should become red (2)"


# Ensures that the side crosswalks cannot change when side lights are red
def test_negative_side_crosswalk():
    lights = TrafficLightSystem()
    lights.set_initial_lights()
    lights.change_side_crosswalk()
    assert lights.side_crosswalk == 2, "Side crosswalk should still be red (2)"


# The 8 tests above are all necessary to test requirement (b)
# Each crosswalk has 4 tests, the first two for both crosswalks are test_main_crosswalk and test_side_crosswalk.
# These two tests ensure that when we initialize the lights, the crosswalk lights match their respective light
# The next two, greenmain_redsidewalk and greenside_redsidewalk test that possibility to make the crosswalk red
# even if its light is green. There may not always be a need for a green walk signal when the light is green.
# The tests abnormal_main and abnormal_side make sure that the crosswalks changes correctly when the lights changes
# to red. No matter the case, if the light goes red, so should the crosswalk because there cannot be a green crosswalk
# on a red light.
# Lastly, the negative_main and negative_side test ensure that the crosswalk lights cannot switch to green while its
# matching traffic light is red.
# These tests are sufficient because we have proved the signal matches the light when initialized and when the light
# changes colour.
# We made sure that while the light may be green, the crosswalk does not need to be green
# By changing the light while the crosswalk is green, we make sure the crosswalk swaps to red when that happens.
# By trying to change the crosswalk to green while the light is red, we prove we met the requirement.


