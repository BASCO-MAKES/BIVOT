import xbee


print(" +--------------------------------------+")
print(" | XBee MicroPython Receive Data Sample |")
print(" +--------------------------------------+\n")

print("Waiting for data...\n")

while True:
    # Check if the XBee has any message in the queue.
    received_msg = xbee.receive()
    if received_msg:
        # Get the sender's 64-bit address and payload from the received message.
        sender = received_msg['sender_eui64']
        payload = received_msg['payload']
        print("Data received from %s >> %s" % (''.join('{:02x}'.format(x).upper() for x in sender),
                                               payload.decode()))
