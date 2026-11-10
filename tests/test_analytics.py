import sys
import os

project_root = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

sys.path.append(project_root)

from analytics import *

def run_all_tests():

    print("\n=== ANALYTICS TESTS ===")

    total_passengers()
    average_passengers()
    most_used_route()
    most_used_vehicle()
    route_statistics()

if __name__ == "__main__":
    run_all_tests()