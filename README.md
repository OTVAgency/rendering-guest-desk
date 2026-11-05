# Rendering… Guest Desk

Reusable guest-facing episode dashboards for OTV Network.

The dashboard layout, episode names, studio preview and thumbnail are public. Full video and caption links use separately restricted Google Drive files. Never upload raw recordings, caption files, transcripts, contact lists or credentials into this repository.

## Update an episode

Copy an episode folder, update its approved metadata and review asset links, then add an entry to episodes.json and the episode library. Grant the guest reader access on the linked Drive video and captions. Test the direct episode link and both Google account permissions before sending it. Each episode remains independently addressable.

Review comments and approvals are not collected by this static dashboard. Chapter buttons copy timestamps for feedback; use Drive to seek the recording.

## Hosting

GitHub Pages serves the main branch root. No custom domain or extra dependencies. The .nojekyll file preserves the static package. Barlow Condensed uses the included OFL license.

Run python3 -B check_pages.py and node --check assets/review.js before publishing.
