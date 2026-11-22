#!/usr/bin/env python3
"""
Battery Lab 3D: safe, source-preserving patch helper.

Put this file beside the existing index.html, then run:
    python3 apply_fixes.py

It creates index.html.backup before editing. It refuses to edit if any
expected source block is missing or appears more than once.
"""
from pathlib import Path
import sys

target = Path("index.html")
if not target.exists():
    sys.exit("ERROR: index.html was not found. Put this script beside it.")

source = target.read_text(encoding="utf-8")
original = source

replacements = [
    (
        '<h1 class="font-bold text-sm sm:text-base tracking-tight text-white">BatteryLab <span class="text-cyan-400">3D</span></h1>',
        '<h1 class="font-bold text-sm sm:text-base tracking-tight text-white">Battery Lab <span class="text-cyan-400">3D</span></h1>',
        "Correct the visible product name"
    ),
    (
        "lab: { components: labState.components, wires: labState.wires }",
        "lab: { components: labState.components, wires: labState.wires, redProbe: labState.redProbe, blackProbe: labState.blackProbe, dmmMode: labState.dmmMode, tool: labState.tool }",
        "Persist multimeter probes and mode"
    ),
    (
        """              labState.components = JSON.parse(JSON.stringify(proj.lab.components || []));
              labState.wires = JSON.parse(JSON.stringify(proj.lab.wires || []));""",
        """              labState.components = JSON.parse(JSON.stringify(proj.lab.components || []));
              labState.wires = JSON.parse(JSON.stringify(proj.lab.wires || []));
              labState.redProbe = proj.lab.redProbe || { col: 2, row: 0 };
              labState.blackProbe = proj.lab.blackProbe || { col: 2, row: 1 };
              labState.dmmMode = proj.lab.dmmMode || 'V';
              labState.tool = proj.lab.tool || 'select';
              labState.selectedId = null;
              labState.pendingPin = null;
              labState.placingProbe = null;
              nextLabId = Math.max(
                1,
                ...labState.components.map(c => Number(c.id) + 1),
                ...labState.wires.map(w => Number(w.id) + 1)
              );""",
        "Restore lab controls and recalculate next component ID"
    ),
    (
        """      document.getElementById('btn-export-png').onclick = () => {
        let dataUrl = '';
        if (state.activeSection === 'laboratory') {
          dataUrl = document.getElementById('lab-canvas').toDataURL('image/png');
        } else {
          renderer.render(scene, camera);
          dataUrl = renderer.domElement.toDataURL('image/png');
        }
        const a = document.createElement('a');
        a.href = dataUrl;
        a.download = `BatteryLab3D_${state.packAnalysis?.topology || 'export'}.png`;
        a.click();
        showToast('Exported PNG snapshot.');
      };""",
        """      document.getElementById('btn-export-png').onclick = () => {
        try {
          let dataUrl = '';
          if (state.activeSection === 'laboratory') {
            const canvas = document.getElementById('lab-canvas');
            if (!canvas) throw new Error('Laboratory canvas is unavailable.');
            dataUrl = canvas.toDataURL('image/png');
          } else {
            if (!renderer || !scene || !camera) throw new Error('3D renderer is unavailable.');
            renderer.render(scene, camera);
            dataUrl = renderer.domElement.toDataURL('image/png');
          }
          const a = document.createElement('a');
          a.href = dataUrl;
          a.download = `BatteryLab3D_${state.packAnalysis?.topology || 'export'}.png`;
          document.body.appendChild(a);
          a.click();
          a.remove();
          showToast('Exported PNG snapshot.');
        } catch (error) {
          console.error('PNG export failed:', error);
          showToast('PNG export failed. The canvas may be unavailable or blocked.', 'error');
        }
      };""",
        "Handle PNG export failures safely"
    ),
    (
        """      document.getElementById('btn-reset-all').onclick = () => {
        loadBatteryPackPreset('1s1p');
        loadLabCircuitPreset('led_resistor');
        showToast('Workspace reset to default.');
      };""",
        """      document.getElementById('btn-reset-all').onclick = () => {
        if (!window.confirm('Reset the entire workspace? Saved projects will not be deleted.')) return;
        loadBatteryPackPreset('1s1p');
        loadLabCircuitPreset('led_resistor');
        showToast('Workspace reset to default.');
      };""",
        "Confirm workspace reset before clearing it"
    ),
]

# Validate all source anchors before making any change.
for old, new, label in replacements:
    count = source.count(old)
    if count != 1:
        sys.exit(f"STOP: {label}: expected exactly 1 matching source block, found {count}. No edits were made.")

for old, new, label in replacements:
    source = source.replace(old, new, 1)

if source == original:
    sys.exit("No changes were necessary.")

backup = target.with_name("index.html.backup")
if backup.exists():
    sys.exit("STOP: index.html.backup already exists. Rename it before running again.")

backup.write_text(original, encoding="utf-8")
target.write_text(source, encoding="utf-8")
print("Updated index.html successfully.")
print("Original backup saved as index.html.backup.")
print("Next: upload the updated index.html to the repository root.")
