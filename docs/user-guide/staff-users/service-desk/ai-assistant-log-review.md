# Reviewing AI Assistant chat sessions

This guide helps helpdesk staff review the conversations users have had with the
Waldur AI Assistant — to follow up on a support request, audit flagged content,
or understand how the assistant is being used.

!!! note
    The review pages are available to **staff** and **support** users when the
    AI Assistant is enabled. For turning the assistant on and configuring it, see
    [AI Assistant configuration](../../../admin-guide/ai-assistant.md).

## Accessing the chat session logs

1. Select **Support** from the left-hand menu.
2. Click **Logs** from the top menu.
3. Open the **AI assistant logs** tab.

A table opens listing every chat session (thread). Each row shows:

* The **user** and their organization.
* The **thread name** (auto-generated from the conversation).
* The number of **messages** and the **token** usage of the session.
* Whether the session is **flagged**, its **max severity**, and whether the user
  left **feedback**.
* When the session was **created** and last **modified**.

## Finding a specific session

The table can be narrowed down in two ways.

### Search by keyword or phrase

Use the **search box** above the table to find sessions by their content. The
search covers:

* The **conversation itself** — both the user's questions and the assistant's
  replies.
* The **thread name**.
* The **user** — username, name, or email address.

The search understands natural phrasing, so you can type a few keywords
(`resize openstack volume`) or wrap an exact phrase in quotes
(`"quota exceeded"`) to match it as a whole.

!!! tip
    Content search matches word stems, so `resizing` also finds sessions that
    mention `resize`. If a search returns too many results, add another keyword
    or switch to an exact quoted phrase.

### Filter by attribute

Use the column filters to focus on a subset of sessions:

* **User** — sessions belonging to a specific person.
* **Flagged** — sessions where the input guards flagged a message.
* **Feedback** — sessions where the user rated a reply.
* **Max severity** — the highest severity detected in the session
  (`Critical`, `High`, `Medium`, `Low`, or `None`).

Filters and the search box combine, so you can, for example, search for a
keyword *and* restrict the results to flagged sessions.

## Reviewing a conversation

Expand a row to read the full transcript of the session. For each turn you can
see the user's message, the assistant's response, and any warning raised by the
input guards (for example, redacted personal data or a detected prompt-injection
attempt).

!!! warning
    Chat sessions may contain personal data. Access is restricted to staff and
    support users and every review is auditable — only open sessions you have a
    legitimate support reason to review.

## Related

* [AI Assistant configuration](../../../admin-guide/ai-assistant.md) — enabling
  the assistant, access roles, token limits, and session retention.
* [Service desk interactions](service-desk-interactions.md) — managing support
  tickets raised by users.
