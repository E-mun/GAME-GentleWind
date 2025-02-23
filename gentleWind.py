print('-------------------')
print('-- A Gentle Wind --')
print('------ an EMUN game')
print('-------------------')
print('\n\n')

import math
import random
from os import system
import time



class AREA():
    def __init__(self, exit = bool, desc = str, x = int, y = int):
        self.exit = exit
        self.description = desc
        self.pathLinks = []
        self.pathDescs = []
        self.x = x
        self.y = y




                
# Main Menu Initialization
def printMenu():
    frame_line = ''
    for i in range(24):
        frame_line += '-'
    print(frame_line)
    for line in range(4):
        frame_line = '|'
        for i in range(22):
            frame_line += ' '
        frame_line += '|'
        print(frame_line)
    
    frame_line = '|      MAIN MENU       |'
    print(frame_line)

    for line in range(4):
        frame_line = '|'
        for i in range(22):
            frame_line += ' '
        frame_line += '|'
        print(frame_line)
    
    frame_line = '|      TYPE START      |'
    print(frame_line)

    for line in range(4):
        frame_line = '|'
        for i in range(22):
            frame_line += ' '
        frame_line += '|'
        print(frame_line)
    frame_line = ''
    for i in range(24):
        frame_line += '-'
    print(frame_line)

# MAIN GAME LOOP
GAME_RUNNING = True   
IN_GAME = False 
while GAME_RUNNING:

    

    areas = [
    # first is the exit area
    'a grassy clearing with an old, blue mountain bike. A clear trail leads out of the forest.',
    
    # other blank areas
    'a silent meadow with deep green and grey moss covering the forest floor. Pine trees block sound and sun.',
    'a grove of bright yellow aspen trees in every direction.',
    'a gentle creek running over thick red mud. Occasional chirping of birds can be heard overhead.',
    'a windy field with towering wheat blocking lines of sight.',
    'a constellation of large, dark rocks breaking though the forest floor. The rocks can be climbed but offer no great visibility.',
    
    # 6-10
    'a long-dead campfire surrounded by small rocks, sitting in a small clearing of an oak-dense portion of forest.',
    'a series of fallen pine trees. They create small openings in the otherwise dense canopy.',
    'a rolling section of forest hills covered in green ferns.',
    'a random scattering of old junk made of plywood, rusted garden equipment and hardware. No other signs of activity are present in the surrounding dense forest.',
    'a single large, rounded grey rock sitting unassumingly in the forest floor.',

    # 11-15
    'a long abandoned deer stand sitting at the base of a large poplar tree. The forest has a few longer lines of sight, but is also obscured by dense brush in most directions.',
    'a thick, small patch of bamboo - oddly situated in the deciduous forest. You hear occassional rustling from within.',
    'a old, crumbling pair of stone benches, facing away from each other. No other signs of human activity are anywhere nearby.',
    'a gargantuan and ancient oak tree, with the letter "B" carved and scarred over its base.',
    'a damp but empty creekbed. Deer tracks clutter the banks, but no sounds can be heard nearby.',
    ]
    # Initialize 4x4 grid
    grid = [
    ['','','',''],
    ['','','',''],
    ['','','',''],
    ['','','',''],
    ]

    exit_area_assigned = False

        # populate grid with areas
    for x in range(4):
        for y in range(4):

            #generate a random index to pop from the areas list
            rand_index = random.randint(0, len(areas)-1)
            area_description = areas.pop(rand_index)

            # This marks the exit area the first time the index chosen is 0
            if rand_index == 0 and exit_area_assigned == False:
                area_exit = True
                exit_area_assigned = True
                exit_area_coords = [x,y]
            else:
                area_exit = False

            grid[x][y] = AREA(area_exit, area_description, x, y)

    paths = [
        # 1-5
        'A thin trail marked with blue trail markers leads away from the area.',
        'A wider, winding trail is marked with intermittent white trail markers leads into the woods.',
        'A narrow trail marked with faded red trail markers leads deeper into the woods.',
        'A broad, sloping trail marked with yellow striped markers leads away from the area.',
        'A twisting trail marked with black trail markers leads into the forest.',

        # 6-10
        'A stone archway marks the entrance to an otherwise unmarked path.',
        'A holly bush partially obscures the beginning of a small footpath.',
        'A towering wall of earth yields to a narrow crevice of a path.',
        'A subtle deer trail leads back into the woods',
        'What remains of a rusted bike frame lies at the entrance of a sloped mud path.',

        # 11 - 15
        'An unmarked trail leads into the woods.',
        'An unmarked trail leads into the woods.',
        'An unmarked trail leads into the woods.',
        'An unmarked trail leads into the woods.',
        'An unmarked trail leads into the woods.',

        # 16 - 20
        'An unmarked trail leads into the woods.',
        'An unmarked trail leads into the woods.',
        'An unmarked trail leads into the woods.',
        'An unmarked trail leads into the woods.',
        'An unmarked trail leads into the woods.',

    ]

    # Assign paths between areas
    # Will assign 1 path starting from each area to a random new area that isn't already connected to it

    for x in range(4):
        for y in range(4):
            currentArea = grid[x][y]
            lookingForLink = True
            if len(currentArea.pathLinks) < 3:
                while lookingForLink:
                    randX = random.randint(0,3)
                    randY = random.randint(0,3)

                    #ensure the link isn't a self reference
                    if randX != x and randY != y:

                        #check the link doesn't already exist and dest isn't full
                        checkArea = grid[randX][randY]
                        if ([x,y] not in checkArea.pathLinks) and (len(checkArea.pathLinks) < 3):

                            # pick the path description
                            rand_index = random.randint(0, len(paths)-1)
                            pathDesc = paths.pop(rand_index)

                            # assign the location and desc to the currentArea
                            currentArea.pathLinks.append([randX, randY])
                            currentArea.pathDescs.append(pathDesc)

                            # assign the recip. location and desc to the target Area
                            checkArea.pathLinks.append([x, y])
                            checkArea.pathDescs.append(pathDesc)

                            lookingForLink = False

    # Minimum of 1 connection should now be present for every area

    printMenu()
    action = input('>> ')
    if action.lower() == 'start':

        system('clear')
        print('LOADING.')
        time.sleep(1)

        system('clear')
        print('LOADING..')
        time.sleep(1)

        system('clear')
        print('LOADING...')
        time.sleep(1)
        system('clear')
        
        # Determine Start Area
        if exit_area_coords[0] < 2:
            if exit_area_coords[1] < 2:
                # Q1 Exit
                start_coords = [3,3]
            else:
                # Q2 Exit
                start_coords = [3,0]
        else:
            if exit_area_coords[1] < 2:
                start_coords = [0,3]
            else:
                start_coords = [0,0]

        # IN GAME LOOP
        current_area = grid[start_coords[0]][start_coords[1]]
        DEBUG_NEXT_DESTINATION = [start_coords[0],start_coords[1]]
        IN_GAME = True
        turn_count = 0
        while IN_GAME:
            DEBUG_ISOLATED = []
            DEBUG_1 = []
            DEBUG_2 = []
            DEBUG_3 = []
            DEBUG_4 = []

            for i in range(4):
                for j in range(4):
                    area = grid[i][j]
                    if len(area.pathLinks) < 1:
                        DEBUG_ISOLATED.append([area.x, area.y])
                    elif len(area.pathLinks) == 1:
                        DEBUG_1.append([area.x, area.y])
                    elif len(area.pathLinks) == 2:
                        DEBUG_2.append([area.x, area.y])
                    elif len(area.pathLinks) == 3:
                        DEBUG_3.append([area.x, area.y])
                    else:
                        DEBUG_4.append([area.x, area.y])

            turn_count += 1
            # Gentle Wind Check / Path Shifting
            if turn_count % 4 == 0:
                print('A gentle wind rushes through the forest along your path.')

                # PATH ADD
                lookingForLink = True
                while lookingForLink:
                    

                    # looking to add a path between 2 areas

                    for x in range(4):
                        for y in range(4):
                            area = grid[x][y]

                            # start from an area with only 1 link
                            if len(area.pathLinks) < 2:
                                # pick a random area for the destination
                                randX = random.randint(0,3)
                                randY = random.randint(0,3)
                                checkArea = grid[randX][randY]

                                # check if that index is not already a link to this area && not self-reference
                                if checkArea != area and [randX, randY] not in area.pathLinks:

                                    # pull description of path from front of path list
                                    new_path_description = paths.pop(0)

                                    # add the link + description to starting area
                                    area.pathDescs.append(new_path_description)
                                    area.pathLinks.append([randX, randY])

                                    # add link + description to destination area
                                    checkArea.pathDescs.append(new_path_description)
                                    checkArea.pathLinks.append([x,y])

                                    lookingForLink = False
                                    break
                        if lookingForLink == False:
                            break
                
                # SUBTRACT PATH
                lookingForErase = True

                # Looking to subtract a path from 2 areas that each have more than 1 path
                while lookingForErase:
                        x = random.randint(0,3)
                        y = random.randint(0,3)
                        area = grid[x][y]

                        # front area has more than 1 path
                        if len(area.pathLinks) > 1:

                            # check all of area's path destinations for viable erasures
                            for i in range(len(area.pathLinks)):
                                if len(grid[area.pathLinks[i][0]][area.pathLinks[i][1]].pathLinks) > 1: # << The number of paths connecting to the destination of this path 'i'
                                    
                                    dest_area = grid[area.pathLinks[i][0]][area.pathLinks[i][1]]
                                    
                                    # valid erasure found
                                    lookingForErase = False

                                    # pop path description to back of paths list
                                    path_removed = area.pathDescs.pop(i)
                                    paths.append(path_removed)
                                    

                                    # remove destination path
                                    path_index_to_erase = dest_area.pathDescs.index(path_removed)
                                    dest_area.pathLinks.pop(path_index_to_erase)
                                    dest_area.pathDescs.pop(path_index_to_erase)

                                    # remove path link from initial area
                                    area.pathLinks.pop(i)

                                    break

            # Print the Current Area Description
            area_intro = 'You come to '+current_area.description
            print(area_intro)

            # Check for Win Condition to exit In Game Loop
            if current_area.exit:
                print('')
                print('You take the bike and ride out of the forest and towards the familiar highway. You made it.')
                time.sleep(1.2)
                print('THE END')
                time.sleep(3)

                IN_GAME = False
                break
            
            # Print the Map of the Area with different paths
            print('')
            sp8 = '        '
            top9 = '--- A ---'
            side9 = '|       |'
            sideBgap = '        |'
            sideBCgap = '         '
            sideB = 'B       |'
            sideBC = 'B       C'
            bot9 = '---------'

            top = sp8+top9+sp8

            # Top Frame
            print(top)
            for i in range(2):
                print(sp8+side9+sp8)
            
            if len(current_area.pathLinks) == 3:
                print(sp8+sideBCgap+sp8)
                print(sp8+sideBC+sp8)
                print(sp8+sideBCgap+sp8)
                path_choices = ['A. '+current_area.pathDescs[0], 'B. '+current_area.pathDescs[1], 'C. '+current_area.pathDescs[2]]

            elif len(current_area.pathLinks) == 2:
                print(sp8 + sideBgap + sp8)
                print(sp8 + sideB + sp8)
                print(sp8 + sideBgap + sp8)
                path_choices = ['A. '+current_area.pathDescs[0], 'B. '+current_area.pathDescs[1]]

            else:
                print(sp8 + side9 + sp8)
                print(sp8 + side9 + sp8)
                print(sp8 + side9 + sp8)
                path_choices = ['A. '+current_area.pathDescs[0]]

            for i in range(2):
                print(sp8+side9+sp8)
            
            print(sp8+bot9+sp8)

            print()
            for p in path_choices:
                print(p)
            
            # Take Player Input
            action = input(">> ")
            action = action[0].lower()

            if action == 'a':
                DEBUG_LAST_DESTINATION = DEBUG_NEXT_DESTINATION
                DEBUG_NEXT_DESTINATION = [current_area.pathLinks[0][0],current_area.pathLinks[0][1]]
                current_area = grid[current_area.pathLinks[0][0]][current_area.pathLinks[0][1]]
                
                system('clear')
            elif action == 'b' and len(current_area.pathLinks) >= 2:
                DEBUG_LAST_DESTINATION = DEBUG_NEXT_DESTINATION
                DEBUG_NEXT_DESTINATION = [current_area.pathLinks[1][0],current_area.pathLinks[1][1]]
                current_area = grid[current_area.pathLinks[1][0]][current_area.pathLinks[1][1]]
                
                system('clear')
            elif action == 'c' and len(current_area.pathLinks) >= 3:
                DEBUG_LAST_DESTINATION = DEBUG_NEXT_DESTINATION
                DEBUG_NEXT_DESTINATION = [current_area.pathLinks[2][0],current_area.pathLinks[2][1]]
                current_area = grid[current_area.pathLinks[2][0]][current_area.pathLinks[2][1]]
                
                system('clear')
            else:
                print('Input unrecognized - please enter a valid path.')
                time.sleep(1)
            
    
    else:
        print('Type START to begin the game.\n')
    
    action = ''

    