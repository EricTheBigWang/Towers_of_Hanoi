# from __future__ import annotations
import pygame
import settings


class Disk:
    """A disk a peg contains.

    === Attributes ===
    peg: the peg the disk belongs to.
    length: the length of the disk
    height: the height of the disk
    """
    # Attribute types
    peg: 'Peg'
    length: int
    height: int

    def __init__(self, peg: 'Peg', length: int) -> None:
        """Create a new disk.
        """
        self.peg = peg
        self.length = 32 + length * 20
        self.height = 20

    def draw(self) -> None:
        """Draw the disk on the screen.
        """
        index = self.peg.disks.index(self)
        disks = self.peg.number_of_disks
        shape = self.peg.rectangle

        disk = (
            shape[0] + (shape[2] - self.length) / 2,
            shape[1] + shape[3] + (self.height + 1) * (index - disks) + 1,
            self.length,
            self.height
        )

        pygame.draw.rect(settings.get_screen(), (80, 80, 80), disk, 0)

    def set_peg(self, peg: 'Peg') -> None:
        """Change the peg the disk belongs to.
        """
        self.peg = peg
