import bpy
import os
import inspect
import sys

from io_xplane2blender.tests import *
from io_xplane2blender import xplane_config

__dirname__ = os.path.dirname(__file__)

def filterLines(line):
    return isinstance(line[0],str) and\
            ("ANIM" in line[0] or\
             "ATTR_manip" in line[0])

class TestRotationBoneRules(XPlaneTestCase):
    def test_1_only_rotated_around_one_axis(self):
        out = self.exportLayer(0)
        self.assertLoggerErrors(1)

    def test_2_rot_keyframes_must_be_sorted(self):
        out = self.exportLayer(1)
        self.assertLoggerErrors(1)

    def test_3_must_be_driven_by_only_1_dataref(self):
        out = self.exportLayer(2)
        self.assertLoggerErrors(1)

    def test_4_no_animimation_not_allowed(self):
        out = self.exportLayer(3)
        self.assertLoggerErrors(1)

    def test_5_counter_clockwise_also_allowed(self):
        filename = inspect.stack()[0][3]
        self.assertLayerExportEqualsFixture(
            4, os.path.join(__dirname__, 'fixtures', filename + '.obj'),
            filename,
            filterLines
        )

    def test_6_known_good_rotation_bone(self):
        filename = inspect.stack()[0][3]
        self.assertLayerExportEqualsFixture(
            5, os.path.join(__dirname__, 'fixtures', filename + '.obj'),
            filename,
            filterLines
        )

runTestCases([TestRotationBoneRules])
