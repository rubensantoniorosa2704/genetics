#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod

class QueenStrategy(ABC):
    @abstractmethod
    def solve(self, board):
        pass
