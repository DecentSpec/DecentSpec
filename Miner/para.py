class Para:
    def __init__(self, preproc, train, alpha, difficulty, seeder, seed_name, init_weight, nn_structure):
        
        # ML related
        self.alpha = alpha
        self.preproc = preproc
        self.train = train
        self.init_weight = init_weight
        self.nn_structure = nn_structure
        
        # BC related
        self.difficulty = difficulty
        self.seeder = seeder
        self.seed_name = seed_name
