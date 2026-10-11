# vibecheck - the AI that vibe checks your PRs

https://github.com/user-attachments/assets/9d8c28a7-a025-4d69-854c-651698859e1a

**Vibecheck is a merge gate that checks the author of the PR understands the change they are putting in.**

Before a PR can merge, vibecheck asks several questions about the PR (generated using AI.) The first question is always *"How does this change work on a high level?"* and vibecheck will block the PR until they answer technical questions well enough to convince a LLM grader. 

## What problem is this solving?

It's far easier to write code than read and understand it. This means that reviewers are often burdened with the task of reviewing massive PRs. 

The result? More burnout. People just say: "LGTM, CI is green" and now you are shipping code you don't understand! For business critical software, this is unacceptable.

## Features (so far)

- **An exam sheet for every PR.** vibecheck reads the diff once to form its own blind interpretation, then writes a short sheet: the fixed high-level question plus scoped questions, each anchored to a specific part of the diff. The author sees one question per screen, next to just the slice of the diff it is about.
- **Sized to the change.** One scoped question per 15 changed lines, up to `EXAM_QUESTION_COUNT`. A one-line PR gets one question, a 1,000-line monstrosity gets picked apart section by section, and nobody is quizzed on git headers.
- **Graded on submit, leniently.** Claude marks each answer against the blind interpretation. A terse but correct answer passes; contradicting the diff fails. Wrong answers can be retried, then vibecheck reveals the answer and moves on. "Explain it for me" gives a plain-language walkthrough of a section with no effect on the mark, and "Skip" gives up on a question.
- **No understanding? No merge.** The session passes once `PASSINGMARKS` screens are correct and fails as soon as that is out of reach. vibecheck reports it as a `vibecheck/verdict` commit status; require it in branch protection and the PR cannot merge until the author passes.
- **Good development practices check.** Oversized PRs and diffs are rejected before any question is asked. More coming soon.
- **Local first.** Self-hosted only: one Docker Compose command and it's running, and it works in enterprise environments. BYOK of course.
- **No GitHub App, no OAuth, no webhooks.** It's a FastAPI service that a GitHub Action talks to over a bearer token. Nothing to install on GitHub beyond a workflow file. Just keep the vibecheck token a secret.
- **Sarcastic mode.** For the thick skinned, vibecheck will brutally tear your understanding. I used to have a tech lead who did this. I miss them.

## Need a demo?

See it in action on real PRs:

- [Demo 1: Pass a PR](https://github.com/bhurghundii/vibecheck.dev/pull/30): answer well and `vibecheck/verdict` goes green.
- [Demo 2: Fail a PR](https://github.com/bhurghundii/vibecheck.dev/pull/27): answer badly and the merge stays blocked.

## Contributing

I am well aware of the irony of having vibe slop to deal with the problem of vibe slop. 

I **encourage AI generated PRs** over human ones. Why? Because the entire point is to help devs integrate vibe coding more safely. 

I still think humans > AI any day though. 

## Documentation

Full docs live at **https://bhurghundii.com/vibecheck.dev/** (source in [`docs/`](docs/)):

- [Quickstart](https://bhurghundii.com/vibecheck.dev/quickstart/): self-host it with Docker Compose
- [How it works](https://bhurghundii.com/vibecheck.dev/how-it-works/)
- [Wire it into a repo](https://bhurghundii.com/vibecheck.dev/wire-it-up/) and [block PRs until they pass](https://bhurghundii.com/vibecheck.dev/blocking-prs/)
- [Configuration](https://bhurghundii.com/vibecheck.dev/configuration/)
- [Deploying to Railway](https://bhurghundii.com/vibecheck.dev/deploy-railway/) and the [pre-launch security checklist](https://bhurghundii.com/vibecheck.dev/security/)
- [Local development](https://bhurghundii.com/vibecheck.dev/development/) and [limitations](https://bhurghundii.com/vibecheck.dev/limitations/)

## License
MIT
