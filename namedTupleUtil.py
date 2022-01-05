from collections import namedtuple
if __name__ == "__main__":
    # Instead of this
    tupleData = (1, True, "red")
    # Use this
    tupleData = namedtuple('tupleData', 'count enabled color')
    test = tupleData(count=1, enabled=True, color="red")
    print(test.count)
    print(test.enabled)
    print(test.color)

    """ 
    Output:
            1
            True
            red
    """