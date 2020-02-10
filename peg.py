# from __future__ import annotations
from typing import Any, List, Optional, Tuple
import pygame
import settings
from disk import Disk


class Peg:
    """A peg that holds disks.

    === Attributes ===
    rectangle: The location and dimensions of the peg.
    number_of_disks: The number of disks the peg contains.
    disks: The disks the peg contains.
    """
    # Attribute types
    rectangle: Tuple[int, int, int, int]
    number_of_disks: int
    disks: List[Optional['Disk']]

    def __init__(self, x: int, y: int, length: int, height: int) -> None:
        """Create a new peg.
        """
        self.rectangle = (x, y, length, height)
        self.number_of_disks = 0
        self.disks = []

    def draw(self) -> None:
        """Draw the peg on the screen, along with the disks it contains.
        """
        pygame.draw.rect(
            settings.get_screen(), (150, 150, 150), self.rectangle, 0)

        for i in range(len(self.disks)):
            self.disks[i].draw()

    def set_disks(self, n: int) -> None:
        """Set n disks onto the peg starting from 
        size n + 1 at the bottom of the peg, and ending 
        with a disk of size 1 at the top of the peg.

        Precondition: self.disks == []
        """
        for i in range(n):
            self.disks.append(Disk(self, i + 1))
        self.number_of_disks = n

    # TODO
    def __len__(self) -> int:
        """Return the number of disks the peg contains.
        """
        pass

    # TODO
    def is_empty(self) -> bool:
        """Return False iff the peg contains disks.
        """
        pass

    # TODO
    def place_disk(self, disk: 'Disk') -> None:
        """Place a disk onto the peg.
        """
        pass

    # TODO
    def remove_disk(self) -> 'Disk':
        """Remove the top disk from the peg iff the peg contains no disks.
        """
        pass

    # TODO
    def transfer_disk(self, other: 'Peg') -> None:
        """Transfer the top disk of self, to the top of the other peg.
        """
        pass