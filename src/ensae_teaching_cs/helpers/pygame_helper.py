"""
@file
@brief pygame helpers

The module pygame is not imported in this module but sent
to every function as a parameter to avoid importing
the module if not needed.
"""

MOUSE = "mouse"
KEY = "key"


def wait_event(pygame):
    """
    The function waits for an event, a

    @param      pygame      module pygame
    """
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                return (MOUSE, event.button, event.pos[0], event.pos[1])
            elif event.type == pygame.KEYUP:
                if event.key == 27:
                    return None
                else:
                    return (KEY, event.key)
            elif event.type == pygame.QUIT:
                return None


def empty_main_loop(pygame):
    """
    remove all events in the main loop,
    a mouse click make the program halt,
    another click makes it start again

    @param      pygame      module pygame
    @return                 event ``pygame.QUIT``?
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        if event.type == pygame.MOUSEBUTTONUP:
            wait_event(pygame)
    return True
