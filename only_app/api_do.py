import digitalocean


class my_server(object):

    # api token 
    api_token="beb074d0c9a88caac568a705e75d600e0e0c49cebea2e774e79ea42068a9191b"

    ss=['ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDn8hGrTD8j3C69n1WC96cl6n8oGV1psYXzh4jZLFd9oDikhlp/bT8BzFdJ5aNdo3iYmG4LggaOZviez+oeabLBNrk4v+FvSDdZvNbjA6GbQUV6LZB2HWhyAgcN2chpNVdcqiWJZS5cdVX1u+QMVcejboEyEzkoEAv1XjUQoOttgUqKyiTNOfzhZtIkcygZVQY+r9HI03HuUoAFXlToYstt0X5banr4dd7LlJlvSPz99aHWgjWz39mAEOOIZKBEaqevE0OXil30FEL652xzXEM5WtBmqVBPY67d1PlWMf5xxB5Cp1+GtX6gFaX/TDyaOK/2wwUFj70hNcVAdIxF+VLR vibhcool@localhost.localdomain']        

    #3 server create
    def server_create(self,s_name,s_image='ubuntu-14-04-x64',s_size_slug='512mb',s_region='nyc2'):
        self.droplet = digitalocean.Droplet(token=self.api_token,
                                   name=s_name,
                                   region=s_region, # New York 2
                                   image=s_image, # Ubuntu 14.04 x64
                                   size_slug=s_size_slug,ssh_keys=self.ss,  # 512MB
                                   backups=True)
        self.droplet.create()

    #all server close
    def server_all_close(self,):
        manager = digitalocean.Manager(token=self.api_token)
        my_droplets = manager.get_all_droplets()
        for droplet in my_droplets:
            droplet.shutdown()

    #7 server close
    def server_close(self,):
        self.droplet.shutdown()


    #check status server
    def server_status(self,):
        actions = droplet.get_actions()
        for action in actions:
            action.load()
        # Once it shows complete, droplet is up and running
        print(action.status)

    #5 server_on
    def server_on(self,):
        self.droplet.power_on()

    def server_snap(self,d_name):
        self.droplet.take_droplet(d_name)		

    def server_destroy(self,):
        self.droplet.destroy()

    def server_restore(self,):
        print(self.droplet.get_snapshots())

