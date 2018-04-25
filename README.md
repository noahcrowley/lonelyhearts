# Project Night: Lonely Heart's Club

These materials are intended to accompany the "Project Night: Lonely Heart's Club" intro to time series workshop.

## Pulse Sensor and Arduino

Plug your Arduino into your laptop; the pulse sensor should power on and the green LED should light up.

Install the Arduino IDE and the Adafruit Trinket M0 board description. Check that the port for your board is set. Load the sketch onto your board. Check that it's working using Arduino's built-in serial plotter and serial monitor.

Hold the heartbeat sensor against your fingertip. You might have to adjust the pressure a bit before you get a clear reading, but once you do you should be able to make out the heartbeat waveform. The LED on the Arduino should also blink for each heartbeat. The LED turns on when the sensor value exceeds a certain amount, and turns off again when it dips back below the threshold.

If the LED on the Arduino isn't blinking, you'll need to adjust the threshold.

## Telegraf Setup

Let's start by setting up Telegraf. If you don't already have it installed on your machine, you can find [installation instructions here](https://docs.influxdata.com/telegraf/v1.6/introduction/installation/). Once you have Telegraf installed, you can generate a new configuration file by entering the following commands in your terminal:

```telegraf --sample-config -input-filter socket_listener -output-filter influxdb```

Edit this file with the correct IP address, ports, etc. The workshop organizer will be able to provide you with the information needed to connect to the database for the workshop.

Save the config and start telegraf using

```telegraf -config nameofconfig.conf```

## Python Relay

The last component we need to put in place is the relay script, which should work with both Python 2 and Python 3. It has one dependency, the pyseril library, which we're going to install using `pip`.

If you do a lot of Python development, you might want to use a tool like virtualenv to keep your projects, and their dependencies, separate. If you're working with Python and serial a lot, however, it can be nice to have the library installed and available so you can drop into an interactive interpreter and use it there.

```
$ python3 -m pip install pyserial
```

Next, you'll need to get the relay script and set a few variables. The `name` variable will be used as a tag in InfluxDB, and the `port` variable is the Arduino's serial port.

You can find out your serial port by looking in the Arduino IDE by navigating to "Tools > Port".

IMAGE

Change the variables using a text editor, then save and run the script as follows:

```
$ python3 ./relay.py
```

As the script reads data from the serial port and sends it to Telegraf, it also prints it to the console. If your Arduino is connected and powered on you should begin to see data being printed to the terminal. 

## Visualizing with Chronograf

To verify that everything is working we can use Chronograf.

The workshop organizer will demostrate this for the group, but you can also install Chronograf locally and walk through this process if you have the time.

Connect to the instance and navigate to the Data Explorer. You should see the `telegraf` database; connect to it and you should also see our `heartbeat` measurements.

Each participant should be sending their name and hostname along with the data, so we can sort by those tags in order to get graphs of each individual's heartbeats.

Select the values. You might have to turn off the aggregation functions in order to see the full waveform.
