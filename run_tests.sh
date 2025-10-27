#!/bin/bash
timestamp=$(date +"%Y-%m-%d_%H-%M-%S")
report="src/reports/report_$timestamp.html"
mkdir -p src/reports
pytest -v --html="$report" --self-contained-html
open "$report" 2>/dev/null || xdg-open "$report" 2>/dev/null
