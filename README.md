# Motherland

English｜[中文](README.zh-CN.md)

The documentation and engineering baseline for all of my repositories. It governs five things: how documents are created, how they are written, how they are changed and deleted, how to tell whether a set is complete, and which language a module is written in.

The primary reader is the agent — the one actually editing the docs — and secondarily a human coming back six months later. That decides a few things: agents retrieve by filename and keyword, not by walking directories; an agent reads only the passage it grabbed, never the sentence you didn't write; and it copies port numbers, paths, and defaults from documents verbatim, without verifying them. So every criterion here must be decidable on the spot, and every template must be directly copyable.

## Paste this to your AI

To have your AI tidy your repositories' documentation against these standards, send it this paragraph:

```text
Read the Motherland repository: https://github.com/Tanramisu/Motherland and audit the documentation of every repository I own against its criteria: add what is missing, fix what is outdated, merge what is duplicated. Edit directly — do not wait for me to approve a plan first. When you are done, report per repository what you changed.

Finally, ask me: should I set up a scheduled task that runs every 24 hours and tidies these repositories' documentation to the Motherland standard automatically?
```

## How multiple repositories share this one baseline

**Registration.** A repository that adopts this baseline writes one line at the top of its own `docs/README.md` pointing here, and lists where it deviates and why. Unregistered is not an exception; it is drift.

**Propagation.** Whoever changes a criterion is responsible for pushing the change to registered repositories. Unregistered repositories are out of scope for that round. One change propagates one layer only: criteria, templates, and examples travel separately; do not refactor other people's documents on the side.

**Precedence.** Criteria > templates > examples. When a criterion changes, templates follow in the same batch; examples may lag a step, because they only illustrate.

This section records judgment formed from running several repositories this way; it has no controlled experiment behind it.

## The seven main criteria

1. **Write only what code and commit history cannot reconstruct.** Why something was designed this way, what was rejected, which operations fail silently, the real constraints of the field. Code structure is not written: reading code is faster, and code changes do not update docs. Literals that code can falsify — ports, defaults, version numbers, path lists — become a one-hop pointer to the source of truth, unless this page is their owner: a reference document owns its fields' defaults, and a snapshot like `status.md` owns the state at its moment; that is their job, not duplication. When a value in a document is stale while the code is right, an agent copies the stale one, confidently (pre-registered experiment, [surface-bench](https://github.com/Connorrmcd6/surface-bench/blob/main/PAPER.md)).
2. **One fact, one home.** The same sentence in two places means one of them is wrong, and you don't know which.
3. **Don't mix types.** A blueprint speaks of the future, a current-state document of the present, a decision of the past, a record only appends. Mixed on one page, you get sentences like "it does not own X, does not carry Y, is not a second Z" — no information at all.
4. **Say what it is first.** A definition must be precise enough for a reader to judge whether a new example counts. Negation appears only to block a real misunderstanding.
5. **Outdated: edit it. Superseded: delete it.** No "deprecated", no "used to be X, now Y". Deleted is deleted; git history is the backup. The one exception is deleting a page with an external URL, which leaves one hop behind — reasons and method in [`docs/lifecycle.md`](docs/lifecycle.md).
6. **Completeness is checked against a list.** The list comes from the code, the running system, and the paths readers actually walk — not from the existing documents. Mark each item covered, half-covered, or missing; add what's missing, fix what doesn't match.
7. **The reader can get there.** Filenames and titles are the main index: remembering one word must be enough to grep it and tell from the title which document it is. At most two guessy classification decisions along any path, each layer more specific than the one above. A complete list is not a sound structure — an index proves documents exist; names prove readers can find them.

The full criteria and the list of bad smells are in [`docs/what-good-means.md`](docs/what-good-means.md).

## Building a repository's documentation from scratch

1. Pick the archetype: one of the eight in [`docs/archetypes.md`](docs/archetypes.md); it decides which directories the repository needs.
2. Build the skeleton: the default in [`docs/structure.md`](docs/structure.md), minus the sections you don't need.
3. Write the entrance: the root `README.md` links once to `docs/README.md`; `docs/README.md` has an orientation layer and sections, each section with one hub, giving paths rather than a full inventory.
4. Type every document: one of the ten in [`docs/doc-types.md`](docs/doc-types.md); each document does one thing.
5. Write: [`docs/writing.md`](docs/writing.md). If the system isn't built yet, write the blueprint first, using the four-part addition method in [`docs/blueprint.md`](docs/blueprint.md).
6. Reconcile: list what should exist per criterion 8 of [`docs/what-good-means.md`](docs/what-good-means.md), mark each item covered, half-covered, or missing, then check per criterion 9 for pages with zero inbound links. Run the mechanical checks first: `python scripts/check-doc-links.py` scans each repository's root entrance files and `docs/` against the local checkouts listed in `REPOS.md`, and reports relative links that point nowhere and link targets written as local absolute paths like `D:/...` — the latter open fine on the author's machine and are guaranteed dead after a clone.

## Templates

| What you're writing | Copy this |
|---|---|
| Repository home page | [`README.template.md`](templates/README.template.md) |
| Working agreements for an agent | [`AGENTS.template.md`](templates/AGENTS.template.md) |
| Index page for `docs/` | [`index.template.md`](templates/index.template.md) |
| Where to start reading unfamiliar code | [`CODEMAP.template.md`](templates/CODEMAP.template.md) |
| What the system should eventually become | [`blueprint.template.md`](templates/blueprint.template.md) |
| What a system or module is now (type 4, current state) | [`reference.template.md`](templates/reference.template.md) |
| How to do something | [`how-to.template.md`](templates/how-to.template.md) |
| How to recover from a failure | [`runbook.template.md`](templates/runbook.template.md) |
| Why a decision was made | [`decision.template.md`](templates/decision.template.md) |
| A field's rules and terminology | [`domain.template.md`](templates/domain.template.md) |
| A retrospective, incident, or milestone | [`record.template.md`](templates/record.template.md) |

Each template's opening comment says who the reader is, what belongs, and what to cut. When you copy one, delete the comment with it and keep only the skeleton.

## The standards

| Question | Read |
|---|---|
| Should this be a document at all, and which kind | [`docs/doc-types.md`](docs/doc-types.md) |
| How to split directories, name files, when to split | [`docs/structure.md`](docs/structure.md) |
| Which skeleton fits my repository | [`docs/archetypes.md`](docs/archetypes.md) |
| Is this documentation set complete, what's missing | [`docs/what-good-means.md`](docs/what-good-means.md), system-level criteria 8 and 9 |
| Should I write a blueprint, and what goes in it | [`docs/blueprint.md`](docs/blueprint.md) |
| How to phrase this sentence, how to write a path | [`docs/writing.md`](docs/writing.md) |
| Which sentence to cut, which information must not be cut | [`docs/what-good-means.md`](docs/what-good-means.md) |
| Keep or delete an old document | [`docs/lifecycle.md`](docs/lifecycle.md) |
| See real good and bad examples | [`docs/examples.md`](docs/examples.md) |
| Which language an agent writes code in, and how | [`docs/language-rules.md`](docs/language-rules.md) |
| Publishing a repository as open source | [`docs/open-source.md`](docs/open-source.md) |

## Out of scope

- **What each repository's documents say.** This baseline gives shapes; content belongs to that repository.
- **Code structure, symbols, call graphs.** That is the live state of `codebase-memory-mcp`; copied into a document it is stale tomorrow. A CODEMAP says where to start reading, not a symbol index.
- **A repository index.** Which repository lives where and whether a local checkout exists: see [`REPOS.md`](REPOS.md).
- **Pushing rules into other repositories.** The rules here govern only this repository.

## Credentials

If you find what looks like a leaked credential, report it; do not act on it. Changing, deleting, moving, redacting, or rotating it is not the agent's call to make for the human.
