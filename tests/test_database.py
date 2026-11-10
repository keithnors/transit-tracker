import sys
import os

from database import delete_record, update_record

sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)
"""  
TESTING DATABASE.PY FUNCTIONS  
from database import *

def test_view_records():

    print("\nTESTING VIEW RECORDS")
    view_records()


if __name__ == "__main__":
    test_view_records()
"""


"""   
TESTING ADD RECORD FUNCTION
from database import *

def test_add_record():

    print("\nTESTING ADD RECORD")

    add_record(
        "TEST BUS",
        "TEST ROUTE",
        "08:00",
        "10:00",
        25
    )

    print("Add Record Test Passed")


if __name__ == "__main__":
    test_add_record()
"""

"""
TESTING UPDATE RECORD FUNCTION
def test_update_record():

    print("\nTESTING UPDATE RECORD")

    update_record(
        1,
        "UPDATED BUS",
        "UPDATED ROUTE",
        "09:00",
        "11:00",
        50
    )

    print("Update Test Passed")
"""


"""
TESTING DELETE RECORD FUNCTION
def test_delete_record():

    print("\nTESTING DELETE RECORD")

    delete_record(1)

    print("Delete Test Passed")
"""