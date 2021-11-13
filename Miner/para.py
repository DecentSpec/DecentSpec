class Para:
    def __init__(self, preproc, train, alpha, difficulty, seeder, seed_name, init_weight, nn_structure, sample_para):
        
        # ML related
        self.alpha = alpha                  # EWMA coefficient 
        self.preproc = preproc
        self.train = train
        self.init_weight = init_weight
        self.nn_structure = nn_structure
        self.sample_para = sample_para
        
        # BC related
        self.difficulty = difficulty
        self.seeder = seeder
        self.seed_name = seed_name
    
    def get_para_dict(self):
        return self.__dict__
