# Copyright 2020 The SQLFlow Authors. All rights reserved.
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
""" This module provides two APIs to compress and decompress a
directory.
"""
import tarfile


def zip_dir(src_dir, tarball):
    """compress a directory into tarball
    Args:
        src_dir: string
        the source directory to compress.

        tarball: string
        the output tarball name.
    """
    with tarfile.open(tarball, "w:gz") as tar:
        tar.add(src_dir, recursive=True)


def unzip_dir(tarball, dest_dir="./"):
    """decompress a tarball to a directory.
    Args:
        tarball: string
        the tarball to decompress.

        dest_dir: string
        the output path.
    """
    with tarfile.open(tarball, 'r:gz') as tar:
        tar.extractall(path=dest_dir)
