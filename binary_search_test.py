from binary_search import search_for_num

def test_search_for_num():
    num_list = [1,2,3,4,5]
    assert search_for_num(num_list, 3) == 2, "the target number is 3 and the index is 2"

def test_search_for_num_return_negative_one():
    num_list = [1,2,3,4,5]
    assert search_for_num(num_list, 6) == -1, "the target number doesn't exist so return -1"
