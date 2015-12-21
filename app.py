import digitalocean
import os
from datetime import date
today = date.today()
do_token = os.environ['TOKEN']
manager = digitalocean.Manager(token=do_token)

def main():
    my_droplets = manager.get_all_droplets()
    for droplet in my_droplets:
        if droplet.status == 'active':
            droplet.take_snapshot('{1} {0:%Y%m%d}'.format(today, droplet.name), power_off=True)

if __name__ == "__main__":
    main()
