#!/usr/bin/env python

import subprocess
from jenkins_setup import common

def run(source_path, result_path):
    print "===== Performing sloccount ====="

    try: 
        out, err = common.call("sloccount --duplicates --wide --details " + str(source_path), verbose=False)
        common.call("touch " + result_path + "/sloccount.sc")
        f = open(result_path + "/sloccount.sc", 'w')
        f.write(out)
    except:
        print "Error in sloccount. Skipping test, no results generated."

    print "===== Completed sloccount ====="

if __name__ == "__main__":
    run("/tmp/src","/tmp/result")
