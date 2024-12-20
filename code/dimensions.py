# Dimensions of all resources needed
NUM_CELLS_ROW       = 40 
NUM_CELLS_COL       = 30
CELL_WIDTH          = 20
CELL_HEIGHT         = 20
CELL_DIMS           = (CELL_WIDTH, CELL_HEIGHT)
CELLS_MARGIN        = 1 # margin between cells
MARGIN              = 15
NUM_COL_BUTTONS     = 2
BUTTON_WIDTH        = 120
BUTTON_HEIGHT       = 40
BUTTON_SIZE         = (BUTTON_WIDTH, BUTTON_HEIGHT)
LITTLE_BUTTON_SIZE  = (30, 40)
OPTION_BUTTON_SIZE  = (BUTTON_WIDTH, 30)

BUTTONS_POS_Y       = 50
BUTTONS_POS_X       = 5*MARGIN + NUM_CELLS_ROW*CELL_WIDTH
BUTTONS_SPACE       = 4*MARGIN + NUM_COL_BUTTONS*BUTTON_WIDTH + BUTTONS_POS_Y
INFO_BORDER         = 35 # margin up 15 and margin down 15
WIN_WIDTH           = NUM_CELLS_ROW * (CELL_WIDTH + CELLS_MARGIN) + 2*MARGIN + BUTTONS_SPACE
WIN_HEIGHT          = NUM_CELLS_COL * (CELL_HEIGHT + CELLS_MARGIN) + 2 *MARGIN + INFO_BORDER
WINDOW_DIMS         = (WIN_WIDTH, WIN_HEIGHT)
X_SECOND_COL        = BUTTONS_POS_X + BUTTON_WIDTH + BUTTONS_POS_Y
Y_SECOND_ROW        = 1.5*BUTTONS_POS_Y + BUTTON_HEIGHT
NEW_ROW             = 0.5*BUTTONS_POS_Y + BUTTON_HEIGHT
RESMESAGGE_POS_X    = WIN_WIDTH - 5*MARGIN - BUTTON_WIDTH - BUTTONS_POS_Y
RESMESSAGE_POS      = (RESMESAGGE_POS_X, WIN_HEIGHT-100)