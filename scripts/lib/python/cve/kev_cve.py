#
# EMLinux CVE checker.
# Download and store KEV data
#
# Copyright (c) Cybertrust Japan Co., Ltd.
#
# SPDX-License-Identifier: MIT
#

import urllib.request
import gzip
import json
import os.path
import time
import logging

logger = logging.getLogger("emlinux-cve-check")
KEV_JSON_URL = "https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json"

def fetch_json_data():
    request = urllib.request.Request(KEV_JSON_URL)
    for attempt in range(5):
        try:
            r = urllib.request.urlopen(request)

            if (r.headers['content-encoding'] == 'gzip'):
                buf = r.read()
                raw_data = gzip.decompress(buf)
            else:
                raw_data = r.read().decode("utf-8")

            r.close()
        except Exception as e:
            logger.debug(f"json file: received error ({e}), retrying")
            time.sleep(6)
            pass
        else:
            return json.loads(raw_data)
    else:
        # We failed at all attempts
        return None

def should_skip_fetch_json_file(json_file):
    if json_file:
        if os.path.exists(json_file):
            if time.time() - os.path.getmtime(json_file) < 86400:
                logger.info(f"Last database update is in 1day so skip Debian CVE database update")
                return True

    return False

def fetch_kev_data(dl_dir):
    logger.info("Update KEV database")
    kev_json = f"{dl_dir}/known_exploited_vulnerabilities.json"
    if should_skip_fetch_json_file(kev_json):
        return kev_json

    data = fetch_json_data()
    if data is None:
        return None

    with open(kev_json, "w") as f:
        json.dump(data, f)

    return kev_json

