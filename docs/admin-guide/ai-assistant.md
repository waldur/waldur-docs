# AI Assistant configuration

The Waldur AI Assistant provides natural language interaction for managing resources, discovering calls, and navigating the platform. It requires an OpenAI-compatible language model backend.

## Prerequisites

- An OpenAI-compatible inference service (vLLM, OpenAI API, Ollama)
- A model with function calling support
- Network access from the Waldur backend to the inference service

## Enabling the assistant

Enabling the assistant is a two-step process. The configuration page stays hidden until the feature flag is switched on.

### 1. Turn on the feature flag

Go to **Administration > User interface > Support workspace** and enable **Enable AI Assistant**.

### 2. Configure the backend

The settings page then appears at **Administration > Configuration > AI Assistant settings**.

!!! warning
    `AI_ASSISTANT_ENABLED_ROLES` defaults to `disabled`. Setting `AI_ASSISTANT_ENABLED` to `True` on its own is not enough — no user will see the assistant until a role is selected as well.

## Configuration

All settings are managed through the Constance admin interface at **Administration > Configuration > AI Assistant settings**.

### Core settings

| Setting | Description | Default |
|---|---|---|
| `AI_ASSISTANT_ENABLED` | Master on/off switch for the feature and all calls to the inference service | `False` |
| `AI_ASSISTANT_ENABLED_ROLES` | Who can access: `disabled`, `staff`, `staff_and_support`, `all`, `anonymous` | `disabled` |
| `AI_ASSISTANT_BACKEND_TYPE` | LLM provider type: `vllm`, `openai`, `ollama` | `vllm` |
| `AI_ASSISTANT_API_URL` | Base URL for the LLM service (e.g., `https://llm.example.com/v1`) | — |
| `AI_ASSISTANT_API_TOKEN` | Authentication token for the LLM service | — |
| `AI_ASSISTANT_MODEL` | Model identifier (e.g., `gpt-4`, `qwen3.5-122b`) | `qwen3.5-122b-nothinking` |
| `AI_ASSISTANT_NAME` | Display name for the assistant persona | `Waldur Assistant` |

The `anonymous` role is a superset of `all`: every authenticated user gets the full assistant, and unauthenticated visitors additionally get the public discovery assistant. See [Public assistant](#public-assistant) below.

!!! tip
    Roll out in stages. Start with `staff` to verify the model behaves as expected with your own team, then switch to `all` to open the assistant to end users.

### Advanced settings

| Setting | Description | Default |
|---|---|---|
| `AI_ASSISTANT_SYSTEM_PROMPT_CUSTOM_INSTRUCTIONS` | Extra instructions injected into the system prompt — organisation context, terminology, FAQ content. Supports `{assistant_name}` and `{organization}` placeholders | — |
| `AI_ASSISTANT_COMPLETION_KWARGS` | JSON override for temperature, top_p, max_tokens, etc. | `{}` |
| `AI_ASSISTANT_STREAM_TIMEOUT_SECONDS` | Hard timeout for a full streaming request including LLM completion | `120` |
| `AI_ASSISTANT_TOKEN_LIMIT_DAILY` | Daily token limit per user (-1 = unlimited) | `-1` |
| `AI_ASSISTANT_TOKEN_LIMIT_WEEKLY` | Weekly token limit per user | `-1` |
| `AI_ASSISTANT_TOKEN_LIMIT_MONTHLY` | Monthly token limit per user | `-1` |
| `AI_ASSISTANT_GLOBAL_DAILY_TOKEN_BUDGET` | Site-wide daily token cap across all traffic, authenticated and anonymous (-1 = unlimited) | `5000000` |
| `AI_ASSISTANT_GLOBAL_REQUESTS_PER_MINUTE` | Site-wide burst cap across all assistant traffic | `60` |
| `AI_ASSISTANT_HISTORY_LIMIT` | Maximum past messages in context | `50` |
| `AI_ASSISTANT_SESSION_RETENTION_DAYS` | Days to retain chat history | `90` |
| `AI_ASSISTANT_INJECTION_ALLOWLIST` | Comma-separated phrases that bypass prompt injection detection | — |

!!! tip
    Per-user limits and the site-wide budget are independent. Per-user caps stop one person exhausting the service; `AI_ASSISTANT_GLOBAL_DAILY_TOKEN_BUDGET` bounds total spend regardless of how many users are active.

### Setting per-user token limits

The `AI_ASSISTANT_TOKEN_LIMIT_*` settings above are system-wide defaults. Individual users can be given their own limits, which override the defaults for that user only.

Go to **Support > Users** and expand the row of the user you want to adjust. The expanded panel shows current usage against the effective limit for all three periods, and lets you set a per-user value for each.

| Value | Effect |
|---|---|
| Left empty | Use the system default from the settings above |
| `-1` | Unlimited — no quota enforcement for this user |
| `0` or a positive integer | Specific token limit for this period |

Setting per-user limits requires staff or support permissions. The panel is only visible when the AI Assistant feature flag is enabled.

The same operations are available through the API — `POST /api/chat-quota/set_quota/` to set a user's limits, and `GET /api/chat-quota/usage/?user_uuid=<uuid>` to read another user's current usage.

### Helm configuration

When deploying via Helm, set the AI Assistant values:

```yaml
waldur:
  constance:
    AI_ASSISTANT_ENABLED: true
    AI_ASSISTANT_ENABLED_ROLES: "all"
    AI_ASSISTANT_BACKEND_TYPE: "vllm"
    AI_ASSISTANT_API_URL: "https://llm.example.com/v1"
    AI_ASSISTANT_MODEL: "your-model-name"
```

!!! warning
    Set `AI_ASSISTANT_API_TOKEN` through a Kubernetes secret or environment variable, not in the Helm values file.

## Custom system prompts

Beyond `AI_ASSISTANT_SYSTEM_PROMPT_CUSTOM_INSTRUCTIONS`, administrators can create named system prompt records and activate one at a time. An active record overrides the Constance instructions.

Custom instructions are injected as an additive section. The core prompt structure — persona, scope boundaries, tool instructions, and UI capabilities — remains immutable, so a custom prompt cannot disable the assistant's safety or permission behaviour.

## Health check

Verify the AI Assistant configuration:

```bash
waldur ai_assistant health
```

This checks:

1. Configuration completeness
2. Network connectivity to the LLM service
3. Model response capability

A broader `run_all` subcommand additionally validates evaluation scenarios and runs them against the configured model:

```bash
waldur ai_assistant run_all
```

## Available tools

The AI Assistant uses a tool system that allows it to query the Waldur database and perform actions on behalf of the user. Tools are grouped into categories and filtered by user role. Every tool enforces the same permission checks as the REST API, so a user can only reach data they could already see in the UI.

### Account tools

| Tool | Description | Access |
|---|---|---|
| `list_organizations` | List organizations the user has access to | All users |
| `list_projects` | List projects the user has access to | All users |
| `get_project_resources` | Fetch resources for a project, with state and offering | All users |
| `get_project_quota` | Fetch quota limits and current usage for a project | All users |
| `get_resource_usage` | Component usage (CPU hours, RAM-GB-hours, storage) for the current billing period | All users |
| `explain_project_credit_balance` | Explain how much credit was allocated and spent for a project | All users |
| `list_overdrawn_projects` | List projects that have spent more than their allocated credit | All users |
| `explain_resource_paused_reason` | Report why a resource is paused and what clears it | All users |
| `explain_invoice_compensations` | Explain credit compensations and manual cost adjustments on an invoice | All users |
| `get_customer_credit_overview` | Whole-organization credit overview in a single call | All users |
| `get_user_overview` | Snapshot of another user's organizations, projects, resources and pending orders | Staff and support |

### Resource management tools

| Tool | Description | Access |
|---|---|---|
| `display_user_resources` | List the user's active cloud resources | All users |
| `plan_vm` | Iteratively gather VM parameters and return a preview for confirmation | All users |
| `create_vm` | Create the OpenStack VM after the user confirms the `plan_vm` preview | All users |

### Marketplace tools

| Tool | Description | Access |
|---|---|---|
| `search_offerings` | Search publicly viewable offerings by keyword, category or type | All users |
| `get_offering` | Full details for one offering, including plans and components | All users |
| `list_categories` | List categories containing at least one publicly viewable offering | All users |
| `compare_offerings` | Compare two or more offerings across provider, category and specification | All users |

### Proposal research tools

| Tool | Description | Access |
|---|---|---|
| `find_matching_calls` | Find open calls matching the user's research project | All users |
| `list_calls` | Browse calls, filtered by state, round status or managing organization | All users |
| `list_proposals` | List proposals the user can see | All users |
| `guide_proposal` | Explain what a specific call requires for submission | All users |
| `proposal_overview` | Summarize a proposal: project, team, resource requests, review status | All users |

### Proposal review tools

| Tool | Description | Access |
|---|---|---|
| `review_workload` | Reviewer's pending reviews, prioritized by deadline | All users |
| `review_assistant` | Analyze a proposal against the call's criteria | All users |
| `call_insights` | Call health: submission trends, review bottlenecks, score patterns | Staff only |

!!! note
    `review_workload` and `review_assistant` are available to every user, but return data only for proposals the caller is actually assigned to review. Availability of a tool and the scope of the data it returns are enforced separately.

### Meta-tools

Two tools are always available and need no configuration. `search_tools` lazily fetches tool specifications by category, which keeps the system prompt small; it only ever returns tools the caller is permitted to use. `ask_user` lets the assistant ask structured multiple-choice questions when required detail is missing.

## Public assistant

Setting `AI_ASSISTANT_ENABLED_ROLES` to `anonymous` additionally exposes a public, unauthenticated assistant for service discovery. Visitors can explore the marketplace catalog without logging in.

The public assistant uses a fixed, read-only tool surface — the four marketplace tools plus `ask_user`. It has no access to account, resource, VM or proposal tools, and `search_tools` is not offered.

### Public assistant settings

| Setting | Description | Default |
|---|---|---|
| `ANONYMOUS_CHAT_USER_SLUG_SALT` | Scrypt salt for per-IP pseudonymous identifiers. Empty disables slug computation | — |
| `ANONYMOUS_CHAT_FEEDBACK_TOKEN_SECRET` | HMAC-SHA256 secret for feedback anti-replay tokens | — |
| `ANONYMOUS_CHAT_CATALOG_MAX_ENTRIES` | Cap on offerings injected into the public assistant's catalog summary | `50` |
| `ANONYMOUS_CHAT_REVIEW_ENABLED` | Master toggle for the nightly LLM-as-judge session review | `True` |
| `ANONYMOUS_CHAT_REVIEW_DAILY_TOKEN_BUDGET` | Independent budget for the judge, so review cannot starve user-facing traffic | `2000000` |
| `ANONYMOUS_CHAT_ARTIFACT_RETENTION_DAYS` | Days of inactivity before pseudonymous bookkeeping rows are purged (-1 disables) | `30` |

Anonymous traffic is budgeted per IP across daily, weekly and monthly windows, and sessions are pinned to their originating IP address — requests from a different address are rejected. Site-wide caps (`AI_ASSISTANT_GLOBAL_DAILY_TOKEN_BUDGET`, `AI_ASSISTANT_GLOBAL_REQUESTS_PER_MINUTE`) apply to authenticated and anonymous traffic together.

### Automated session review

When `ANONYMOUS_CHAT_REVIEW_ENABLED` is on, a nightly task runs an LLM-as-judge pass over completed public sessions, scoring answer quality and auditing the offering links the assistant produced. It reuses `AI_ASSISTANT_API_URL`, `AI_ASSISTANT_API_TOKEN` and `AI_ASSISTANT_MODEL`, but draws from its own token budget so it cannot compete with live traffic.

Review results are stored alongside any human thumbs-up/thumbs-down feedback, giving support staff a combined quality signal.

## Monitoring and support access

Staff and support users can review assistant activity from the support workspace.

| Data | Endpoint | Access |
|---|---|---|
| Per-user token consumption | `GET /api/chat-quota/usage/` | Own usage for any user; staff and support can query others via `user_uuid` |
| Authenticated chat sessions | `GET /api/chat-sessions/` | Staff and support see all; users see their own |
| Public assistant transcripts | `GET /api/anonymous-chat-interactions/` | Staff and support |
| Public assistant conversations, grouped | `GET /api/anonymous-chat-interactions/conversations/` | Staff and support |
| Public assistant KPIs | `GET /api/anonymous-chat-interactions/kpi/` | Staff and support |
| Budget snapshot | `GET /api/anonymous-chat-interactions/budget/` | Staff and support |
| Feedback and judge review results | `GET /api/anonymous-chat-feedbacks/` | Staff and support |

Opening another user's chat session or thread is recorded in that user's audit log, under the `chat` event group. Viewing your own conversations is not logged, and neither is listing sessions — only opening an individual conversation.

For the support-facing workflow, see [AI assistant log review](../user-guide/staff-users/service-desk/ai-assistant-log-review.md).

## Security considerations

- The AI Assistant sends structured data to the external LLM service for response generation
- All tool calls enforce the same permission checks as the REST API
- Prompt injection detection is built in — incoming messages are scored, and flagged messages are filtered and logged with severity and categories
- Tool arguments are re-checked for injection before execution, not just the original user message
- PII and credential detection flags sensitive content before it reaches the model
- `AI_ASSISTANT_INJECTION_ALLOWLIST` can exempt specific phrases when legitimate domain vocabulary triggers false positives
- Token usage is tracked per user for quota enforcement, and site-wide for total spend
- All chat sessions are auditable, and staff access to another user's session is logged
