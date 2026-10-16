# Explore navigation publication

The portfolio and its product overview pages expose the company Explore directory at https://intentsolutions.io/projects/. The mobile portfolio navigation also links directly to the typing game overview, BLUE GOLD BLUE and Perception.

## Perception artifact provenance

Perception remains a generated application owned by `jeremylongshore/omarchy-listening-post-entry`. The navigation patch is source commit `02f3d07`, changing only public footer links and footer wrapping. The portfolio's deployed bundle predates that repository's current policy changes, so publishing the current whole application would exceed the navigation scope.

The deployed baseline was reproduced from application commit `8ab32e3`, using its committed lockfile versions and `VITE_PERCEPTION_API_URL=https://api.perception.intentsolutions.io`. Before the navigation patch, the build matched the deployed files exactly:

- `index-k8OO506T.js`: SHA256 `4743d8f8ee8b9b9629d3fdfa252be15d613044a11535e4076a20da1fcb57d4bc`
- `index-DQrSth7c.css`: SHA256 `2d680bb1952431bbaa21e353ba9c815ea164f969ee1eb2e31c5449c3ab3615fe`

Apply only the source diff from `02f3d07` to that baseline and run `npm --prefix web run build` with the same API origin. Publish the resulting hashed JS/CSS and update their generated HTML references, preserving the existing site analytics inclusion. Prior assets remain available for open tabs. No checkout, terms, pricing, API deployment, or production-bundle admission settings changed.

The source patch is also committed upstream so a later full application publication retains the links. Public navigation verification blocks provider calls and form submissions; it does not launch gameplay or enter customer accounts.
