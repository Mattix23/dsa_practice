from sort_array import sortArray
def test_sort_array():
    nums1 = [5,4,3,2,1]
    assert sortArray(nums1) == [1,2,3,4,5]

    nums2 = [5,1,1,2,0,0]
    assert sortArray(nums2) == [0,0,1,1,2,5]

