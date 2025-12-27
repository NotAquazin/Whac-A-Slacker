# Whac-A-Slacker
A lightweight slacker detector app that reminds you to get back to locking in on your work.
It detects which window or tab you're currently focused on and rings an alarm when you're on
a non-productive window. It also locally logs all window focus change to help you keep track
of how much you tend to lock out.

Current features:
- Window/tab detection
- Event logging (all window focus change)
- Alarm ringing when distracted
- Starting and stopping detection
- light-weight background operation

Upcoming Features:
- UI for defining productive vs non-productive windows/tabs
- Cutomizability 
    (Custom alarms, 
    Alarm volume, 
    Default label for undefined windows/tabs, 
    Slider for delay before alarm rings, 
    and more)
- Configurable Facial direction detection using Computer Vision 
    (May be used to ensure user is not distracted on their phone)
  
---------------------------------------------------------------------------------------    

Dependencies for development:
- Python 3.13 (3.14 not supported yet by pythonnet)
- pywebview
- pythonnet
- pywin32
- JS
