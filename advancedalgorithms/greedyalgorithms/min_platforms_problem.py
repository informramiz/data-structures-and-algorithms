"""
Author: Ramiz Raja
Created on: 20/01/2020

Problem: Given arrival and departure times of trains on a single day in a railway platform,
find out the minimum number of platforms required so that no train has to wait for the other(s) to leave.

You will be given arrival and departure times in the form of a list.

Note: Time hh:mm would be written as integer hhmm for e.g. 9:30 would be written as 930. Similarly,
13:45 would be given as 1345
"""
from asserts.asserts import assert_


def min_platforms(arrival, departure):
    arrival.sort()
    departure.sort()

    # Solution: At any point (or arrival or departure) we calculate the total number of trains on the platform.
    # the maximum number of trains present at any given time on station is minimum number of platforms required is 3.

    total_trains = len(arrival)
    # index of the train just arriving
    arriving_train_index = 1
    # index of the firstly arrived train on the station which still has not departed yet
    firstly_arrived_train_index = 0

    # train at 0 index is considered already arrived (as firstly_arrived_train_index = 0) so
    trains_currently_present_on_platform = 1
    max_trains_overlap_at_any_moment = 1

    while arriving_train_index < total_trains and firstly_arrived_train_index < total_trains:
        # a new train (current_train) has arrived. Check if there is an overlap or not
        if arrival[arriving_train_index] < departure[firstly_arrived_train_index]:
            # a new train has arrived and the last one has not departed yet so increase trains count
            # currently present at the station
            trains_currently_present_on_platform += 1

            # as max trains at station at any given moment defines the required
            # stations so keep track of max trains at the station at any moment
            if trains_currently_present_on_platform > max_trains_overlap_at_any_moment:
                max_trains_overlap_at_any_moment = trains_currently_present_on_platform

            # get the next train ready to process
            arriving_train_index += 1
        else:  # departure[firstly_arrived_train_index] <= arrival[arriving_train_index]

            # depart the firstly arrived train as it's departure time has arrived.
            # Note: We will note increment "arriving_train_index" until all trains that
            # need to depart (departure[firstly_arrived_train_index] <= arrival[arriving_train_index]) have departed
            firstly_arrived_train_index += 1
            # a train has departed so decrease the count of currently present trains
            trains_currently_present_on_platform -= 1

    # max overlap at any moment is the min number of required stations
    return max_trains_overlap_at_any_moment


def test_function(test_case):
    arrival = test_case[0]
    departure = test_case[1]
    solution = test_case[2]
    output = min_platforms(arrival, departure)
    assert_(expected=solution, actual=output)


def tests():
    arrival = [900, 940, 950, 1100, 1500, 1800]
    departure = [910, 1200, 1120, 1130, 1900, 2000]
    test_case = [arrival, departure, 3]
    test_function(test_case)

    arrival = [200, 210, 300, 320, 350, 500]
    departure = [230, 340, 320, 430, 400, 520]
    test_case = [arrival, departure, 2]
    test_function(test_case)


tests()
