
class StateMachine:
    def __init__(self) :
        self.state_names = {
            0: "phone weg",
            1: "phone gelegt",
            2: "phone da",
            3: "phone genommen",
        }

        self.current_state = 0

        self.state_transitions = {
            0: {
                "HG" : 2,
                "HR" : 0,
                "LG" : 1,
                "LR" : 0
            },
            1: {
                "HG" : 2,
                "HR" : 0,
                "LG" : 1,
                "LR" : 0
            },
            2: {
                "HG" : 2,
                "HR" : 0,
                "LG" : 3,
                "LR" : 0
            },
            3: {
                "HG" : 2,
                "HR" : 0,
                "LG" : 3,
                "LR" : 0
            }
        }
    
    def transition(self, signal) :
        self.current_state = self.state_transitions[self.current_state][signal]

    def get_current_state(self):
        return self.state_names[self.current_state]
    
    