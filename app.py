import digitalocean
from datetime import date
today = date.today()
manager = digitalocean.Manager(token='69e27519546dadffd51a5bc2811d06db108d894cfba0ccb65a519b8979af7fd0')
my_droplets = manager.get_all_droplets()
for droplet in my_droplets:
    if droplet.status == 'active':
        droplet.take_snapshot('{1} {0:%Y%m%d}'.format(today, droplet.name), power_off=True)
