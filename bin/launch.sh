#!/bin/bash
cd $SNAP
$SNAP/bin/uvicorn app.main:app --port 5000
