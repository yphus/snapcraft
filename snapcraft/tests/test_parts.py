# -*- Mode:Python; indent-tabs-mode:nil; tab-width:4 -*-
#
# Copyright (C) 2015-2016 Canonical Ltd
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 3 as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import unittest
import unittest.mock


import snapcraft
from snapcraft.internal import dirs
from snapcraft.internal import project_loader
from snapcraft import tests


class TestParts(tests.TestCase):

    def setUp(self):
        super().setUp()
        dirs.setup_dirs()

        patcher = unittest.mock.patch(
            'snapcraft.internal.project_loader._get_snapcraft_yaml')
        self.mock_get_yaml = patcher.start()
        self.mock_get_yaml.return_value = 'snapcraft.yaml'
        self.addCleanup(patcher.stop)
        self.part_schema = project_loader.Validator().part_schema
        self.deb_arch = snapcraft.ProjectOptions().deb_arch

    @unittest.mock.patch('snapcraft.internal.parts.PartsConfig.load_plugin')
    def test_get_parts_none(self, mock_loadPlugin):
        self.make_snapcraft_yaml("""name: test
version: "1"
summary: test
description: test
confinement: strict

parts:
  part1:
    plugin: go
    stage-packages: [fswebcam]
""")
        config = project_loader.load_config(None)
        self.assertEqual(None, config.parts.get_part('not-a-part'))
