import time
import json
from atproto import Client

def load_post_data_from_json(file_path):
    with open(file_path, 'r') as json_file:
        post_data_list = json.load(json_file)
    return post_data_list

def main():

    client = Client()
    client.login('handle', 'password')

    post_data_list = load_post_data_from_json('data.json')
    counter = 0

    while True:
        post_data = post_data_list[counter]
        with open(post_data['image_path'], 'rb') as f:
            img_data = f.read()

        client.send_image(
            text=post_data['text'],
            image=img_data,
            image_alt=post_data['image_alt']
        )
        
        counter += 1
        print(counter, ". Post Sent.")
        
        if counter >= len(post_data_list):
            break
            
        #You can change time.sleep to determine how long it will post. 43200sec = 12hours
        time.sleep(43200)
        

if __name__ == '__main__':
    main()