#!/bin/bash
cd $SNAP
$SNAP/bin/uvicorn app.main:app --host 0.0.0.0 --port 4040
