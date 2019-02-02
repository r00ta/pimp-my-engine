# pimp-my-engine

This project aims to make your cheap car sound like a Ferrari. How? 

Pretty simple to be honest: you will need just

1) a raspberry pi (or a laptop)
2) connect the AUX of the raspberry pi to the car radio
3) plug an OBDII dongle in your car (like this http://www.obdlink.com/sxusb/) 
4) run the main application of this project.
5) Raise the volume and cover your ears baby.

The main idea is to generate the sound of a sporty car based on the RPM your the car. 

## Installation 

```bash
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
git clone https://github.com/r00ta/python-OBD_multi.git
cd python-OBD_multi
git checkout multi-command
python setup.py install
```

