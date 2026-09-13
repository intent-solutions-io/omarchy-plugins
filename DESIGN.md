---
name: Intent Solutions OMA Portfolio
description: A restrained evidence workshop for clear, source-backed Omarchy surfaces.
colors:
  canvas: "#f6f6f4"
  surface: "#ffffff"
  ink: "#111114"
  ink-soft: "#2f3036"
  muted: "#62636b"
  rule: "#d8d8d3"
  rule-strong: "#9b9b95"
  dark-rule: "#66666d"
  orange: "#ff8f55"
  orange-deep: "#a93d0b"
  orange-soft: "#fff0e8"
  green: "#08745a"
  green-soft: "#dff5ed"
  preview-surface: "#101114"
  preview-muted: "#c7c7c2"
  text-on-dark-muted: "#bdbdc3"
  command-text: "#a8efd8"
  beacon-forest: "#18221b"
  beacon-paper: "#eef1e9"
  beacon-moss: "#315b46"
  beacon-ember: "#f97316"
  beacon-teal: "#086976"
  beacon-gold: "#f4c542"
  beacon-correction: "#a43d2b"
  perception-deep: "#0c141b"
  perception-panel: "#101a22"
  perception-ink: "#e8edf0"
  perception-muted: "#93a2ab"
  perception-line: "#2a3942"
  perception-signal: "#63c7c5"
  perception-route: "#efa84a"
  bluegold-blue: "#0a5f89"
  bluegold-blue-deep: "#083b55"
  bluegold-blue-soft: "#dcecf4"
  bluegold-gold: "#e1a51d"
  bluegold-gold-soft: "#fff4d5"
  bluegold-night: "#102733"
  bluegold-paper: "#f2f7f9"
typography:
  display:
    fontFamily: "JetBrains Mono, SFMono-Regular, Consolas, Liberation Mono, monospace"
    fontSize: "clamp(3.7rem, 7.4vw, 7rem)"
    fontWeight: 800
    lineHeight: 1.01
    letterSpacing: "-0.035em"
  headline:
    fontFamily: "JetBrains Mono, SFMono-Regular, Consolas, Liberation Mono, monospace"
    fontSize: "clamp(2.4rem, 4.4vw, 4.5rem)"
    fontWeight: 700
    lineHeight: 1.06
    letterSpacing: "-0.035em"
  title:
    fontFamily: "JetBrains Mono, SFMono-Regular, Consolas, Liberation Mono, monospace"
    fontSize: "1.42rem"
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: "-0.04em"
  body:
    fontFamily: "IBM Plex Sans, Segoe UI, Helvetica, Arial, sans-serif"
    fontSize: "16px"
    fontWeight: 400
    lineHeight: 1.65
  label:
    fontFamily: "JetBrains Mono, SFMono-Regular, Consolas, Liberation Mono, monospace"
    fontSize: "0.72rem"
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: "0.04em"
rounded:
  square: "0"
  circle: "50%"
spacing:
  gutter: "20px"
  xs: "8px"
  sm: "12px"
  md: "16px"
  lg: "22px"
  xl: "24px"
  section: "clamp(76px, 9vw, 132px)"
components:
  button-primary:
    backgroundColor: "{colors.orange}"
    textColor: "{colors.ink}"
    rounded: "{rounded.square}"
    padding: "0 20px"
    height: "48px"
  button-quiet:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.square}"
    padding: "0 20px"
    height: "48px"
  button-dark:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.surface}"
    rounded: "{rounded.square}"
    padding: "0 20px"
    height: "48px"
  input:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.square}"
    padding: "0 14px"
    height: "44px"
  card:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.square}"
    padding: "22px"
  bluegold-button:
    backgroundColor: "{colors.bluegold-blue-deep}"
    textColor: "#ffffff"
    rounded: "{rounded.square}"
    padding: "0 20px"
    height: "50px"
---

# Design System: Intent Solutions OMA Portfolio

## Overview

**Creative North Star: "The Evidence Workshop"**

The OMA portfolio is a restrained evidence workshop: engineered, calm, legible, and candid. It presents source-backed work in a light, paper-like field with strong typographic structure, deliberate rules, and dark structural panels when a sequence or proof state needs to hold attention. The interface is typography-led rather than illustration-led. Hierarchy comes from scale, whitespace, aligned rails, and rare functional color.

The shared portfolio surface is the default visual authority for the catalog and supporting pages. The Beacon Wakes, Perception, and BLUE GOLD BLUE surfaces can establish their own scoped palettes and signature compositions while retaining the same discipline of readable type, explicit state, and honest unfinished status. BLUE GOLD BLUE uses blue for protection and information, then reserves gold for its safety-gated change step.

**Key Characteristics:**
- Typography-led hierarchy with JetBrains Mono headings and labels.
- IBM Plex Sans body copy with generous readable line lengths.
- Light canvas, thin rules, square forms, and dark structural panels.
- Functional accents used sparingly to communicate state, action, or attention.

## Colors

The shared palette is near-white and black with orange for action and review, green for verified status, and cool gray rules. Product surfaces add scoped colors only when their subject requires a distinct state language.

### Primary
- **Signal Orange** (`{colors.orange}`): The shared action, review, and active-state accent. Use it for primary catalog actions, current states, and small structural markers.

### Secondary
- **Verified Green** (`{colors.green}`): A restrained confirmation signal for listed, complete, or verified states. Keep its use informational rather than decorative.

### Tertiary
- **BLUE GOLD BLUE protection blue** (`{colors.bluegold-blue}` and `{colors.bluegold-blue-deep}`): A scoped product-surface variant for protection, information, links, and primary interest actions.
- **BLUE GOLD BLUE change gold** (`{colors.bluegold-gold}`): A scoped product-surface variant for the safety-gated GOLD step and its explicit change emphasis.

### Neutral
- **Canvas** (`{colors.canvas}`): The shared page field.
- **Surface** (`{colors.surface}`): Cards, controls, and other raised light containers.
- **Ink** (`{colors.ink}`) and **Ink Soft** (`{colors.ink-soft}`): Primary and secondary text on light surfaces.
- **Muted** (`{colors.muted}`): Supporting copy, metadata, and secondary labels.
- **Rule** (`{colors.rule}`) and **Rule Strong** (`{colors.rule-strong}`): Thin separators, borders, and table-like rails.
- **Dark Rule** (`{colors.dark-rule}`): A divider used inside dark structural areas.
- **Preview Surface** (`{colors.preview-surface}`) and **Preview Muted** (`{colors.preview-muted}`): Catalog preview fields and their missing-image labels.

### Named Rules

**The Rare Accent Rule.** Color is a functional signal. Use an accent to identify an action, state, route, or exception, and let the surrounding light field and dark structure carry the rest of the hierarchy.

## Typography

**Display Font:** JetBrains Mono (with SFMono-Regular, Consolas, Liberation Mono, and monospace fallbacks)
**Body Font:** IBM Plex Sans (with Segoe UI, Helvetica, Arial, and sans-serif fallbacks)
**Label/Mono Font:** JetBrains Mono

**Character:** The pairing is technical without becoming cold. JetBrains Mono gives headings, labels, statuses, and controls a measured instrument-panel voice, while IBM Plex Sans keeps explanation and form guidance open and readable.

### Hierarchy
- **Display** (800, `clamp(3.7rem, 7.4vw, 7rem)`, `1.01`): Large portfolio and product hero statements, set in uppercase where the surface uses the shared catalog treatment.
- **Headline** (700, `clamp(2.4rem, 4.4vw, 4.5rem)`, `1.06`): Section headings and major explanatory statements.
- **Title** (700, `1.42rem`, `1.15`): Catalog card names and compact content titles.
- **Body** (400, `16px`, `1.65`): Explanatory copy, metadata context, and form guidance. Keep long passages near the established 65 to 75 character reading measure where the layout allows.
- **Label** (700, `0.72rem`, `1.4`, `0.04em`): Navigation, status, filters, controls, and other uppercase operational text.

### Named Rules

**The Instrument Label Rule.** Use the mono face for operational language and state. Do not turn body paragraphs into labels or use display scale where a compact status marker is clearer.

## Layout

The shared shell uses a centered container capped at 1240px with a 20px minimum side gutter. Desktop compositions favor two-column grids with the reading or explanatory column beside a proof, signal, or action panel. Catalog and ledger sections use generous vertical blocks, usually in the 76px to 132px range, while controls and cards use compact 8px to 24px gaps. Thin rules create aligned rails for filters, trust strips, status rows, and option lists.

At 980px, multi-column product compositions collapse to one column and trust strips move to two columns. At 620px, the shell narrows to a 14px side gutter, option rows and form grids become single-column, and BLUE GOLD BLUE exposes its compact sequence line before the route board. The Perception variant uses a separate 1280px dark signal shell and its own inline palette. Preserve readable line length, 44px or larger interactive targets, and visible focus treatment at every width.

## Elevation & Depth

The shared portfolio is mostly flat and derives depth from tonal contrast, borders, whitespace, and dark structural panels. Interactive catalog cards and buttons use the established hard offset shadow on hover. BLUE GOLD BLUE adds one diffuse shadow to its route board so the proof sequence reads as a contained instrument. Do not add ambient shadows to ordinary text blocks, rails, or fields.

### Shadow Vocabulary
- **Hard interaction offset** (`5px 5px 0 var(--ink)`): Shared button and catalog-card hover state.
- **BLUE GOLD BLUE route board depth** (`0 20px 48px rgba(0, 0, 0, 0.18)`): Scoped depth for the dark sequence board on the research surface.

### Named Rules

**The Structural Depth Rule.** Establish hierarchy with surface tone, rules, and whitespace first. A shadow is a state or signature treatment, not a default decoration.

## Shapes

The form language is square and editorial. Buttons, inputs, selects, cards, filters, and preview frames use no corner radius. Circular geometry is reserved for status dots and route nodes. Borders are usually one pixel, with two-pixel or four-pixel accents where a current state needs stronger registration. Clipping is purposeful and limited to preview media and route or field graphics.

## Components

### Buttons
- **Character:** Compact, uppercase, mono controls with a clear action hierarchy.
- **Shape:** Square corners (`0`), 48px minimum height in the shared portfolio and 50px on the BLUE GOLD BLUE form.
- **Primary:** Signal Orange background with ink text, 20px horizontal padding, and a one-pixel ink border.
- **Hover / Focus:** Hover lifts the control by 2px and applies the shared hard offset shadow. Focus uses the 3px orange outline with a 4px offset, with the BLUE GOLD BLUE surface changing the outline to its protection blue.
- **Quiet / Dark:** Quiet buttons keep a surface background with an ink border. Dark buttons use the ink background and surface text for actions placed on light page fields.
- **BLUE GOLD BLUE variant:** The primary action uses deep blue with white text. Gold is not a generic button color on this surface; it marks the safety-gated change step.

### Cards / Containers
- **Character:** Honest information blocks with a visible edge and a calm interior.
- **Corner Style:** Square (`0`).
- **Background:** Surface white on the shared canvas; dark structural panels are used where sequence or proof needs contrast.
- **Shadow Strategy:** Flat at rest; shared cards gain the hard offset shadow on hover.
- **Border:** One-pixel strong rule, with accent or top-edge changes for review and lifecycle states.
- **Internal Padding:** Catalog card bodies use 22px; larger callouts and product panels use responsive padding from the existing clamp values.

### Inputs / Fields
- **Style:** White field, one-pixel strong rule, square corners, and 44px shared minimum height. BLUE GOLD BLUE fields use a 50px minimum height and its scoped blue ink.
- **Focus:** A visible 3px outline with a 2px offset on BLUE GOLD BLUE fields, plus a deep-blue border shift. Shared fields retain the global visible focus treatment.
- **Error / Disabled:** Status text carries explicit success, error, and loading colors. Disabled BLUE GOLD BLUE actions wait, reduce opacity, and do not imply completion.

### Navigation
- **Style:** A 76px minimum header with a mono wordmark and mono navigation. The wordmark uses a vertical rule to separate company and product labels.
- **Default / Hover / Active:** Links inherit ink, keep a 44px minimum target, and reveal the orange inset underline on hover. Surface variants can use a dark filled interest link for the primary route.
- **Mobile treatment:** Preserve the compact header and let navigation wrap or collapse according to the existing surface rules. Do not reduce target size to preserve a single line.

### Status Rails
- **Style:** Trust strips, sequence rails, and option rows use thin horizontal rules, compact mono labels, and explicit state text. A dot, square, or colored segment is meaningful only when it maps to a known state.

### BLUE GOLD BLUE Route Board
- **Style:** A dark night panel containing four vertically connected steps. BLUE steps use protection blue, the gate remains neutral, and GOLD is the scoped change emphasis.
- **Behavior:** The board makes the order visible: save and verify, pass the safety gate, change, then restore. The final doctrine is presented as a gold block below the list.

## Do's and Don'ts

### Do:
- **Do** lead with the evidence, sequence, or status the visitor needs to understand.
- **Do** use JetBrains Mono for operational labels and IBM Plex Sans for explanatory copy.
- **Do** use whitespace, thin rules, and dark structural panels to create hierarchy before reaching for color.
- **Do** keep interactive targets at least 44px high and preserve visible keyboard focus.
- **Do** scope product palettes to their product surface. On BLUE GOLD BLUE, use blue for protection and information and gold for safety-gated change.
- **Do** make unfinished, under-review, and unknown states explicit in both copy and visual treatment.

### Don't:
- **Don't** replace evidence with fabricated renders, testimonials, prices, countdowns, availability claims, or endorsement language.
- **Don't** introduce illustration-led decoration where typography and structure already communicate the idea.
- **Don't** use rounded cards, pill controls, soft generic gradients, or ornamental shadows that are absent from the incumbent system.
- **Don't** turn the BLUE GOLD BLUE blue and gold semantics into a portfolio-wide color requirement.
- **Don't** use a bright accent as a large decorative wash when a rule, label, or state marker will communicate the same information.
