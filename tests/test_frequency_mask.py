import unittest

import numpy as np

from audiomentations.augmentations.transforms import FrequencyMask
from audiomentations.core.composition import Compose


class TestFrequencyMask(unittest.TestCase):
    def test_apply_frequency_mask(self):
        sample_len = 1024
        samples_in = np.random.normal(0, 1, size=sample_len).astype(np.float32)
        sample_rate = 16000
        augmenter = Compose(
            [FrequencyMask(min_frequency_band=0.3, max_frequency_band=0.5, p=1.0)]
        )

        samples_out = augmenter(samples=samples_in, sample_rate=sample_rate)
        self.assertEqual(samples_out.dtype, np.float32)
        self.assertEqual(len(samples_out), sample_len)

        std_in = np.mean(np.abs(samples_in))
        std_out = np.mean(np.abs(samples_out))
        self.assertLess(std_out, std_in)
