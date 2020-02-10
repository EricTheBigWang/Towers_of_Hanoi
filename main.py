if __name__ == '__main__':
    import pygame
    import settings
    from peg import Peg
    from disk import Disk

    pygame.init()

    # Create the pegs
    number_of_pegs = 3
    peg_height = 80
    peg_length = 24
    peg_spacing = (settings.length() - peg_length) / (number_of_pegs + 1)
    pegs = []
    for i in range(number_of_pegs):
        pegs.append(
            Peg(
                (i + 1) * peg_spacing,
                (settings.height() - peg_height) / 2,
                peg_length,
                peg_height)
        )

    # Add the disks to the first peg
    number_of_disks = 3
    pegs[0].set_disks(number_of_disks)

    # App loop
    last_peg = pegs[number_of_pegs - 1]
    while True:

        # Create background
        settings.get_screen().fill((255, 255, 255))

        # Draw the pegs on the screen
        for peg in pegs:
            peg.draw()

        # Refresh screen
        pygame.display.flip()

        # Handle user input
        move = [i for i in input("Input: ").split(' ')]

        # Check if the input is valid
        valid_input = True

        # Check if any characters entered are not digits or spaces.
        for i in range(len(move)):
            if move[i].isdigit():
                move[i] = int(move[i])
            else:
                valid_input = False
                print("Input should contain digits, and only digits.")
                break

        # Continue iff the input is valid
        if valid_input:
            # Continue iff there are only two integers in the list
            if len(move) == 2:
                # Transfer the pegs if all peg indexes are in bounds.
                if move[0] < number_of_pegs and move[1] < number_of_pegs:
                    starting_peg = pegs[int(move[0])]
                    ending_peg = pegs[int(move[1])]
                    starting_peg.transfer_disk(ending_peg)
                else:
                    print("An index of a peg does not exist")
            else:
                print("Enter two positive integers separated by a space.")

        # End condition for app loop
        if len(last_peg.disks) == number_of_disks:

            # Draw last frame of game
            settings.get_screen().fill((255, 255, 255))

            for peg in pegs:
                peg.draw()
            
            pygame.display.flip()
            break

    # The game is complete
    input("Your work here is done!")
    pygame.quit()