Battery Lab 3D — Repair Kit
============================

Files:
- apply_fixes.py: applies carefully checked edits to your existing index.html.
- privacy.html: new privacy-policy page for the website.

IMPORTANT
1. Download/clone your existing GitHub repository to your computer.
2. Put apply_fixes.py in the same folder as the existing index.html.
3. Run: python3 apply_fixes.py
4. The script creates index.html.backup and updates index.html. If an expected
   source block does not match, it stops without changing index.html.
5. Copy privacy.html into the repository root.
6. Upload/commit the updated index.html and new privacy.html to GitHub.

Do not upload index.html.backup. Keep it locally as a backup.

After deployment, check:
- https://battery.batterylab.workers.dev/
- https://battery.batterylab.workers.dev/privacy.html

Scope:
These are targeted repairs based on the current main/index.html source that was
read during this session. They are not a complete browser-based QA pass. In
particular, the 3D drag interactions, all calculator edge cases, mobile devices,
and AdSense approval still require separate testing.
