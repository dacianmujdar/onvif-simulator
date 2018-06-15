from django.http import Http404
from django.http import HttpResponse
import time


def camera_view(request, pk):
    # get current timestamp
    timestamp = int(round(time.time()))

    current_second = timestamp % 60

    # for seconds 0 to 15 - show picture 1
    picture_index = 1

    # for seconds 15 to 30 - show picture 2
    if current_second >= 15 and current_second < 30:
        picture_index = 2

    # for seconds 30 to 45 - show picture 3
    if current_second >= 30 and current_second < 45:
        picture_index = 3

    # for seconds 45 to 60 - show picture 4
    if current_second >= 45:
        picture_index = 4
    try:
        # get image
        image_data = open("onvif_simulator/static/parkings/{}/{}.jpg".format(pk, picture_index), "rb").read()
        return HttpResponse(image_data, content_type="image/png")
    except:
        raise Http404

