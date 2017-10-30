#! /bin/bash
#
# Usage:  ./start.sh [port]
#  
# Start the service as a background process
#
#

pushd application
python3 botController.py -P ${1} &
pid=$! 
popd
echo "***"
echo "UI server started"
echo "PID ${pid} listening"
echo "***"