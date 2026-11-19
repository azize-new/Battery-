# Battery Lab 3D — Source Audit Report

**Target production URL:** https://battery.batterylab.workers.dev/  
**Audit basis:** uploaded `index.html` and its bundled PNG asset.  
**Deployment:** no production deployment was performed.

## Confirmed defects and changes

1. **MNA LED source polarity was reversed.** The Norton equivalent for the piecewise-linear LED model injected the forward-voltage source with the wrong sign. The default LED circuit therefore solved as an open/incorrect path, while the LED telemetry independently calculated about 112 mA. Corrected the source polarity. The same default circuit now solves at approximately **11.426 mA**, with the 220 Ω resistor and 2.2 V LED model in series, and returns a normal-operation diagnostic.
2. **LED threshold mismatch.** The burn/overcurrent flag used 55 mA while the warning text specified 50 mA. The threshold is now 50 mA.
3. **Runtime display rounding.** Rounding minutes separately could produce `1h 60m`. Runtime is now rounded to total minutes before splitting into hours and minutes.
4. **Constant-power load above the maximum-power-transfer point.** The calculator previously clamped to the maximum-power point without explaining that the requested power was infeasible. It now emits a warning when the requested load exceeds the modeled limit.
5. **Runtime presentation.** Added a caveat explaining that `Ah / A` is an idealized estimate and that usable capacity, temperature, aging, discharge-rate effects, BMS cutoff, voltage limits and wiring losses affect real runtime.
6. **Project-name injection and storage resilience.** Saved project names and dates are escaped before HTML insertion; toast text is escaped; malformed local-storage data is filtered; save/delete operations now handle storage exceptions.
7. **Idle rendering overhead.** Replaced the permanent Three.js animation-frame loop with render-on-demand scheduling. Frames continue while OrbitControls damping is active and stop when the scene is idle.
8. **Breadboard resize behavior.** Added a `ResizeObserver` and resize redraw so the canvas is recalculated when its container changes size.
9. **Mobile zoom and layout.** Removed `maximum-scale=1.0` and `user-scalable=no`; added dynamic viewport sizing, overflow guards, touch-target minimums and RTL drawer transform handling. Canvas touch behavior now permits page pinch zoom.
10. **SEO metadata.** Added a unique description, canonical URL, robots directive, Open Graph metadata, Twitter Card metadata and `SoftwareApplication` JSON-LD.
11. **Favicon path.** Corrected the favicon URL to include the `.png` extension.
12. **Initial telemetry placeholder.** Replaced the stale `0.0 mA` / `112 mA overcurrent` HTML placeholders with values consistent with the corrected default LED + 220 Ω circuit. JavaScript still recalculates the live values at startup.
13. **Heading hierarchy.** Made the application brand the single H1 and demoted the calculator section heading to H2.
14. **Crawler files.** Added `robots.txt` and a valid one-URL `sitemap.xml` for the production origin.
15. **Input bounds.** Added finite-value checks and reasonable upper/lower bounds to editable battery voltage, capacity, internal resistance and state-of-charge values.

## Automated checks performed

- JavaScript syntax check (`node --check`): **passed**.
- Battery topology calculations: **passed** for 1S1P, 3S1P, 1S3P and 2S2P.
- Default LED + 220 Ω circuit: **passed**, 11.426 mA; no overcurrent warning.
- Direct battery short-circuit detection: **passed**.
- Empty breadboard behavior: **passed**.
- Calculator finite runtime output: **passed**.
- Unachievable constant-power warning: **passed**.
- Empty-pack NaN/Infinity output check: **passed**.
- HTML parser pass: **passed**.
- Exactly one H1 and no duplicate element IDs: **passed**.
- JSON-LD parse: **passed**.
- Sitemap XML parse: **passed**.
- Favicon file existence and robots-to-sitemap reference: **passed**.
- Viewport zoom restriction scan: **passed** (no `user-scalable=no` or `maximum-scale=1`).

## Not fully verified / remaining limitations

- A full interactive browser session could not be completed in this environment. Therefore real touch behavior, visual layout at device breakpoints, WebGL rendering, Three.js OrbitControls, PNG download, project save/load through an actual browser, and browser-console/network errors remain unverified.
- The public production URL was reachable with HTTP 200 during the audit, but the deployed files were not changed. The updated `robots.txt`, `sitemap.xml`, favicon path and metadata will take effect only after the corrected files are deployed.
- The application contains English, French and Arabic dictionaries for its `data-i18n` interface labels. Many dynamically generated engineering warnings and toast messages remain hard-coded in English; complete dynamic-warning localization was not implemented in this pass.
- The MNA engine uses a simplified piecewise-linear LED model (fixed 25 Ω dynamic resistance) and a simplified DC circuit model. Results are educational estimates, not a substitute for SPICE-grade simulation or real-world electrical safety analysis.
- Runtime remains a theoretical estimate using nominal Ah divided by modeled current; the app does not yet implement a chemistry-specific discharge curve or cutoff-voltage integration.
- Cloudflare deployment configuration, HTTP response headers, canonical host behavior, and actual crawler access to the newly added sitemap/robots files must be checked after deployment.

## Deployment contents

- `index.html` — corrected application source.
- `robots.txt` — crawler policy and sitemap reference.
- `sitemap.xml` — production homepage sitemap.
- `file_00000000a4348210be5b9336c4ca200b.png` — existing application image/favicon.
- `googlebf01d3c2944aee75.html` — original Google Search Console verification file.
