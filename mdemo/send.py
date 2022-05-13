import argparse
from google.cloud import pubsub_v1


parser = argparse.ArgumentParser()
parser.add_argument("--filename", type=str, required=True)
parser.add_argument("--projectid", type=str, required=True)
parser.add_argument("--topic", type=str, required=True)
args = parser.parse_args()
input_file = args.filename
project = args.projectid
topic = args.topic


publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(project,topic)
print(f'this is the topic path{topic_path}')

with open(input_file) as f:
    lines = f.readlines()
    for line in lines:
        print(f'line: {line}')
        data = line.encode("utf-8")
        future = publisher.publish(topic_path, data)
        print(future.result())