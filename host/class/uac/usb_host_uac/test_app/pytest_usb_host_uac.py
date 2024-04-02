# SPDX-FileCopyrightText: 2024 Espressif Systems (Shanghai) CO LTD
# SPDX-License-Identifier: Apache-2.0

from typing import Tuple

import pytest
from pytest_embedded_idf.dut import IdfDut


@pytest.mark.esp32s2
@pytest.mark.esp32s3
@pytest.mark.usb_host
def test_usb_host_uac(dut: Dut) -> None:
    dut.expect_exact('Press ENTER to see the list of tests.')
    dut.write('[uac_host]')
    dut.expect_unity_test_output(timeout = 3000)