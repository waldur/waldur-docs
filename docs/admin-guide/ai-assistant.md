# AI Assistant configuration

The Waldur AI Assistant provides natural language interaction for managing resources, discovering calls, and navigating the platform. It requires an OpenAI-compatible language model backend.

## Prerequisites

- An OpenAI-compatible inference service (vLLM, OpenAI API, Ollama)
- A model with function calling support
- Network access from the Waldur backend to the inference service

## Configuration

All settings are managed through the Constance admin interface at **Administration > Settings > AI Assistant**.

### Core settings

| Setting | Description | Default |
|---|---|---|
| `AI_ASSISTANT_ENABLED` | Enable/disable the AI Assistant | `False` |
| `AI_ASSISTANT_ENABLED_ROLES` | Who can access: `disabled`, `staff`, `staff_and_support`, `all` | `disabled` |
| `AI_ASSISTANT_BACKEND_TYPE` | LLM provider type: `vllm`, `openai`, `ollama` | `vllm` |
| `AI_ASSISTANT_API_URL` | Base URL for the LLM service (e.g., `https://llm.example.com/v1`) | — |
| `AI_ASSISTANT_API_TOKEN` | Authentication token for the LLM service | — |
| `AI_ASSISTANT_MODEL` | Model identifier (e.g., `gpt-4`, `qwen3.5-122b`) | — |

### Advanced settings

| Setting | Description | Default |
|---|---|---|
| `AI_ASSISTANT_NAME` | Display name for the assistant | `Waldur Assistant` |
| `AI_ASSISTANT_COMPLETION_KWARGS` | JSON override for temperature, top_p, max_tokens, etc. | `{}` |
| `AI_ASSISTANT_TOKEN_LIMIT_DAILY` | Daily token limit per user (-1 = unlimited) | `-1` |
| `AI_ASSISTANT_TOKEN_LIMIT_WEEKLY` | Weekly token limit per user | `-1` |
| `AI_ASSISTANT_TOKEN_LIMIT_MONTHLY` | Monthly token limit per user | `-1` |
| `AI_ASSISTANT_HISTORY_LIMIT` | Maximum past messages in context | `50` |
| `AI_ASSISTANT_SESSION_RETENTION_DAYS` | Days to retain chat history | `90` |

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

## Health check

Verify the AI Assistant configuration:

```bash
waldur ai_assistant health
```

This checks:
1. Configuration completeness
2. Network connectivity to the LLM service
3. Model response capability

## Available tools

The AI Assistant uses a tool system that allows it to query the Waldur database and perform actions on behalf of the user. Tools are filtered by user role.

### Resource management tools

| Tool | Description | Access |
|---|---|---|
| `show_user_resources` | List user's active cloud resources | All users |
| `list_projects` | List accessible projects for VM creation | All users |
| `preview_vm` | Preview VM configuration before creation | All users |
| `create_vm` | Create OpenStack VM via marketplace | All users |

### Proposal management tools

| Tool | Description | Access |
|---|---|---|
| `find_matching_calls` | Discover calls matching research needs | All users |
| `guide_proposal` | Explain call requirements and preparation | All users |
| `review_workload` | Reviewer's pending work summary | All users |
| `proposal_overview` | Structured proposal summary | All users |
| `review_assistant` | Analysis for assigned reviewers | Assigned reviewers |
| `call_insights` | Call health and progress analysis | Staff only |

## Security considerations

- The AI Assistant sends structured data to the external LLM service for response generation
- All tool calls enforce the same permission checks as the REST API
- Prompt injection detection is built in — messages with detected injection attempts are filtered
- PII detection flags sensitive content before processing
- Token usage is tracked per user for quota enforcement
- All chat sessions are auditable

## Monitoring

Chat usage metrics are available via:

- **Token quota endpoints**: `GET /api/chat-quota/usage/` — per-user token consumption
- **Session history**: Accessible to staff via admin interface
- **Health check**: `waldur ai_assistant health` — infrastructure status
