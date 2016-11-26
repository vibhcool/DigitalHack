# api token 
api_token="beb074d0c9a88caac568a705e75d600e0e0c49cebea2e774e79ea42068a9191b"


import digitalocean


class my_server(object):

	#3 server create
	def server_create(self,s_name,s_image='ubuntu-14-04-x64',s_size_slug='512mb',s_region='nyc2'):
		self.droplet = digitalocean.Droplet(token=api_token,
		                           name=s_s_name,
		                           region=s_region, # New York 2
		                           image=s_image, # Ubuntu 14.04 x64
		                           size_slug=s_size_slug,  # 512MB
		                           backups=True)
		self.droplet.create()

	#all server close
	def server_all_close(self,):
		manager = digitalocean.Manager(token=api_token)
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
		droplet.power_on()

	def server_snap(self,d_name):
		self.droplet.take_droplet(d_name)		


