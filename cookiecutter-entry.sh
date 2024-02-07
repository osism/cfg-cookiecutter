#!/bin/bash

if [ "$1" = "/bin/bash" ];then
  exec /bin/bash
fi

if [ -z "$TARGET_UID" ];then
   echo "ERROR: ENVIRONMENT VARIABLE TARGET_UID IS NOT PROVIDED"
   exit 1
fi
if [ -z "$TARGET_GID" ];then
   echo "ERROR: ENVIRONMENT VARIABLE TARGET_GID IS NOT PROVIDED"
   exit 1
fi

set -x
umask 0077
cookiecutter -o /output /data $@
chown -R $TARGET_UID:$TARGET_GID /output

set +x
echo "COOKIECUTTER COMPLETED"
