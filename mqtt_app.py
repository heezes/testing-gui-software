from PyQt5 import QtCore, QtGui, QtWidgets
import paho.mqtt.client as mqtt
import time
import sys
import json

SUBSCRIPTION_TOPIC  =   "vim/subscribe"
DEBUG_PUBLISH_TOPIC =   "vim/debug_publish"
INFO_PUBLISH_TOPIC  =   "vim/info_publish"

UNLOCK_OPCODE       =   1
LOCK_OPCODE         =   2
SYNC_OPCODE         =   5
THEFT_OPCODE        =   8
EXIT_OPCODE         =   6
LOOP_OPCODE         =   7

class mqtt_application():
    def __init__(self, ui):
        self.ui = ui
        self.mqttc  = mqtt.Client()
        self.mqttc.username_pw_set(username='munnvxsn', password='unegqTSYxMKO')
        self.mqttc.on_connect = self.on_connect
        self.mqttc.on_message = self.on_message
        self.mqttc.on_disconnect = self.on_disconenct
        self.mqttc.connect_async("m11.cloudmqtt.com", 19845, 60)
        self.mqttc.loop_start()

    """
    @brief: Callback function for mqtt connection
    @param: client: client handle
    @param: userdata: data passed to user via stack
    @param: flags: mqtt flag
    @params: rc: return code
    """
    def on_connect(self, client, userdata, flags, rc):
        # self.mqtt_connected = True
        # Subscribing in on_connect() means that if we lose the connection and
        # reconnect then subscriptions will be renewed.
        client.subscribe(INFO_PUBLISH_TOPIC)#as the raspberry publishes on this topic


    """
    @brief: Callback function when data is recieved on subscribed topic
    @param: client: client handle
    @param: userdata: data passed to user via stack
    @param: msg: data received on subscribed topic
    """
    def on_message(self, client, userdata, msg):
        print(msg.topic+" "+str(msg.payload))
        display_msg = msg.payload.decode()
        try:
            _translate = QtCore.QCoreApplication.translate
            self.ui.operation_status.setText(_translate("MainWindow",display_msg))
            # self.ui.operation_status.setAlignment(Qt.AlignJustify)
            self.ui.operation_status.adjustSize()
        except Exception as e :
            print(e)
            pass
        # if(self.isNumeric(str(msg.payload))):
        #     self.test_request = int(msg.payload.strip())

    """
    @brief: Callback function for mqtt disconnection
    @param: client: client handle
    @param: userdata: data passed to user via stack
    @params: rc: return code
    """
    def on_disconenct(self, client, userdata, rc):
        print("Disconected with result code: "+str(rc))
        # self.mqtt_connected = False

    """
    @brief: Send message to the remote  mqtt server
    @param: message: Data to be sent
    """
    def sendInfo(self, message):
        #raspberry is listening to this topic
        self.mqttc.publish(SUBSCRIPTION_TOPIC,str(message), qos=1, retain=False)

    #[mode, wait_time, count, timeout, ...]
    def lockPressed(self):
        message = {}
        message['cmd'] = LOCK_OPCODE
        message['arg'] = []
        arguments = []
        if self.ui.modeSelector.currentText().find("BLE") > -1:
            arguments.append(0)
        else:
            arguments.append(1)
        arguments.append(self.ui.wait_time.value())
        arguments.append(self.ui.count.value())
        arguments.append(self.ui.timeout.value())
        for i in range(len(arguments)):
            message['arg'].append(arguments[i])
        self.sendInfo(json.dumps(message))

    def unlockPressed(self):
        message = {}
        count = self.ui.count.value()
        if(count > 1):
            message['cmd'] = LOOP_OPCODE
        else:
            message['cmd'] = UNLOCK_OPCODE
        message['arg'] = []
        arguments = []
        if self.ui.modeSelector.currentText().find("BLE") > -1:
            arguments.append(0)
        else:
            arguments.append(1)
        arguments.append(self.ui.wait_time.value())
        arguments.append(count)
        arguments.append(self.ui.timeout.value())
        for i in range(len(arguments)):
            message['arg'].append(arguments[i])
        print(json.dumps(message))
        self.sendInfo(json.dumps(message))

    def exitPressed(self):
        message = {}
        message['cmd'] = EXIT_OPCODE
        input_msg = self.ui.input_msg.text()
        if(len(input_msg) > 0):
            message['msg'] = input_msg
        # message['arg'] = []
        # arguments = []
        # if self.ui.modeSelector.currentText().find("BLE"):
        #     arguments.append(0)
        # else:
        #     arguments.append(1)
        # arguments.append(self.ui.wait_time.value())
        # arguments.append(self.ui.count.value())
        # arguments.append(self.ui.timeout.value())
        # for i in range(len(arguments)):
        #     message['arg'].append(arguments[i])
        self.sendInfo(json.dumps(message))
        self.ui.input_msg.setText("")

    def syncPressed(self):
        message = {}
        message['cmd'] = SYNC_OPCODE
        # message['arg'] = []
        # arguments = []
        # if self.ui.modeSelector.currentText().find("BLE"):
        #     arguments.append(0)
        # else:
        #     arguments.append(1)
        # arguments.append(self.ui.wait_time.value())
        # arguments.append(self.ui.count.value())
        # arguments.append(self.ui.timeout.value())
        # for i in range(len(arguments)):
        #     message['arg'].append(arguments[i])
        self.sendInfo(json.dumps(message))

    def theftPressed(self):
        message = {}
        message['cmd'] = THEFT_OPCODE
        # message['arg'] = []
        # arguments = []
        # if self.ui.modeSelector.currentText().find("BLE"):
        #     arguments.append(0)
        # else:
        #     arguments.append(1)
        # arguments.append(self.ui.wait_time.value())
        # arguments.append(self.ui.count.value())
        # arguments.append(self.ui.timeout.value())
        # for i in range(len(arguments)):
        #     message['arg'].append(arguments[i])
        self.sendInfo(json.dumps(message))
