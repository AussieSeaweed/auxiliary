from collections import Sequence
from typing import Any
from unittest import TestCase


class ExtendedTestCase(TestCase):
    def assertSequenceAlmostEqual(self, seq1: Sequence[Any], seq2: Sequence[Any]) -> None:
        """Checks if elements in both sequences are almost equal.

        :param seq1: the first sequence
        :param seq2: the second sequence
        :return: None
        """
        self.assertEqual(len(seq1), len(seq2))

        for v1, v2 in zip(seq1, seq2):
            self.assertAlmostEqual(v1, v2)
