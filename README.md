# onvif-simulator

Simulates the behavior of an onvif camera which returns the current frame via an http request. 

For a camera, add 4 files on /static/cameras/{camera_id}/ with names 1.jpg, 2.jpg, 3.jpg. 
The 4 frames will simulate a loop for 1 minute (first 15 seconds - return 1.jpg, seconds 15-30 - return 2.jpg, etc)

Frames can pe accessed via url/cameras/{camera_id}