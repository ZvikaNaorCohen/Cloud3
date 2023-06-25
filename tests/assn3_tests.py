import pytest
import sys
import connectionController
from assertions import *


def test_insert_three_dishes():
    word1 = "orange"
    word2 = "spaghetti"
    word3 = "apple pie"
    response1 = connectionController.http_post("dishes", data={'name': word1})
    response2 = connectionController.http_post("dishes", data={'name': word2})
    response3 = connectionController.http_post("dishes", data={'name': word3})

    assert response1.status_code == 201
    assert response2.status_code == 201
    assert response3.status_code == 201

    assert response1.json() != response2.json() != response3.json()

'''
Execute a GET dishes/<orange-ID> request, using the ID of the orange dish.
The test is successful if:
 (i) the sodium field of the return JSON object is between .9 and 1.1 and
 (ii) the return status code from the request is 200.
'''


'''
Execute a GET /dishes request.
The test is successful if:
 (i) the returned JSON object has 3 embedded JSON objects (dishes)
 (ii) the return status code from the GET request is 200.
'''


def test_insert_dish_doesnt_exist():
    word1 = "blah"
    response1 = connectionController.http_post("dishes", data={'name': word1})

    assert response1.json() == -3
    assert response1.status_code == 404 or response1.status_code == 400 or response1.status_code == 422


'''
Perform a POST dishes request with the dish name “orange”. 
The test is successful if:
 (i) the return value is -2 (same dish name as existing dish)
 (ii) the return status code is 400 or 404 or 422.
'''


def test_insert_dish_already_exists():
    word1 = "orange"
    response1 = connectionController.http_post("dishes", data={'name': word1})

    assert response1.json() == -2
    assert response1.status_code == 404 or response1.status_code == 400 or response1.status_code == 422


'''
Perform a POST /meals request specifying that the meal name is “delicious”, and that it contains:
an “orange” for the appetizer, “spaghetti” for the main, and “apple pie” for the dessert (note you will need to use their dish IDs).
The test is successful if:
(i) the returned ID > 0 
(ii) the return status code is 201.
'''


'''
Perform a GET /meals request. 
The test is successful if:
(i) the returned JSON object has 1 meal
(ii) the calories of that meal is between 400 and 500
(iii) the return status code from the GET request is 200.
'''


'''
Perform a POST /meals request as in test 6 with the same meal name (and courses can be the same or different). 
The test is successful if:
(i) the code is -2 (same meal name as existing meal) 
(ii) the return status code from the request is 400 or 422.
'''