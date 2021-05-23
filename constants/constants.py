
# constants values representing fields in the game world
EMPTY_FIELD_VALUE = 0
OBSTACLE_VALUE = 1
AGENT_VALUE = 2
DESTINATION_VALUE = 3
PATH_VALUE = 4

OBSTACLE_CHAR = "#"
DESTINATION_CHAR = "$"
AGENT_CHAR = "A"
EMPTY_FIELD_CHAR = "."
PATH_CHAR = "X"

# constants values representing game world building
OBSTACLES_COUNT = 9
MIN_OBSTACLE_HEIGHT = 1
MIN_OBSTACLE_WIDTH = 1
MAX_OBSTACLE_SIZE = 4

# constants values representing agent parameters
EXPLORATION_RATE_INIT = 1
EXPLORATION_DECAY_RATE = 0.99
LEARNING_RATE = 0.7
DISCOUNT_RATE = 0.99
MAX_AGENT_MOVES_COUNT = 50

# constants values representing fields costs
EMPTY_FIELD_COST = -0.5
DESTINATION_FIELD_PRICE = 20
INIT_DECISION_RATING = 5

