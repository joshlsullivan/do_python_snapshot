import digitalocean
from datetime import date
today = date.today()
manager = digitalocean.Manager(token='')
my_droplets = manager.get_all_droplets()
for droplet in my_droplets:
    if droplet.status == 'active':
        droplet.take_snapshot('{1} {0:%Y%m%d}'.format(today, droplet.name), power_off=True)
