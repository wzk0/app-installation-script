import yaml

config=yaml.load(open('config.yaml'),Loader=yaml.FullLoader)
pac=config['main']['pac']
su=config['main']['su']
ok=config['main']['ok']
src=config['main']['src']