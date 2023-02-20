import logging
import dz_15_1


def main():
    """
    The main entry point of the application
    """

    logger = logging.getLogger("exampleApp")
    logger.setLevel(logging.INFO)

    # create the logging file handler
    filehand = logging.FileHandler("write_log.log")

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    filehand.setFormatter(formatter)

    # add handler to logger object
    logger.addHandler(filehand)

    logger.info("Program started")
    start_server = dz_15_1.my_server()
    logger.info("Done!")


if __name__ == "__main__":
    main()