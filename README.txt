Battery Lab 3D — Updated Project
=================================

WHAT CHANGED
- Refreshed the interface with a cleaner dark theme, cyan/mint highlights,
  improved focus states, compact controls, and subtle section transitions.
- Added an Undo button in the top toolbar and Ctrl+Z keyboard shortcut.
- Undo history stores up to 40 workspace checkpoints in the current browser session.
- Expanded project saving/loading to retain calculator settings, lab tools,
  multimeter mode, probe positions, components, and wires.
- Loading a project recalculates the next lab component ID to avoid collisions.
- Existing project manager supports multiple named projects (up to 20 saved
  locally in this browser).

DEPLOY
1. Extract this ZIP.
2. Upload the contents of the Battery--main folder to the root of your GitHub
   repository, replacing the existing files when prompted.
3. Commit the changes and wait for Cloudflare Pages/Workers deployment.
4. Open https://battery.batterylab.workers.dev/ and test Undo and Projects.

IMPORTANT
- Projects are stored in the browser's localStorage; they do not synchronize
  between different browsers or devices.
- Undo history is temporary and is cleared when the page is reloaded.
- JavaScript module syntax was checked. This is not a full live-browser QA pass;
  test 3D dragging, breadboard interactions, calculations, and mobile layout
  after deployment.
- Keep a local copy of the previous repository as a backup.


Advanced Engineering Suite: open advanced.html from the main sidebar. It provides educational simulations and estimators; see UPDATE_NOTES.md for scope and limitations.
