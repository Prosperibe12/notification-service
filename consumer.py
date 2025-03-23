import os, sys, pika
from send.email import ConsumerNotification

def main():
    """
    Converter Service receives messages from the video queue and processes it, proceesed messages are sent back to
    the mp3 queue for consumption by the notification service. 
    """
    # create a connection to Rabbitmq
    # connection = pika.BlockingConnection(pika.URLParameters("amqp://guest:guest@rabbitmq:5672/"))
    # channel = connection.channel()
    
    parameters = pika.ConnectionParameters(
        host="rabbitmq",  
        port=5672,  
        credentials=pika.PlainCredentials("guest", "guest"),
        heartbeat=30,
        blocked_connection_timeout=300,
        connection_attempts=10,
        retry_delay=5,
        socket_timeout=120
    )

    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()
        
    # define a callback function
    def callback(ch, method, properties, body):
        """
        execute the function when a message is received in the queue
        """
        # convert the video to mp3
        err = ConsumerNotification.notification(body)
        if err:
            # acknowledge message failure
            ch.basic_nack(delivery_tag=method.delivery_tag)
        else:
            # acknowledge message delivery
            ch.basic_ack(delivery_tag=method.delivery_tag)
            
    # consume messages from the queue
    channel.basic_consume(
        queue=os.environ.get("MP3_QUEUE"), on_message_callback=callback
    )
    print('[*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()
    
if __name__ == "__main__":
    try:
        # start listening on the queue for messages
        main()
    except KeyboardInterrupt:
        print("Interruped")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)