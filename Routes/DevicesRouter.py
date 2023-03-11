from Controller.DeviceController import DeviceController
from flask import Flask, jsonify, request

from __main__ import app

devices = DeviceController()

# Every devices
@app.route('/devices', methods=['GET'])
def getDevices():
    #devices = DeviceController.getDevices()
    #return jsonify({"Devices":devices})
    return DeviceController.getDevices()

# Single Device
@app.route('/devices/<string:device_id>', methods=['GET'])
def getDevice(device_id):
    deviceFound = devices.getDevice(device_id)
    if (deviceFound != False):
        return jsonify({'device': deviceFound})
    return jsonify({'message': 'Device Not found'}), 400

# Create device
@app.route('/devices', methods=['POST'])
def addDevice():
    new_device = Device(request.json['id'], request.json['name'], request.json['code'], 
                        request.json['description'], request.json['image'], '', '')
    if (devices.addDevice(new_device)):
        return devices.getDevice()
    return jsonify({'message': 'Device can not be added'})
    
#Update device
@app.route('/devices/<string:device_id>', methods=['PUT'])
def editDevice(device_id):
    deviceFound = devices.getDevice(device_id)
    device_editted = Device(request.json['id'], request.json['name'], request.json['code'], 
                        request.json['description'], request.json['image'], '', '')
    if(devices.updatedDevice(deviceFound, device_editted)):
        return jsonify({
            'message': 'Device Updated',
            'device': devices.getDevice(device_id)
        })
    return jsonify({'message': 'Device Not found'})

#Delete device
@app.route('/devices/<string:device_id>', methods=['DELETE'])
def deleteDevice(device_id):
    deviceFound = devices.getDevice(device_id)
    if(devices.deleteDevice(deviceFound)):
        return jsonify({
            'message': 'Device Deleted',
            'device': devices.getDevices()
        })
    return jsonify({'message': 'Device Not found'})