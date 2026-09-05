# Training Demo: Dependency-Lock Mismatch Runbook

> **Scope:** Fictional public training example. This is not a production runbook and contains no customer data, credentials, or internal endpoints.

## Trigger

Use this runbook when CI reports `DEPENDENCY_LOCK_MISMATCH`: the dependency manifest and lock file are inconsistent.

## Procedure

1. Identify the repository's package manager and its required version from version-controlled project configuration.
2. Create a clean working branch. Do not modify the default branch directly.
3. Regenerate the lock file using the repository's package manager and required version.
4. Review the diff. Confirm that changes are limited to dependencies implied by the manifest change.
5. Run the repository's targeted dependency-install and test checks.
6. Attach the lock-file diff and relevant test output to the review request.

## Escalation conditions

Escalate to the repository owner when any of the following is true:

- The required package-manager version cannot be determined.
- Regenerating the lock file changes unrelated packages.
- Targeted tests remain red after a clean regeneration.

Do not bypass integrity checks or hand-edit lock-file hashes.

## Demo question

> According to the “Training Demo: Dependency-Lock Mismatch Runbook”, when must the operator escalate? Cite the source.
