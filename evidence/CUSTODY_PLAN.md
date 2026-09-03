# v3 custody instrumentation plan

Scientific source commit: `0eead840a1fc2f5de96d809b5e7b45ee14f7d726`

The custody workflow must check out this exact commit before validation and assay execution. Any commit that changes the workflow is instrumentation provenance only and is not the scientific source commit.

Required evidence:
- pytest output
- raw `structural_complexity_control_output.json`
- SHA-256 of the raw JSON
- provenance containing both the frozen scientific source SHA and the workflow/instrumentation SHA
- uploaded GitHub Actions artifact
