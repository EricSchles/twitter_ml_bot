import twint

config = twint.Config()
config.Username = "EricSchles"
config.Store_csv = True
twint.run.Search(config)
