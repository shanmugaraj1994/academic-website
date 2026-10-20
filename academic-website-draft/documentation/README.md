# Academic profile website

The website is in dist/. No build or installation is required. Open dist/index.html locally.

## Publish on GitHub Pages
Create a public repository named YOUR-USERNAME.github.io and upload the CONTENTS of dist/ to its root, including assets/, scripts/, .github/, and .nojekyll. Hidden directories must be included (Git command line or GitHub Desktop is easiest).

In Settings → Pages, set Source to GitHub Actions. The included workflow publishes on pushes to main and can be started manually under Actions. If your default branch is not main, update .github/workflows/pages.yml.

For a simpler setup without monthly updates, omit .github/ and scripts/, then use Settings → Pages → Deploy from a branch → main → / (root).

## Optional monthly citation updates
The displayed count is 162, confirmed by the owner on 19 October 2026. Automatic updates are NOT active yet.

1. Obtain a SerpApi API key for its Google Scholar Author API. Review the provider's terms and plan before use; no subscription or request was made here.
2. In the GitHub repository, Settings → Secrets and variables → Actions → Secrets, add SERPAPI_API_KEY. Never add a key to HTML, JavaScript, or source files.
3. Under Actions → Variables, add ENABLE_SCHOLAR_UPDATES with value true.
4. Allow GitHub Actions read/write access to repository contents. Set Pages Source to GitHub Actions as above.
5. Manually run the workflow once to verify setup. It then attempts a refresh on the first day of each month at 06:17 UTC. GitHub schedules may be delayed; scheduled workflows in public repositories can be disabled after 60 days without repository activity.

The action reads the all-time citation total for Scholar author tuuSnYMAAAAJ, validates the returned author and number, updates the count and date in both profile and CV, commits the result, and deploys Pages. On API failure it leaves the last successful count and date untouched, and the workflow reports failure. The key is used only in the GitHub runner. Visitors make no requests to SerpApi or Scholar.

Google Scholar does not offer a supported public profile-count API for direct browser integration. The provider above is a third-party service. Direct automated fetching can encounter rate limits and robots restrictions. Source: https://scholar.google.com/intl/en/scholar/help.html and https://serpapi.com/google-scholar-author-api.

## Content updates applied
- Email: shanmugarajcode94@gmail.com.
- Google Scholar, LinkedIn, and TUM links provided by the owner; portrait included unchanged.
- Materials and Structures paper listed as accepted in 2026; DOI pending. Other unpublished work omitted.
- Frontiers review uses publication year 2023, as requested in the latest revision.

## Remaining review items
- Appointment start: CV says November 2025; slides say 2026. Website says Current pending confirmation.
- Conference author lists are explicitly abbreviated. Check full proceedings citations if complete lists are preferred.
- Confirm laboratory/collaborator image permissions and individual credits before public launch (ASSETS.md).
- Add the Materials and Structures DOI once assigned.

Edit index.html for the profile and cv.html for the printable CV. Update shared publication details in both. styles.css controls appearance. Phone numbers and referee contact details are omitted from the public site.

The .openai directory outside dist/ records the unpublished Sites preview identity. It is not required for GitHub Pages. The ZIP contains the deployable root plus these instructions.

## Research presentation revision
The profile now leads with computer vision and digital construction. The manual, keyboard-accessible hero carousel covers visual analysis, camera/laser sensing, production digital twins, bridge monitoring, and adaptive robotic operations. Postdoctoral research is labelled ongoing; no completed results are asserted. Doctoral work is grouped under process and quality monitoring in 3D concrete printing. The original collapse GIF is available with opt-in playback and a stop control. Camera illustration and all research graphics come from the PPT; KEYENCE product imagery is credited separately as an equipment example.

## Industry experience revision
Dedicated Industry navigation and section added, with construction-site images from slide 4 and role descriptions grounded in the CV. CV job titles and month-level dates are used because the slide uses broader functional labels (Operations Engineer / Civil Planning Manager). Includes INR 1,200-crore project planning responsibility, four-member team leadership, seven-project coordination, client interfaces, resource management, and mentoring. Functional areas from slide 4 supplement these descriptions without claiming unsupported project outcomes. Industry responsibilities are also expanded in the printable CV.
