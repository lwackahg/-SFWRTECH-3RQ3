# Lukas Gabrys
# ID - 400423742
# Explanation at bottom

class TrafficLightSystem:
    main_lights = 0
    side_lights = 0

    def set_initial_lights(self):
        pass

    def set_opp_initial_lights(self):
        pass

    def change_main_lights(self):
        pass

    def change_side_lights(self):
        pass


# Ensures that both sets of lights can be set to states
def test_lights():
    lights = TrafficLightSystem()
    lights.set_initial_lights()
    assert lights.main_lights != lights.side_lights, "Main lights should be green (1), Side lights should be red (2)"


# Ensures that both sets of lights can be set to opposite states
def test_lights_2():
    lights = TrafficLightSystem()
    lights.set_opp_initial_lights()
    assert lights.main_lights != lights.side_lights, "Main lights should be red (2), Side lights should be green (1)"


# Ensures that lights are same at red when changing colours
def test_opposite_1():
    lights = TrafficLightSystem()
    lights.set_initial_lights()
    assert lights.main_lights != lights.side_lights, "Main light should be green (1), side light should be red (2)"
    lights.change_main_lights()
    assert lights.main_lights == lights.side_lights, "Main lights should be == to side lights, both red (2)"
    lights.change_side_lights()
    assert lights.side_lights != lights.main_lights, "Main light should be red (2), side light should be green (1)"


# Ensures that lights are same at red when changing colours
def test_opposite_2():
    lights = TrafficLightSystem()
    lights.set_opp_initial_lights()
    assert lights.main_lights != lights.side_lights, "Side light should be green (1), main light should be red (2)"
    lights.change_side_lights()
    assert lights.main_lights == lights.side_lights, "Main lights should be == to side lights, both red (2)"
    lights.change_main_lights()
    assert lights.side_lights != lights.main_lights, "Main light should be green (1), side light should be red (2)"


# Ensures that lights cannot both be green, side lights should not change when main lights are green
def test_opposite_negative_1():
    lights = TrafficLightSystem()
    lights.set_initial_lights()
    assert lights.main_lights != lights.side_lights, "Main light should be green (1), side light should be red (2)"
    lights.change_side_lights()
    assert lights.side_lights != lights.main_lights, "Main light should stay green (1), side light should stay red (2)"


# Ensures that lights cannot both be green, main lights should not change when side lights are green
def test_opposite_negative_2():
    lights = TrafficLightSystem()
    lights.set_opp_initial_lights()
    assert lights.main_lights != lights.side_lights, "Side light should be green (1), main light should be red (2)"
    lights.change_main_lights()
    assert lights.side_lights != lights.main_lights, "Side light should stay green (1), main light should stay red (2)"


# The 6 tests above are all necessary to test requirement (a)
# The first two test are needed because they test if we are able to initialize the lights in either configuration if
# needed the initialization stubs are just used for testing purposes
# The tests named Opposite 1 and 2 are required because we need to make sure both the main and side lights change
# correctly when both sets of lights are red and one of them requires to change to green. In this case we test both
# lights will correctly switch when required to. This allows the ability to test for our requirement of having the
# both sets of lights not to be green.
# The last two tests are the most important because we try to change the lights to a state that should not work.
# If either the main lights or side lights are green, the opposite pair of lights should not change to green. By trying
# to force lights to green while the opposite lights are also green, we except the forced light not to change states.
# By making sure both sets of lights can use their green light and red light, we prove they can use both states.
# By testing if the lights are able to change their colour, prove that they can change
# By trying to change the red light to green before both lights are red, we ensure both lights will never green
# at the same time.

