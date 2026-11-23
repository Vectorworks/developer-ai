# Publishing to developer-ai

The **Promote to public repository** workflow creates a snapshot commit on a
new branch in `Vectorworks/developer-ai` and opens a pull request against its
`main` branch. It does not publish development Git history.

The branch is public as soon as it is pushed, before the pull request is
reviewed. Review the selected development revision for sensitive or
unreleased content before running the workflow. Every tracked file, including
`.github` files, is copied; files present only in the public repository are
proposed for deletion. Review the entire pull request before merging.

## One-time setup

1. Create a fine-grained personal access token for a service account or user
   authorized to write to `Vectorworks/developer-ai`. Restrict it to that
   repository and grant **Contents: read and write**, **Pull requests: read and
   write**, and **Workflows: read and write**. The workflow permission is
   needed when publishing changes under `.github/workflows`. Complete any
   organization authorization or approval required for the token.
2. Add the token as the `PUBLIC_REPO_TOKEN` Actions repository secret in
   `Vectorworks/developer-ai-dev`. Do not commit the token.
3. Ensure Actions is enabled in the development repository and that public
   repository rules permit the token owner to push a branch and open a pull
   request. Normal rules and required reviews still apply to merging.

## Promote a snapshot

After this workflow is available on the development repository's default
branch, open **Actions → Promote to public repository → Run workflow**, select
the development branch to publish, and run it. The selected revision's tracked
files replace the public `main` snapshot. If there are no differences, no
branch or pull request is created.

If creating the pull request fails after the push, the public branch remains
visible. Inspect or delete that branch in the public repository before retrying.
Token owners are responsible for rotating the secret when it expires.
