# -*- Mode:Python; indent-tabs-mode:nil; tab-width:4 -*-
#
# Copyright (C) 2016 Canonical Ltd
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

import os
import time

from testtools.matchers import (
    FileExists,
    Equals
)

import integration_tests


class YamlInSubdirTestCase(integration_tests.TestCase):

    def test_stage(self):
        project_dir = 'yaml-in-subdir'
        subdir = os.path.join(project_dir, 'subdir')
        self.run_snapcraft('stage', project_dir, subdir)

        expected_file = os.path.join(subdir, 'stage', 'file')
        self.assertThat(expected_file, FileExists())
        with open(expected_file) as f:
            self.assertThat(f.read(), Equals("I'm a file\n"))

        expected_file = os.path.join(subdir, 'stage', 'subdirfile')
        self.assertThat(expected_file, FileExists())
        with open(expected_file) as f:
            self.assertThat(f.read(), Equals("I'm in the subdir\n"))
