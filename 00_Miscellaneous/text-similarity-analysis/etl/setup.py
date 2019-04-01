#!/usr/bin/python
#
# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import absolute_import
from __future__ import print_function

import setuptools

REQUIRED_PACKAGES = [
    'tensorflow==1.7.0',
    'tensorflow-hub==0.1.0',
    'tensorflow-transform==0.6.0',
    'bs4==0.0.1',
    'nltk==3.3']

setuptools.setup(
    name='etl_pipeline',
    version='0.0.1',
    author='anonymous',
    author_email='anonymous@google.com',
    install_requires=REQUIRED_PACKAGES,
    packages=setuptools.find_packages())