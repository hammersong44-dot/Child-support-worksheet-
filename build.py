#!/usr/bin/env python3
"""Builds the single-file app: puts the 9:315.19 schedule (src/schedule_2025.json)
into src/template.html and writes the finished .html next to this script.
Run: python3 build.py"""
import json, os
here = os.path.dirname(os.path.abspath(__file__))
sched = json.load(open(os.path.join(here, "src", "schedule_2025.json")))
html = open(os.path.join(here, "src", "template.html")).read()
assert "/*SCHEDULE_JSON*/null" in html
html = html.replace("/*SCHEDULE_JSON*/null", json.dumps(sched, separators=(",", ":")))
out = os.path.join(here, "26-10_App_ChildSupportWorksheet_v1.html")
open(out, "w").write(html)
print("wrote", out, len(html), "bytes")
