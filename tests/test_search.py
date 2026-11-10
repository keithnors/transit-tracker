import sys
import os

project_root = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

sys.path.append(project_root)

from functions import *

def test_search_route():

    print("\nSEARCH ROUTE")

    search_route("Manila")

def test_search_vehicle():

    print("\nSEARCH VEHICLE")

    search_vehicle("Victory")

def test_search_departure():

    print("\nSEARCH DEPARTURE")

    search_departure("08:00")


if __name__ == "__main__":

    test_search_route()
    test_search_vehicle()
    test_search_departure()


def test_sort_vehicle():

    print("\nSORT VEHICLE")

    sort_vehicle_name()

def test_sort_passengers():

    print("\nSORT PASSENGERS")

    sort_passengers()


def test_bubble_sort():

    print("\nBUBBLE SORT")

    bubble_sort_passengers()