from handler import LevelOneSupportHandle, LevelTwoSupportHandle
from request import Request

def main():
    level_two = LevelTwoSupportHandle(None)
    level_one = LevelOneSupportHandle(level_two)

    request = Request(2)
    level_one.handle_request(request)

if __name__ == "__main__":
    main()