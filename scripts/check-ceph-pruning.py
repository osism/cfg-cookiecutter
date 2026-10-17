#!/usr/bin/env python3

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# With with_ceph=0 the post-gen hook prunes every Ceph file from the rendered
# repository. Fail if a file or directory whose path mentions ceph is left,
# so a new Ceph overlay cannot slip past the pruning list unnoticed.

import os
import sys


def main():
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <project-directory> <with_ceph>")
        sys.exit(1)

    project_dir, with_ceph = sys.argv[1], sys.argv[2]

    if with_ceph != "0":
        print(f"with_ceph={with_ceph}, nothing to check")
        return

    leftovers = []
    for root, dirs, files in os.walk(project_dir):
        dirs[:] = [d for d in dirs if d != ".git"]
        for name in dirs + files:
            path = os.path.relpath(os.path.join(root, name), project_dir)
            if "ceph" in path.lower():
                leftovers.append(path)

    if leftovers:
        print("ERROR: Ceph files left after pruning with with_ceph=0:")
        for path in sorted(leftovers):
            print(f"  {path}")
        sys.exit(1)

    print("No Ceph files left with with_ceph=0")


if __name__ == "__main__":
    main()
