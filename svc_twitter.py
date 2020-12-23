import twint  # configuration
config = twint.Config()
config.Search = "bitcoin"
config.Limit = 10  # running search
twint.run.Search(config)
