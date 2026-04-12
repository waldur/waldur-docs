# AI Assistant

Waldur includes a built-in AI Assistant that helps users manage cloud resources and navigate the platform through natural language conversation.

## Overview

The AI Assistant can:

- **Discover calls for proposals** — find open calls matching your research needs
- **Guide proposal preparation** — explain call requirements, deadlines, and forms
- **Track review workload** — show pending reviews with priority and deadlines
- **Summarize proposals** — provide structured overviews of any proposal you have access to
- **Assist with reviews** — analyze proposals against call criteria for assigned reviewers
- **Provide call insights** — submission trends, review bottlenecks, and action items (staff only)
- **Manage cloud resources** — create VMs, list resources, manage projects

## Accessing the AI Assistant

The AI Assistant is available as a chat sidebar. Click the assistant icon in the navigation bar to open the conversation panel.

!!! note
    The AI Assistant must be enabled by your platform administrator. If you don't see the assistant icon, contact your admin.

## Example conversations

### Finding calls to apply to

> **You:** I need GPU hours for climate modeling simulations. Which calls can I apply to?
>
> **Assistant:** Based on your requirements, I found 2 matching calls:
>
> 1. **2025 GPU Research Program** — offers up to 5,000 GPU hours with A100 hardware
> 2. **2025 Spring HPC Allocation Call** — standard compute package with 100K CPU hours

### Understanding call requirements

> **You:** What do I need to prepare for the 2025 GPU Research Program call?
>
> **Assistant:** Here's what you need:
> - Institution type and accreditation certificate
> - Resource requirements: GPU hours (up to 5,000), storage
> - Research area selection and funding status declaration
> - Deadline: March 27, 2027

### Checking review workload

> **You:** What reviews do I have pending?
>
> **Assistant:** You have 3 reviews in progress, 1 completed, and 2 pending invitations.

### Getting call insights (staff/managers)

> **You:** How is the Spring HPC call going?
>
> **Assistant:** 4 proposals submitted, 2 in review, acceptance rate 75%. 1 reviewer has not started their assigned review.

## Available capabilities by role

| Capability | End users | Support | Staff |
|---|---|---|---|
| Find matching calls | Yes | Yes | Yes |
| Proposal guidance | Yes | Yes | Yes |
| Review workload | Yes | Yes | Yes |
| Proposal overview | Yes | Yes | Yes |
| Review assistant | Assigned reviewers | Yes | Yes |
| Call insights | — | — | Yes |
| Create VMs | Yes | Yes | Yes |
| List resources | Yes | Yes | Yes |

## Tips for better results

- **Be specific** about your research domain, resource needs, and timeframe
- **Mention call names** when asking about specific calls
- **Use proposal slugs** (e.g., "R1-001") when asking about specific proposals
- The assistant provides **clickable links** to navigate directly to relevant pages

## Privacy and data handling

- Conversations are stored per user and are private
- The assistant uses an external language model for generating responses
- Platform data accessed by the assistant respects your role permissions — you can only see data you have access to through the normal UI

!!! warning
    Do not share sensitive personal information (passwords, financial details) in the chat. The assistant processes your messages through an external AI service.
