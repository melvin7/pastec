#!/usr/bin/python3

class Reply():
    OK = 1
    ERROR_GENERIC = 2
    PONG = 3
    WRONG_MODE = 10
    IMAGE_DATA_TOO_BIG = 20
    IMAGE_NOT_INDEXED = 21
    IMAGE_SIZE_TOO_BIG = 22
    IMAGE_NOT_DECODED = 23
    
class Query():
    INIT_BUILD_FORWARD_INDEX = 1
    BUILD_BACKWARD_INDEX = 2
    INIT_SEARCH = 3
    INDEX = 10
    INDEX_IMAGE = 11
    PING = 20
    STOP = 30
    SEARCH = 40