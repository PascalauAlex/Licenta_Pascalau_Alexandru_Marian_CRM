from datetime import date, datetime


def checkForInactivity(last_modified:date) -> bool:
    """This function checks every time a request is made , if the last_modified is bigger than 3 days from current date
    """
    threeDays = 3 * 24 * 60 * 60 * 1000

    last_modified = datetime(last_modified)
    timePassed = datetime.now() - last_modified

    if timePassed > threeDays:
        return True
    else:
        return False





