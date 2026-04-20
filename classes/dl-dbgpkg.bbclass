#
# This class gets debug symbol packages for SDK.
#
# Copyright (C) Cybertrust Japan Co., Ltd.
#
# SPDX-License-Identifier: MIT
#

#
# [How to use]
# Add following line into the local.conf.
# INHERIT += "dl-dbgpkg"
#
# If you want to get debian patched source tree, add following line too.
# PREPARE_PATCHED_SRC = "1"
#

require classes/dl-dbgpkg.inc
