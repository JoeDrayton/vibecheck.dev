# vibecheck - the AI that vibe checks your PRs


https://github.com/user-attachments/assets/497f427e-182e-4446-ac0c-ed6f1ad8ea28


**vibecheck is a merge gate for GitHub pull requests. Before a PR can merge, the person who opened it has to show they understand their own change.**

## What is it?

You run vibecheck on your own server and add one workflow file to your repository. After that, every time someone opens a pull request:

1. vibecheck reads the code change and writes a few questions about it. The first is always *"How does this change work on a high level?"*
2. The author gets a link and answers in plain English, one question at a time, next to the part of the diff it is about.
3. An AI grader marks each answer against the actual change. A short but correct answer passes. An answer that contradicts the code fails.
4. If the author understands the change, the check goes green and the PR can merge. If not, the merge stays blocked.

A one-line PR gets one question. A big PR gets more. It is quick for someone who knows what they wrote, and impossible to wave through for someone who does not.

## Who is it for, and what do you get?

- **Reviewers and maintainers.** You stop receiving huge PRs from people who cannot explain them. The author has already been checked on the basics before you spend an hour reading.
- **Engineering teams and leads.** Confidence that a person on your team understands every change that ships, even when AI wrote most of it. Use AI to write code faster; vibecheck keeps a human in the loop who knows what it does.
- **Open source projects.** A cheap filter for drive-by, AI-generated pull requests that nobody has actually read.
- **Authors.** A fast way to catch a misunderstanding of your own change before a reviewer does.

## What problem is this solving?

It's far easier to write code than read and understand it, and AI has made that gap bigger. Reviewers end up with massive PRs, nobody has the energy to read them closely, and the result is burnout and rubber-stamping: "LGTM, CI is green." Then you are shipping code that nobody understands. For business critical software, that is unacceptable.

vibecheck does not review the code for you. It checks that the author understands it, which is the part a green CI cannot tell you.

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

- [Demo 1: Pass a PR](https://github.com/bhurghundii/vibecheck.dev/pull/53): answer well and `vibecheck/verdict` goes green.
- [Demo 2: Fail a PR](https://github.com/bhurghundii/vibecheck.dev/pull/54): answer badly and the merge stays blocked.

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
