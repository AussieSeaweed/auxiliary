from unittest import TestCase


class FloatTestCase(TestCase):
    def assertSequenceAlmostEqual(self, seq1, seq2):
        self.assertEqual(len(seq1), len(seq2))

        for v1, v2 in zip(seq1, seq2):
            self.assertAlmostEqual(v1, v2)
