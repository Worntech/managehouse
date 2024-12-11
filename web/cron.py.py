from django_cron import CronJobBase, Schedule
from django.utils.timezone import now
import paho.mqtt.client as mqtt
from .models import MyPayment

# MQTT Broker details
mqtt_broker = "164.90.230.152"
mqtt_port = 1883

class CheckAndUpdateDoorsCronJob(CronJobBase):
    schedule = Schedule(run_every_mins=5)  # Runs every 5 minutes
    code = 'web.check_and_update_doors'  # A unique code for this cron job

    def do(self):
        # Fetch expired payments where the current time is >= end_date
        expired_payments = MyPayment.objects.filter(end_date__lte=now(), Payment_status='paid')

        for payment in expired_payments:
            room_number = payment.Room.Room_Number
            try:
                # Send request to ESP8266 based on room number
                if room_number == "1":
                    topic = f"home/esp8266/mydevicecontrol/control"
                    client = mqtt.Client()
                    client.connect(mqtt_broker, mqtt_port, 60)
                    client.publish(topic, 'highdoorone')
                elif room_number == "2":
                    topic = f"home/esp8266/mydevicecontrol/control"
                    client = mqtt.Client()
                    client.connect(mqtt_broker, mqtt_port, 60)
                    client.publish(topic, 'highdoortwo')
                # Add similar logic for other rooms if needed

                # Update Payment_status to reflect the action
                payment.Payment_status = 'expired'
                payment.save()
            except:
                pass
