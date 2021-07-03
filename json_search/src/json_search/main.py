from loguru import logger
import os

def adder(i1, i2):
    return (i1 + i2)

def main():
    print("Cool json_search project!")
    logger.info("We are here: {}".format(os.path.abspath(__file__)))
   # logger.info("Adding integers {0} and {1}. Result: {2}".format(1, 2, adder(1, 2)))
  #  logger.info("Adding floats {0} and {1}. Result: {2}".format(1.0, 2.0, adder(1.0, 2.0)))
   # logger.info("Adding strings {0} and {1}. Result: {2}".format(1, 2, adder("1", "2")))


if __name__ == "__main__":
    main()