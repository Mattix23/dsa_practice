from algorithmic_one import find_single_num

def test_find_single_num():
    nums1 = [2,2,1]
    expected1 = 1
    assert find_single_num(nums1) == expected1

    nums2 = [[3,3,4,5,5,6,6]]
    expected2 = 4
    assert find_single_num(nums2) == expected2