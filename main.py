import logging
logging.basicConfig(filename="log.txt", level=logging.DEBUG,
                    format="%(asctime)s %(message)s")

print('Hello World')
addMongoData = 12
logging.debug("Logging test..."+str(addMongoData)+"WOW")