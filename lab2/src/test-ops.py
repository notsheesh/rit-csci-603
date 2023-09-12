# Test shift letter at index by offset
def test_shift(message: str, letter_index: int, offset: int = 1) -> str: 
    shifted_message = shift(message, letter_index, offset)
    print("Test Shift k times: {} -[{},{}]-> {}".format(message, letter_index, offset, shifted_message))

# Test shift letter by offset
def test_shift_letter(letter: str, offset: int) -> None:
    shifted_letter = shift_letter(letter, offset)
    print("Test Shift Letter: {} -[{}]-> {}".format(letter, offset, shifted_letter))

# Test rotate message
def test_rotate_once(message: str) -> None: 
    print("Test Rotate Message: {} -[1]-> {}".format(message, rotate_once(message)))

# Test rotate message k times
def test_rotate(message: str, k_times: int) -> None: 
    print("Test Rotate Message k Times: {} -[{}]-> {}".format(message, k_times, rotate(message, k_times)))

# Test duplicate letter once 
def test_duplicate_letter(message: str, letter_index: int) -> None: 
    print("Test Duplicate Letter: {} -[1]-> {}".format(message, duplicate_letter(message, letter_index)))

# Test duplicate letter k times  
def test_duplicate(message: str, letter_index: int, k_times: int) -> None:
    print("Test Duplicate Letter k times: {} -[{},{}]-> {}".format(message, letter_index, k_times, duplicate(message, letter_index, k_times)))


def test_trade_ij(message: str, index_i: int, index_j: int) -> str: 
    traded_message = trade_ij(message, index_i, index_j)
    print("Test Trade i,j : {} -[{},{}]-> {}".format(message, index_i, index_j, traded_message))

def test_enc():
    # shift-enc
    print("shift-enc")
    print(shift("BALL", 0) == "CALL")
    print(shift("ZOO", 0, 2) == "BOO")
    print(shift("AAB", 2, -1) == "AAA")
    print(shift("STORE", 1, 9) == "SCORE")
    print(shift("STORE", 4, -18) == "STORM")

    # duplicate-enc
    print("duplicate-enc")
    print(duplicate("HOPED", 0) == "HHOPED")
    print(duplicate("HOPED", 2, 1) == "HOPPED")
    print(duplicate("HOPED", 3, 2) == "HOPEEED") 
    print(duplicate("HOPED", 4, 20) == "HOPEDDDDDDDDDDDDDDDDDDDDD")

    # trade-enc
    print("trade-enc")
    print(trade_ij("SAUCE", 0, 3) == "CAUSE")
    print(trade_ij("FRIED", 1, 2) == "FIRED")
    print(trade_ij("ABCDEFG", 2, 6) == "ABGDEFC")

    # rotate-enc
    print("rotate-enc")
    print(rotate("TOPS") == "STOP")
    print(rotate("TOPS", 1) == "STOP")
    print(rotate("TRAIN", 2) == "INTRA")
    print(rotate("INTRA", -2) == "TRAIN")
    print(rotate("ABCDEFG", -14) == "ABCDEFG")

    # all-enc

    # affine-enc

def test_dec():
    # duplicate-dec
    print("duplicate-dec")
    print(remove_duplicate("HHOPED", 0) == "HOPED")
    print(remove_duplicate("HOPPED", 2, 1) == "HOPED")
    print(remove_duplicate("HOPEEED", 3, 2) == "HOPED")
    print(remove_duplicate("HOPEDDDDDDDDDDDDDDDDDDDDD", 4, 20) == "HOPED")

    # shift-dec
    print("shift-dec")
    print(shift("CALL", 0, -1) == "BALL")
    print(shift("BOO", 0, -2) == "ZOO")
    print(shift("AAA", 2, 1) == "AAB")
    print(shift("SCORE", 1, -9) == "STORE")
    print(shift("STORM", 4, 18) == "STORE")

    # trade-dec
    print("trade-dec")
    print(trade_ij("CAUSE", 0, 3) == "SAUCE")
    print(trade_ij("FIRED", 1, 2) == "FRIED")
    print(trade_ij("ABGDEFC", 2, 6) == "ABCDEFG")

    # rotate-dec
    print("rotate-dec")
    print(rotate("STOP", -1) == "TOPS")
    print(rotate("STOP", -1) == "TOPS")
    print(rotate("INTRA", -2) == "TRAIN")
    print(rotate("TRAIN", 2) == "INTRA")
    print(rotate("ABCDEFG", 14) == "ABCDEFG")

    # all-dec

    # affine-dec
