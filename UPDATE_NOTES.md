# Battery Lab 3D — Update Notes

## Implemented
- Visual refresh: subtle cyan/mint ambient background, compact control spacing,
  focus-visible states, button feedback, and section entrance transitions.
- Undo: toolbar button and Ctrl+Z. The in-memory history retains up to 40
  checkpoints and covers battery pack state, battery wires, calculator settings,
  lab components/wires, multimeter mode, tool selection, and probe positions.
- Multi-project support: named local projects remain supported; save/load now
  persists the full calculator and laboratory state. Project list remains
  limited to 20 entries in localStorage.
- Loading projects recalculates the next lab component ID.

## Validation
- Extracted JavaScript module passed `node --check`.
- No claim of complete interactive/browser testing is made. Verify actual
  pointer/drag behavior, 3D rendering, calculator outputs, and responsive
  behavior on the deployed site.

## Storage behavior
- Saved projects use browser localStorage and are local to that browser.
- Undo history is session-only and is cleared on page reload.

## Advanced Engineering Suite addition
- Added `advanced.html`, linked from the main workspace sidebar.
- Includes simulated cell-voltage/temperature monitoring, illustrative discharge curve and CSV export, capacity-based SoH estimator, virtual oscilloscope, and electrical calculator.
- These are educational simulations only; no real BMS control, hardware measurement, or certified battery model is provided.
- Print buttons use the browser print dialog (choose Save as PDF).
- Validate in a browser after deployment; no claim of complete interactive browser QA is made.
