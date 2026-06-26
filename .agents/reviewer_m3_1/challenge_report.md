## Challenge Summary

**Overall risk assessment**: HIGH

## Challenges

### [High] Challenge 1: Text Overflow & Layout Breakage in module10_histology.html

- **Assumption challenged**: The assumption that using `display: flex;` without word wrap constraints on `.keypoint` and `.warn-box` in `module10_histology.html` is layout-safe.
- **Attack scenario**: A user views the histology module on a narrow mobile device (e.g. ~320px viewport width) and encounters a long continuous string (such as an academic link, long chemical/anatomical term, or list of terms).
- **Blast radius**: The `.keypoint` or `.warn-box` will fail to wrap the text, causing the element to overflow horizontally. This breaks the grid layout, forces a horizontal scrollbar on the page, and compromises readability.
- **Mitigation**: Update `module10_histology.html` to align with the other 9 modules by using `display: block; position: relative; padding-left: 34px; word-break: break-word; overflow-wrap: break-word;` and positioning the pseudo-element icon absolutely at `left: 12px` and `top: 10px`.

### [High] Challenge 2: Broken Image Links & Rendering Failures in module01_general_anatomy.html

- **Assumption challenged**: The assumption that hardcoded `upload.wikimedia.org` URLs (containing specific thumbnail sizes like `960px` or `640px`) are stable and robust.
- **Attack scenario**: Wikimedia changes its thumbnail path hashing, updates the original image file (which changes the hash of the thumbnail folder), or deprecates specific thumb sizes.
- **Blast radius**: The hardcoded thumbnail URLs return a 404 or broken image icon.
- **Mitigation**: Convert all 13 hardcoded URLs in `module01_general_anatomy.html` to standard `Special:FilePath` redirect URLs (e.g. `https://commons.wikimedia.org/wiki/Special:FilePath/Human_anatomy_planes,_labeled.svg`), which are officially supported, redirect-resistant, and stable.

## Stress Test Results

- **Long continuous string in `.keypoint` (Module 10)** → Expected: Text wraps cleanly to next line. → Actual: Text overflows container horizontally, breaking box alignment. → **FAIL**
- **Long continuous string in `.keypoint` (Module 09)** → Expected: Text wraps cleanly to next line. → Actual: Text wraps properly within the box margins. → **PASS**
- **Wikimedia URL Stability (Module 01)** → Expected: Redirect-resistant stable URL endpoints (`Special:FilePath`). → Actual: Hardcoded thumbnail URLs pointing to specific resolutions. → **FAIL**

## Unchallenged Areas

- **Dynamic Server-side rendering / API integrations** — Reason not challenged: Out of scope. The modules are static HTML files designed for offline or CDN delivery.
- **Legacy Browser Support** — Reason not challenged: Modern layout rules like CSS Grid and absolute pseudo-elements are widely supported across current targets.
