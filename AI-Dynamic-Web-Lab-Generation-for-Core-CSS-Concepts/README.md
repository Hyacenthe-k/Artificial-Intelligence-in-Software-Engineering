# AI: Dynamic Web Lab Generation for Core CSS Concepts

Part of my **Artificial Intelligence in Software Engineering** repository.

## Objective

Use sequential, contextual AI prompting to generate single-file HTML/CSS/JS tools that visualize core CSS concepts: the Box Model, the `display` property, and the Flexbox/Grid layout systems.

## AI Tool Used

Gemini (Canvas) for generating the single-file HTML/CSS/JS applications.

## Files

| File | Description |
|---|---|
| `box-model-lab-initial.html` | **Prompt 1 output.** Box Model & Display lab with Box 1 (controlled) and Box 2 (reference). Sliders for padding, margin, border-width and width, plus a `display` dropdown (block, inline-block, inline). Content, padding, margin and border are color-coded. |
| `box-model-lab-refined.html` | **Prompt 2 output (refactor).** Same lab, now with individual top/right/bottom/left sliders for margin, padding and border, plus a corner-radius slider and a live CSS readout. |
| `flexbox-grid-playground.html` | **Prompt 3 output.** Separate playground with a container and 5 items. Dropdowns for `display`, `flex-direction`, `justify-content`, `align-items` and `grid-template-columns`, all updating the container in real time. |

## Prompts Used

1. **Initial Box Model prompt:** generate an interactive page with Box 1 and Box 2, color-differentiated content/padding/margin areas, sliders (padding, margin, border-width, width) with live pixel labels, and a `display` dropdown (block / inline-block / inline) wired up with JavaScript.
2. **Refinement prompt:** *"Implement sliders to adjust the margin, padding, and border for each side (top, right, bottom, left) individually, and add a separate slider for the corner radius."*
3. **Flexbox/Grid prompt:** generate a playground with a container, 5 items, and dropdowns for display, flex-direction, justify-content, align-items and grid-template-columns, updating in real time.

The full prompt text and screenshots are in the submitted Google Doc.

## How to Run

No build step. Download any `.html` file and open it in a browser.

## What I Learned

- Seeing `display: inline` ignore `width` and vertical margins in real time makes the box model click faster than reading the spec.
- Iterating with a refinement prompt (instead of one giant prompt) produced cleaner, more controllable code, the same way real feature work is done in small increments.
- `justify-content` and `align-items` behave differently across flex and grid, and the playground makes those differences obvious.
