# Child Support Worksheet App

One HTML file that prepares a Louisiana child support guideline worksheet (A or B) and prints it on legal paper.

## Open it
Double-click `26-10_App_ChildSupportWorksheet_v2.html`. It works offline and saves nothing: close the tab and the case data is gone.

## Use it
1. Pick Worksheet A (one domiciliary parent, the default) or B (shared custody).
2. Fill in the case, children, custody, income, add-ons and direct payments. The worksheet on the right updates as you type.
3. Click Print worksheet. In the print dialog choose Save as PDF, paper size Legal, margins None, headers and footers off.

## What it covers
La. R.S. 9:315 et seq.: the 9:315.19 schedule (embedded, Acts 2024 No. 86, eff. 1/1/2025), 9:315.20 lines, 9:315.9(A)(7) cap warning on B, 9:315.8(E) day-count reference on A. Out of the schedule range (under $1,050 or over $50,000 combined, more than 6 children) it stops and says why instead of guessing.
Not covered: split custody (run A once per parent), imputed income, deviation. Those are the lawyer's calls.

## Files
- `src/template.html`: the app (comments mark each statute).
- `src/schedule_2025.json`: the schedule as data. A change in the law is an edit here.
- `build.py`: puts the schedule into the template and writes the finished .html (`python3 build.py`).
- Math matches the `child-support-worksheet` skill's `calc.py`; the Self-test panel checks known answers.

Verify against current law before relying on it. Schedule last verified 2026-10-15.

## Branding (v2, 2026-10-24)
Matches the Plea Form Builder: navy header with the office name first and "Attorney at Law" beneath, tool name on the right, brass rule, parchment page, a footer with the PO Box, phone and website, and a dark mode for the screen controls. The worksheet sheet itself (white, Times New Roman, legal paper) and the print output did not change. v1 is kept as `26-10_App_ChildSupportWorksheet_v1.html`; backups of the template and README are in `backups/`.
